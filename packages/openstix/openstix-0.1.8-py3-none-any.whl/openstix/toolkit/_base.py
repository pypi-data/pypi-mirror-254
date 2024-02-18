from stix2 import Environment, MemoryStore
from stix2.environment import ObjectFactory

from openstix import utils
from openstix.objects import Bundle

__all__ = [
    "Workspace",
    "ObjectFactory",
    "Environment",
]


class Workspace(Environment):
    """
    Extends the `stix2.Environment` class to provide a customized environment for handling
    STIX objects in a workspace context. Offers functionality for creating, querying, and
    removing STIX objects, including handling multiple versions of objects.
    """

    def __init__(self, store=None):
        """
        Initializes the Workspace with a MemoryStore.
        """
        if store is None:
            store = MemoryStore()
        super().__init__(store=store)

    def stats(self, query=[]):
        """
        Generates statistics on the STIX objects within the store.

        This function will count the number of occurrences for each type of STIX object.

        Args:
            query (Optional[List], optional): A list of filters representing the query. Defaults to None.

        Returns:
            Dict[str, int]: A dictionary with STIX object types as keys and their counts as values.
        """
        stats = dict()
        for obj in self.query(query):
            stats[obj.type] = stats.get(obj.type, 0) + 1
        return stats

    def create(self, cls, **kwargs):
        """
        Overrides the `create` method of the `Environment` class to add new STIX objects
        to the store immediately upon creation.

        Args:
            cls: the python-stix2 class of the object to be created (eg. Indicator)
            **kwargs: The property/value pairs of the STIX object to be created

        Returns:
            stix2.base._STIXBase: The newly created STIX object.
        """
        obj = super().create(cls, **kwargs)
        self.add(obj)
        return obj

    def query(self, query=[], last_version_only=True):
        """
        Executes a query against the store to retrieve STIX objects.

        Args:
            query (Optional[List], optional): A list of filters representing the query. Defaults to None.
            last_version_only (bool, optional): When True, only the most recent version of each object is
                                                returned. Defaults to True.

        Returns:
            List[stix2.base._STIXBase]: A list of STIX objects that match the query criteria. When `last_version_only`
                                        is True, the list will contain only the most recent version of each object.
        """
        all_objects = super().query(query)
        if not last_version_only or not all_objects:
            return all_objects

        def get_last_version_objects():
            """
            Yields the last version objects, sorted in reverse order of addition.

            Yields:
                stix2.base._STIXBase: Each STIX object in the store.
            """
            seen = set()
            for obj in reversed(all_objects):
                if obj.id not in seen:
                    seen.add(obj.id)
                    yield obj

        return list(get_last_version_objects())

    def remove(self, object_id):
        """
        Removes an object, along with all its versions, from the store.

        Args:
            object_id (str): The ID of the STIX object to be removed.

        Raises:
            ValueError: If no object with the provided ID could be found.
        """
        try:
            for source in self.source.data_sources:
                del source._data[object_id]
        except KeyError:
            raise ValueError(f"No object found with ID: {object_id}")

    def parse(self, data, allow_custom=False):
        """
        Convert a string, dict or file-like object into a STIX object(s) and loads the object(s) into the Workspace's.

        Args:
            data (str, dict, file-like object): The STIX 2 content to be parsed.
            allow_custom (bool): Whether to allow custom properties as well unknown
                custom objects. Note that unknown custom objects cannot be parsed
                into STIX objects, and will be returned as is. Default: False.
        """
        parsed_data = utils.common.parse(data, allow_custom)
        if isinstance(parsed_data, Bundle):
            self.add(parsed_data.objects)
        else:
            self.add(parsed_data)
