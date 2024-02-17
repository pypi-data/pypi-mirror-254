import json
import requests
from ..archivesspace import ArchivesSpace
from ..models import DateModel, Extent


class ArchivalObject(ArchivesSpace):
    """Class for working with Archival Objects in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    @staticmethod
    def __process_ancestors(ancestors):
        """Takes in a list of tuples and returns ancestors appropriately."""
        return [{"ref": ancestor[0], "level": ancestor[1]} for ancestor in ancestors]

    def get(self, repo_id, archival_object_id):
        """Get an archival object by id.

        Args:
            repo_id (int): The id of the repository you are querying.
            archival_object_id (int): The id of the archival object you want.

        Returns:
            dict: The archival object as a dict.

        Examples:
            >>> ArchivalObject().get(2, 37371)
            {'lock_version': 0, 'position': 0, 'publish': True, 'ref_id': 'ref13_6ap', 'title':
            '<title ns2:type="simple" render="doublequote">As You Came from the Holy Land,</title>', 'display_string':
            '<title ns2:type="simple" render="doublequote">As You Came from the Holy Land,</title>, undated',
            'restrictions_apply': False, 'created_by': 'admin', 'last_modified_by': 'admin', 'create_time':
            '2019-08-08T20:19:18Z', 'system_mtime': '2020-12-02T17:04:13Z', 'user_mtime': '2019-08-08T20:19:18Z',
            'suppressed': False, 'level': 'file', 'jsonmodel_type': 'archival_object', 'external_ids': [{'external_id':
            '209519', 'source': 'Archivists Toolkit Database::RESOURCE_COMPONENT', 'created_by': 'admin',
            'last_modified_by': 'admin', 'create_time': '2019-08-08T20:19:19Z', 'system_mtime': '2019-08-08T20:19:19Z',
            'user_mtime': '2019-08-08T20:19:19Z', 'jsonmodel_type': 'external_id'}], 'subjects': [], 'linked_events':
            [], 'extents': [], 'dates': [{'lock_version': 0, 'expression': 'undated', 'created_by': 'admin',
            'last_modified_by': 'admin', 'create_time': '2019-08-08T20:19:18Z', 'system_mtime': '2019-08-08T20:19:18Z',
            'user_mtime': '2019-08-08T20:19:18Z', 'date_type': 'single', 'label': 'creation', 'jsonmodel_type': 'date'}
            ], 'external_documents': [], 'rights_statements': [], 'linked_agents': [], 'ancestors': [{'ref':
            '/repositories/2/archival_objects/37369', 'level': 'series'}, {'ref': '/repositories/2/resources/598',
            'level': 'collection'}], 'instances': [{'lock_version': 0, 'created_by': 'admin', 'last_modified_by':
            'admin', 'create_time': '2019-08-08T20:19:19Z', 'system_mtime': '2019-08-08T20:19:19Z', 'user_mtime':
            '2019-08-08T20:19:19Z', 'instance_type': 'mixed_materials', 'jsonmodel_type': 'instance',
            'is_representative': False, 'sub_container': {'lock_version': 0, 'indicator_2': '1', 'created_by': 'admin',
            'last_modified_by': 'admin', 'create_time': '2019-08-08T20:19:19Z', 'system_mtime': '2019-08-08T20:19:19Z',
            'user_mtime': '2019-08-08T20:19:19Z', 'type_2': 'folder', 'jsonmodel_type': 'sub_container',
            'top_container': {'ref': '/repositories/2/top_containers/2961'}}}], 'notes': [{'content': [
            '(Labeled<emph render="doublequote">CP141- 3,</emph>i.e. Collected Poems, Robert Fitzgerald, ed., p. 141)'],
             'jsonmodel_type': 'note_singlepart', 'label': 'General Physical Description note', 'type': 'physdesc',
             'persistent_id': 'abf0fe13a03e23754e1faa666670442d', 'publish': True}], 'uri':
             '/repositories/2/archival_objects/37371', 'repository': {'ref': '/repositories/2'}, 'resource': {'ref':
             '/repositories/2/resources/598'}, 'parent': {'ref': '/repositories/2/archival_objects/37369'},
             'has_unpublished_ancestor': False}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/archival_objects/{archival_object_id}",
            headers=self.headers,
        )
        return r.json()

    def create(
        self,
        repo_id,
        parent_resource,
        title,
        ancestors=[],
        dates=[],
        extents=[],
        parent="",
        level="series",
        restrictions_apply=False,
        publish=True,
    ):
        """Creates a new Archival Object.

        Args:
            repo_id (int): The repository id as an it.
            parent_resource (int): The resource this object belongs to as an int.
            title (str): The title of your archival object.
            ancestors (list): A list of ancestors as tuples with the uri to the resource in index 0 and the level as index 1.
            dates (list): A list of Dates.
            extents (list): A list of Extents.
            level (str): The level of the archival object.
            restrictions_apply (bool): Whether or not restrictions apply.
            publish (bool): Whether or not to publish.

        Examples:
            >>> dates = [DateModel().create(date_type="single", label="creation", begin=finding_aid_data["date"]["begin"],)]
            >>> extents = [Extent().create(number="35", type_of_unit="files", portion="whole")]
            >>> ArchivalObject(url="http://localhost:9089").create(2, 118, title="Chronicling Covid: Creative Works", extents=extents, dates=dates, level="series", ancestors=[("/repositories/2/resources/598", "collection")],)
            {'status': 'Created', 'id': 13118, 'lock_version': 0, 'stale': True, 'uri': '/repositories/2/archival_objects/13118', 'warnings': []}
            >>> extents = [Extent().create(number="1", type_of_unit="files", portion="whole"), Extent().create(number="0.12531", type_of_unit="megabytes", portion="whole")]
            >>> ArchivalObject(url="http://localhost:9089").create(2, 118, title="Market_Square_on_Saturday_-_Sarah_Ryan.jpg", extents=extents, dates=dates, level="file", ancestors=[("/repositories/2/resources/598", "collection"), ('/repositories/2/archival_objects/13119', 'series')], parent="13119")
            {'status': 'Created', 'id': 13121, 'lock_version': 0, 'stale': True, 'uri': '/repositories/2/archival_objects/13121', 'warnings': []}

        """
        initial_object = {
            "jsonmodel_type": "archival_object",
            "resource": {"ref": f"/repositories/{repo_id}/resources/{parent_resource}"},
            "level": level,
            "restrictions_apply": restrictions_apply,
            "title": title,
            "ancestors": self.__process_ancestors(ancestors),
            "dates": dates,
            "extents": extents,
            "publish": publish,
        }
        if parent != "":
            initial_object["parent"] = {
                "ref": f"/repositories/{repo_id}/archival_objects/{parent}"
            }
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/archival_objects",
            headers=self.headers,
            data=json.dumps(initial_object),
        )
        return r.json()

    def delete(self, repo_id, archival_object_id):
        """Deletes an Archival Object.

        Args:
            repo_id (int): The repo id to which the archival object belongs.
            archival_object_id (int): The id of the archival object.

        Examples:
            >>> ArchivalObject(url="http://localhost:9089").delete(2, 13118)
            {'status': 'Deleted', 'id': 13118}

        """
        r = requests.delete(
            url=f"{self.base_url}/repositories/{repo_id}/archival_objects/{archival_object_id}",
            headers=self.headers,
        )
        return r.json()

    def link_digital_object(
        self, repo_id, archival_object_id, digital_object_id, is_representative=False
    ):
        """Link a digital object to an archival_object.

        Args:
            repo_id (int): The id of your repository.
            archival_object_id (int): The id of your archival object.
            digital_object_id (int): The id of your digital object.
            is_representative (bool): Whether your digital object should be representative of the resource.

        Returns:
            dict: Success or error message with appropriate metadata.

        Examples:
            >>> ArchivalObject().link_digital_object(2, 18, 2)
            {'status': 'Updated', 'id': 18, 'lock_version': 1, 'stale': None, 'uri': '/repositories/2/archival_object/18',
            'warnings': []}

        """
        new_instance = {
            "is_representative": is_representative,
            "instance_type": "digital_object",
            "jsonmodel_type": "instance",
            "digital_object": {
                "ref": f"/repositories/2/digital_objects/{digital_object_id}"
            },
        }
        existing_collection = self.get(repo_id, archival_object_id)
        existing_collection["instances"].append(new_instance)
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/archival_objects/{archival_object_id}",
            headers=self.headers,
            data=json.dumps(existing_collection),
        )
        return r.json()