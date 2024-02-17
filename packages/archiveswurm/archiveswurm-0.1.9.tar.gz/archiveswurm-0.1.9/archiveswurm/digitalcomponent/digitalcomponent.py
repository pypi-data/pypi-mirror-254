import json
import requests
from ..archivesspace import ArchivesSpace


class DigitalObjectComponent(ArchivesSpace):
    """Class for working with Digital Object Components in ArchivesSpace."""
    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def get_list_of_ids(self, repo_id):
        """Get a list of ids for Digital Object Components in a Repository.

        Args:
            repo_id (int): The id of the repository you are querying.

        Returns:
            list: A list of ints that represent each Digital Object Component in the repository.

        Examples:
            >>> DigitalObjectComponent().get_list_of_ids(2)
            []

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/digital_object_components?all_ids=true",
            headers=self.headers,
        )
        return r.json()

    def get_by_page(self, repo_id, page=1, page_size=10):
        """Get Digital Object Components on a page.

        Args:
            repo_id (int): The id of the repository you are querying.
            page (int): The page of digital object components you want to get.
            page_size (int): The size of the page you want returned.

        Returns:
            dict: A dict with information about the results plus all matching Digital Object Components.

        Examples:
            >>> DigitalObjectComponent().get_by_page(2, 2, 10)
            {'first_page': 1, 'last_page': 1, 'this_page': 1, 'total': 0, 'results': []}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/digital_object_components?page={page}&page_size={page_size}",
            headers=self.headers,
        )
        return r.json()

    def get(self, repo_id, digital_object_component_id):
        """Get a Digital Object Component by id.

        Args:
            repo_id (int): The id of the repository you are querying.
            digital_object_component_id (int): The id of the digital object component you want.

        Returns:
            dict: The digital object component as a dict.

        Examples:
            >>> DigitalObjectComponent().get(2, 1)
            {'lock_version': 0, 'position': 0, 'publish': False, 'display_string': 'Chronicling COVID-19: AIP', 'label': 'Chronicling COVID-19: AIP', 'created_by': 'mark', 'last_modified_by': 'mark', 'create_time': '2023-04-16T14:43:48Z', 'system_mtime': '2023-04-16T14:43:48Z', 'user_mtime': '2023-04-16T14:43:48Z', 'suppressed': False, 'is_slug_auto': False, 'jsonmodel_type': 'digital_object_component', 'external_ids': [], 'subjects': [], 'linked_events': [], 'extents': [], 'lang_materials': [], 'dates': [], 'external_documents': [], 'rights_statements': [], 'linked_agents': [], 'file_versions': [{'lock_version': 0, 'file_uri': 'https://n2t.net/ark:/87290/v8cr5rh5', 'publish': False, 'created_by': 'mark', 'last_modified_by': 'mark', 'create_time': '2023-04-16T14:43:48Z', 'system_mtime': '2023-04-16T14:43:48Z', 'user_mtime': '2023-04-16T14:43:48Z', 'xlink_actuate_attribute': 'onRequest', 'xlink_show_attribute': 'new', 'jsonmodel_type': 'file_version', 'is_representative': False, 'identifier': '11'}], 'notes': [], 'uri': '/repositories/2/digital_object_components/1', 'repository': {'ref': '/repositories/2'}, 'digital_object': {'ref': '/repositories/2/digital_objects/11'}, 'has_unpublished_ancestor': True}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/digital_object_components/{digital_object_component_id}",
            headers=self.headers,
        )
        return r.json()

    def create(self, digital_object, title, repo_id, position=0, specified_properties={}, file_versions=[], publish=False, parent=None):
        """Create a Digital Object Component.

        Args:
            digital_object (int): The id of the parent Digital Object.
            title (str): The title of the Digital Object Component.
            repo_id (int): The id of the repository you are querying and the id of the repository to which the digital object belongs.
            position (int): The position of the Digital Object Component in the parent Digital Object. Defaults to 0.
            specified_properties (dict): A dict of properties to add to the Digital Object Component.
            file_versions (list): A list of file versions to add to the Digital Object Component.
            publish (bool): Whether or not to publish the Digital Object Component. Defaults to False.
            parent (int): The id of the parent Digital Object Component if it belongs to one. Defaults to None.

        Returns:
            dict: The Digital Object Component as a dict.

        Examples:
            >>> DigitalObjectComponent().create(11, "Test Digital Object Component", 2)
            {'status': 'Created', 'id': 3, 'lock_version': 0, 'stale': True, 'uri': '/repositories/2/digital_object_components/3', 'warnings': []}

        """
        initial_data = {
            "jsonmodel_type": "digital_object_component",
            "is_slug_auto": False,
            "publish": publish,
            "position": position,
            "label": title,
            "file_versions": file_versions,
            "digital_object": {
                "ref": f'/repositories/{repo_id}/digital_objects/{digital_object}'
            },
        }
        for key, value in specified_properties.items():
            initial_data[key] = value
        if parent:
            initial_data["parent"] = {
                "ref": f"/repositories/{repo_id}/digital_object_components/{parent}"
            }
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/digital_object_components",
            headers=self.headers,
            data=json.dumps(initial_data),
        )
        return r.json()
