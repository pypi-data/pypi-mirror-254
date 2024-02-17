import requests
import json
from ..archivesspace import ArchivesSpace
from ..models import DateModel, Extent


class Resource(ArchivesSpace):
    """Class for working with Resources in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def create(
        self,
        repo_id,
        title,
        manuscript_id,
        extents=[],
        dates=[],
        publish=False,
        level="collection",
        language_of_materials=["eng"],
    ):
        """Create a resource / finding aid.

        @todo: Throws warning because we have no language currently

        Args:
            repo_id (int): The id for the repository.
            title (str): The title of your resource / finding aid.
            manuscript_id (str): The id for your finding aid.
            extents (list): A list of Extents describing your resource.
            dates (list): A list of DateModels describing your resource.
            publish (bool): Should the resource be published to the PUI?
            level (str): The type of resource it should be (collection, item, etc.)

        Returns:
            dict: Metadata and messaging stating whether your resource was created successfully or failed.

        Examples:
            >>> dates = [DateModel().create(date_type="single", label="creation", begin="2002-03-14")]
            >>> extents = [Extent().create(number="35", type_of_unit="cassettes", portion="whole")]
            >>> Resource().create(2, "Test finding aid", "MS.9999999", extents, dates, publish=True)
            {'status': 'Created', 'id': 20, 'lock_version': 0, 'stale': None, 'uri': '/repositories/2/resources/20',
            'warnings': {'language': ['Property was missing']}}

        """
        initial = {
            "jsonmodel_type": "resource",
            "external_ids": [],
            "subjects": [],
            "linked_events": [],
            "extents": extents,
            "dates": dates,
            "external_documents": [],
            "rights_statements": [],
            "linked_agents": [],
            "is_slug_auto": True,
            "restrictions": False,
            "revision_statements": [],
            "instances": [],
            "deaccessions": [],
            "related_accessions": [],
            "classifications": [],
            "notes": [],
            "title": title,
            "id_0": manuscript_id,
            "level": level,
            "finding_aid_date": "",
            "finding_aid_series_statement": "",
            "finding_aid_language": "und",
            "finding_aid_script": "Zyyy",
            "finding_aid_note": "",
            "ead_location": "",
            "publish": publish,
            "lang_materials": LanguageOfMaterials().add(language_of_materials),
        }
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/resources",
            headers=self.headers,
            data=json.dumps(initial),
        )
        return r.json()

    def get_list_of_ids(self, repo_id):
        """Get a list of ids for Resources in a Repository.

        Args:
            repo_id (int): The id of the repository you are querying.

        Returns:
            list: A list of ints that represent each Resource in the repository.

        Examples:
            >>> Resource().get_list_of_ids(2)
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/resources?all_ids=true",
            headers=self.headers,
        )
        return r.json()

    def get_resources_by_page(self, repo_id, page=1, page_size=10):
        """Get Resources on a page.

        Args:
            repo_id (int): The id of the repository you are querying.
            page (int): The page of resources you want to get.
            page_size (int): The size of the page you want returned.

        Returns:
            dict: A dict with information about the results plus all matching Resources.

        Examples:
            >>> Resource().get_resources_by_page(2, 2, 10)
            {'first_page': 1, 'last_page': 1, 'this_page': 2, 'total': 2, 'results': []}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/resources?page={page}&page_size={page_size}",
            headers=self.headers,
        )
        return r.json()

    def get(self, repo_id, resource_id):
        """Get a specific resource.

        Args:
            repo_id (int): The id of the repository you are querying.
            resource_id (int): The id of the resource you are requesting.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Resource().get(2, 18)
            {'error': 'Resource not found'}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/resources/{resource_id}",
            headers=self.headers,
        )
        return r.json()

    def get_ark_name(self, repo_id, resource_id):
        """Get ark name.

        Args:
            repo_id (int): The id of the repository you are querying.
            resource_id (int): The id of the resource you are requesting.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Resource().get_ark_name(2, 18)
            {'error': 'Resource not found'}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/resources/{resource_id}/ark_name",
            headers=self.headers,
        )
        return r.json()

    def link_digital_object(
        self, repo_id, resource_id, digital_object_id, is_representative=False
    ):
        """Link a digital object to a resource.

        Args:
            repo_id (int): The id of your repository.
            resource_id (int): The id of your resource.
            digital_object_id (int): The id of your digital object.
            is_representative (bool): Whether your digital object should be representative of the resource.

        Returns:
            dict: Success or error message with appropriate metadata.

        Examples:
            >>> Resource().link_digital_object(2, 18, 2)
            {'status': 'Updated', 'id': 18, 'lock_version': 1, 'stale': None, 'uri': '/repositories/2/resources/18',
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
        existing_collection = self.get(repo_id, resource_id)
        existing_collection["instances"].append(new_instance)
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/resources/{resource_id}",
            headers=self.headers,
            data=json.dumps(existing_collection),
        )
        return r.json()

    def save(self, repo_id, resource_id):
        """Update a resource without changing any data.

        Args:
            repo_id (int): The id of your repository.
            resource_id (int): The id of your resource.

        Returns:
            dict: Success or error message with appropriate metadata.

        Examples:
            >>> Resource().save(2, 18)
            {'status': 'Updated', 'id': 18, 'lock_version': 1, 'stale': None, 'uri': '/repositories/2/resources/18',
            'warnings': []}

        """
        existing_resource = self.get(repo_id, resource_id)
        r = requests.post(
            url=f"{self.base_url}/repositories/{repo_id}/resources/{resource_id}",
            headers=self.headers,
            data=json.dumps(existing_resource),
        )
        return r.json()
