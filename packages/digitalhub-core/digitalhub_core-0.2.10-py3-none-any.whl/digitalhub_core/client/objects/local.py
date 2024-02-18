"""
Local Client module.
"""
from copy import deepcopy

from digitalhub_core.client.objects.base import Client
from digitalhub_core.utils.exceptions import BackendError


class ClientLocal(Client):
    """
    Local client.

    The Local client can be used when a remote Digitalhub backend is not available.
    It handles the creation, reading, updating and deleting of objects in memory,
    storing them in a local dictionary.
    The functionality of the Local client is almost the same as the DHCore client.
    Main differences are:
        - Local client does delete objects on cascade.
        - The run execution are forced to be local.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        self._db: dict[str, dict[str, dict]] = {}

    ########################
    # CRUD
    ########################

    def create_object(self, obj: dict, api: str) -> dict:
        """
        Create an object.

        Parameters
        ----------
        obj : dict
            The object to create.
        api : str
            The api to create the object with.

        Returns
        -------
        dict
            The created object.
        """
        project, dto, name, uuid, code = self._parse_api(api)
        try:
            # Check if dto is valid
            if dto is None:
                raise TypeError

            # Check if dto exists, if not create a mapping
            self._db.setdefault(dto, {})

            # Unversioned objects uses "base api". For example:
            #
            # POST /api/v1/projects
            # POST /api/v1/tasks
            # POST /api/v1/runs
            #
            # We do not have "name" attribute for tasks and runs
            # so we use the id to identify them. Projects has
            # the name attribute, not the id and is also not versioned,
            # so we use the name as storage key.
            if project is None:
                name = obj["name"] if dto == "projects" else obj["id"]
                if name in self._db[dto]:
                    code = 5
                    raise ValueError
                self._db[dto][name] = obj

            # Versioned objects uses "context api". For example:
            #
            # POST /api/v1/-/<project-name>/artifacts
            # POST /api/v1/-/<project-name>/functions
            # POST /api/v1/-/<project-name>/workflows
            #
            # We have bith "name" and "id" attributes for versioned objects
            # so we use them as storage keys. The "latest" key is used
            # to store the latest version of the object.
            else:
                name = obj["name"]
                uuid = obj["id"]
                self._db[dto].setdefault(name, {})
                self._db[dto][name][uuid] = obj
                self._db[dto][name]["latest"] = obj

            # Return the created object
            return obj

        # Key error are possibly raised by accessing invalid objects
        except (KeyError, TypeError):
            msg = self._format_msg(code, dto=dto)
            raise BackendError(msg)

        # If try to create already existing object
        except ValueError:
            msg = self._format_msg(code, dto=dto, name=name)
            raise BackendError(msg)

    def read_object(self, api: str) -> dict:
        """
        Get an object.

        Parameters
        ----------
        api : str
            The api to get the object with.

        Returns
        -------
        dict or None
            The object, or None if it doesn't exist.
        """
        project, dto, name, uuid, code = self._parse_api(api)
        try:
            # Unversioned objects
            # API examples
            #
            # GET /api/v1/projects/<name>
            #
            # self._parse_api() should return only dto

            if project is None:
                obj = self._db[dto][name]

                # If the object is a project, we need to add the project spec,
                # for example artifacts, functions, workflows, etc.
                if dto == "projects":
                    obj = self._get_project_spec(obj, name)

            # Versioned objects
            # API example
            #
            # GET /api/v1/-/<project-name>/artifacts/<uuid>
            #
            # self._parse_api() should return dto, name and uuid/version

            else:
                obj = self._db[dto][name][uuid]

            return obj

        except KeyError:
            msg = self._format_msg(code, project, dto, name, uuid)
            raise BackendError(msg)

    def update_object(self, obj: dict, api: str) -> dict:
        """
        Update an object.

        Parameters
        ----------
        obj : dict
            The object to update.
        api : str
            The api to update the object with.

        Returns
        -------
        dict
            The updated object.
        """
        project, dto, name, uuid, code = self._parse_api(api)
        try:
            # Unversioned objects
            # API example
            #
            # PUT /api/v1/projects/<name>

            if project is None:
                self._db[dto][name] = obj

            # Versioned objects
            # API example
            #
            # PUT /api/v1/-/<project-name>/artifacts/<uuid>

            else:
                self._db[dto][name][uuid] = obj

        except KeyError:
            msg = self._format_msg(code, project, dto, name, uuid)
            raise BackendError(msg)

        return obj

    def delete_object(self, api: str) -> dict:
        """
        Delete an object.

        Parameters
        ----------
        api : str
            The api to delete the object with.

        Returns
        -------
        dict
            A generic dictionary.
        """
        project, dto, name, uuid, code = self._parse_api(api)
        try:
            # Unversioned objects
            # API example
            #
            # DELETE /api/v1/projects/<name>

            if uuid is None:
                obj = self._db[dto].pop(name)

            # Versioned objects
            # API example
            #
            # DELETE /api/v1/-/<project-name>/artifacts/<uuid>
            #
            # We do not handle cascade in local client and
            # in the sdk we selectively delete objects by id,
            # not by name nor dto.

            else:
                obj = self._db[dto][name].pop(uuid)

        except KeyError:
            msg = self._format_msg(code, project, dto, name, uuid)
            raise BackendError(msg)
        return {"deleted": obj}

    ########################
    # Logic for CRUD
    ########################

    def _parse_api(self, api: str) -> list[str]:
        """
        Parse the given API.

        Parameters
        ----------
        api : str
            The API to parse.

        Returns
        -------
        list[str]
            The parsed API.
        """
        # Remove prefix from API
        api = api.removeprefix("/api/v1/")

        # Set context flag by default to False
        ctx = False

        # Remove context prefix from API and set context flag to True
        if api.startswith("-/"):
            ctx = True
            api = api[2:]

        # Remove delete flag from API. Local client does not handle cascade
        if api.endswith("?cascade=true") or api.endswith("?cascade=false"):
            api = api.removesuffix("?cascade=true").removesuffix("?cascade=false")

        # Return parsed elements
        return self._parse_api_elements(api, ctx)

    @staticmethod
    def _parse_api_elements(api: str, ctx: bool) -> tuple:
        """
        Parse the elements from the given API.
        Elements returned are: project-name, dto, name, uuid, error_code.

        Parameters
        ----------
        api : str
            The parsed API.
        ctx : bool
            True if the API is a context API.

        Returns
        -------
        tuple
            The parsed elements from the API.
        """
        # Split API path
        parsed = api.split("/")

        # Base API for versioned objects

        # POST /api/v1/<dto>
        # Returns None, dto, None, None
        if len(parsed) == 1:
            return None, parsed[0], None, None, 1

        # GET/DELETE/UPDATE /api/v1/<dto>/<name>
        # Return None, dto, name, None
        if len(parsed) == 2 and not ctx:
            return None, parsed[0], parsed[1], None, 2

        # Context API for versioned objects

        # POST /api/v1/-/<project>/<dto>
        # Returns project-name, dto, None, None
        if len(parsed) == 2 and ctx:
            return parsed[0], parsed[1], None, None, 1

        # GET/DELETE/UPDATE /api/v1/-/<project>/<dto>/<name>
        # Return project-name, dto, name, None
        if len(parsed) == 3:
            return parsed[0], parsed[1], parsed[2], None, 3

        # GET/DELETE/UPDATE /api/v1/-/<project>/<dto>/<name>/<uuid>
        # Return project-name, dto, name, uuid
        if len(parsed) == 4:
            return parsed[0], parsed[1], parsed[2], parsed[3], 4

    def _get_project_spec(self, obj: dict, name: str) -> dict:
        """
        Read the project spec.

        Parameters
        ----------
        obj : dict
            The project object.
        name : str
            The project name.

        Returns
        -------
        dict
            The project object with the spec.
        """
        # Deepcopy to avoid modifying the original object
        project = deepcopy(obj)
        spec = project.get("spec", {})

        # Get all entities associated with the project specs
        projects_entities = [k for k, _ in self._db.items() if k not in ["projects", "runs", "tasks"]]

        for entity_type in projects_entities:
            # Get all objects of the entity type for the project
            objs = self._db[entity_type]

            # Set empty list
            spec[entity_type] = []

            # Cycle through named objects
            for _, named_entities in objs.items():
                # Get latest version
                for version, entity in named_entities.items():
                    if version != "latest":
                        continue

                    # Deepcopy to avoid modifying the original object
                    copied = deepcopy(entity)

                    # Remove spec if not embedded
                    if not copied.get("metadata", {}).get("embedded", True):
                        copied.pop("spec", None)

                    # Add to project spec
                    if copied["project"] == name:
                        spec[entity_type].append(copied)

        return project

    ########################
    # Utils
    ########################

    @staticmethod
    def _format_msg(
        code: int,
        project: str = None,
        dto: str = None,
        name: str = None,
        uuid: str = None,
    ) -> str:
        """
        Format a message.

        Parameters
        ----------
        code : int
            The code to format the message with.
        project : str
            The project name.
        dto : str
            The DTO name.
        name : str
            The object name.
        uuid : str
            The object uuid.

        Returns
        -------
        str
            The formatted message.
        """
        msg = {
            1: f"Object '{dto}' to create is not valid",
            2: f"Object '{dto}' named '{name}' not found",
            3: f"Object '{dto}' named '{name}' for project '{project}' not found",
            4: f"Object '{dto}' named '{name}:{uuid}' for project '{project}' not found",
            5: f"Object '{dto}' named '{name}' already exists",
        }
        return msg[code]

    ########################
    # Interface methods
    ########################

    @staticmethod
    def is_local() -> bool:
        """
        Declare if Client is local.

        Returns
        -------
        bool
            True
        """
        return True
