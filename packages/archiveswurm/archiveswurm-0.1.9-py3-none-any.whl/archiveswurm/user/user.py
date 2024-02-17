import json
import requests
from ..archivesspace import ArchivesSpace

class User(ArchivesSpace):
    """Class for working with Users in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def get_list_of_ids(self):
        """Get a list of ids for Users in a Repository.

        Args:
            repo_id (int): The id of the repository you are querying.

        Returns:
            list: A list of ints that represent each User in the repository.

        Examples:
            >>> User().get_list_of_ids()
            []

        """
        r = requests.get(
            url=f"{self.base_url}/users?all_ids=true",
            headers=self.headers,
        )
        return r.json()

    def get_by_page(self, page=1, page_size=10):
        """Get Users on a page.

        Args:
            page (int): The page of users you want to get.
            page_size (int): The size of the page you want returned.

        Returns:
            dict: A dict with information about the results plus all matching Users.

        Examples:
            >>> User().get_by_page(1, 10)
            {'first_page': 1, 'last_page': 1, 'this_page': 1, 'total': 1, 'results': [{'lock_version': 248, 'username': 'admin', 'name': 'Administrator', 'is_system_user': True, 'create_time': '2023-08-15T12:58:19Z', 'system_mtime': '2023-09-07T12:38:33Z', 'user_mtime': '2023-09-07T12:38:33Z', 'jsonmodel_type': 'user', 'groups': [], 'is_admin': True, 'uri': '/users/1', 'agent_record': {'ref': '/agents/people/1'}}]}

        """
        r = requests.get(
            url=f"{self.base_url}/users?page={page}&page_size={page_size}",
            headers=self.headers,
        )
        return r.json()

    def get(self, user_id):
        """Get a User by id.

        Args:
            user_id (int): The id of the user you want.

        Returns:
            dict: A dict representing the User.

        Examples:
            >>> User().get(1)
            {'lock_version': 247, 'username': 'admin', 'name': 'Administrator', 'is_system_user': True, 'create_time': '2023-08-15T12:58:19Z', 'system_mtime': '2023-09-07T12:28:09Z', 'user_mtime': '2023-09-07T12:28:09Z', 'jsonmodel_type': 'user', 'groups': [], 'is_admin': True, 'uri': '/users/1', 'agent_record': {'ref': '/agents/people/1'}, 'permissions': {'/repositories/1': ['update_enumeration_record', 'update_location_record', 'delete_vocabulary_record', 'update_subject_record', 'delete_subject_record', 'update_agent_record', 'delete_agent_record', 'update_vocabulary_record', 'merge_subject_record', 'merge_agent_record', 'update_container_profile_record', 'update_location_profile_record', 'administer_system', 'become_user', 'cancel_importer_job', 'cancel_job', 'create_job', 'create_repository', 'delete_archival_record', 'delete_assessment_record', 'delete_classification_record', 'delete_event_record', 'delete_repository', 'import_records', 'index_system', 'manage_agent_record', 'manage_assessment_attributes', 'manage_container_profile_record', 'manage_container_record', 'manage_enumeration_record', 'manage_location_profile_record', 'manage_rde_templates', 'manage_repository', 'manage_subject_record', 'manage_users', 'manage_vocabulary_record', 'mediate_edits', 'merge_agents_and_subjects', 'merge_archival_record', 'suppress_archival_record', 'transfer_archival_record', 'transfer_repository', 'update_accession_record', 'update_assessment_record', 'update_classification_record', 'update_container_record', 'update_digital_object_record', 'update_event_record', 'update_resource_record', 'view_all_records', 'view_repository', 'view_suppressed'], '_archivesspace': ['administer_system', 'become_user', 'cancel_importer_job', 'cancel_job', 'create_job', 'create_repository', 'delete_archival_record', 'delete_assessment_record', 'delete_classification_record', 'delete_event_record', 'delete_repository', 'import_records', 'index_system', 'manage_agent_record', 'manage_assessment_attributes', 'manage_container_profile_record', 'manage_container_record', 'manage_enumeration_record', 'manage_location_profile_record', 'manage_rde_templates', 'manage_repository', 'manage_subject_record', 'manage_users', 'manage_vocabulary_record', 'mediate_edits', 'merge_agents_and_subjects', 'merge_archival_record', 'suppress_archival_record', 'transfer_archival_record', 'transfer_repository', 'update_accession_record', 'update_assessment_record', 'update_classification_record', 'update_container_record', 'update_digital_object_record', 'update_event_record', 'update_resource_record', 'view_all_records', 'view_repository', 'view_suppressed', 'update_enumeration_record', 'update_location_record', 'delete_vocabulary_record', 'update_subject_record', 'delete_subject_record', 'update_agent_record', 'delete_agent_record', 'update_vocabulary_record', 'merge_subject_record', 'merge_agent_record', 'update_container_profile_record', 'update_location_profile_record']}}

        """
        r = requests.get(
            url=f"{self.base_url}/users/{user_id}",
            headers=self.headers,
        )
        return r.json()

    def create(self, username, name, is_admin=False, is_active_user=True, password="", email=None):
        """Create a User.

        Args:
            username (str): The username of the user you want to create.
            name (str): The full name of the user you want to create.
            is_admin (bool): Whether the user is an admin or not.
            is_active_user (bool): Whether the user is active or not.
            password (str): The password of the user you want to create.
            email (str): The email of the user you want to create.

        Returns:
            dict: A dict representing the User.

        Examples:
            >>> User().create("testuser", "Test User", password="testpassword")
            {'status': 'Created', 'id': 5, 'lock_version': 0, 'stale': None, 'uri': '/users/5', 'warnings': []}
        """
        initial = {
            "jsonmodel_type": "user",
            "username": username,
            "name": name,
            "is_admin": is_admin,
            "is_active_user": is_active_user,
        }
        if email:
            initial["email"] = email
        r = requests.post(
            url=f"{self.base_url}/users?password={password}",
            headers=self.headers,
            data=json.dumps(initial),
        )
        return r.json()
