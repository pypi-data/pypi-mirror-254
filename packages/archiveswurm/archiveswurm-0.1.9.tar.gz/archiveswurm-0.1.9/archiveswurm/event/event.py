import requests
from ..archivesspace import ArchivesSpace


class Event(ArchivesSpace):
    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def get(self, repo_id, event_id):
        """Get an event object by id.

        Args:
            repo_id (int): The id of the repository you are querying.
            event_id (int): The id of the event object you want.

        Returns:
            dict: The event object as a dict.

        Examples:
            >>> Event().get(2, 7674)
            {'lock_version': 0, 'suppressed': False, 'timestamp': '2021-03-18T16:47:57Z', 'created_by': 'laura',
            'last_modified_by': 'laura', 'create_time': '2021-03-18T16:47:57Z', 'system_mtime': '2022-02-23T18:55:47Z',
            'user_mtime': '2021-03-18T16:47:57Z', 'event_type': 'custody_transfer', 'jsonmodel_type': 'event',
            'external_ids': [], 'external_documents': [], 'linked_agents': [{'role': 'transmitter', 'ref':
            '/agents/corporate_entities/2'}, {'role': 'recipient', 'ref': '/agents/corporate_entities/1'}],
            'linked_records': [{'role': 'transfer', 'ref': '/repositories/2/resources/4728'}], 'uri':
            '/repositories/2/events/7746', 'repository': {'ref': '/repositories/2'}}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/events/{event_id}",
            headers=self.headers,
        )
        return r.json()

    def get_list_of_events(self, repo_id):
        """Get a list of event objects.

        Args:
            repo_id (int): The id of the repository you are querying.

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/events?all_ids=true",
            headers=self.headers,
        )
        return r.json()

    def get_page_of_events(self, repo_id, page):
        """Get a list of event objects.

        Args:
            repo_id (int): The id of the repository you are querying.

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/events?page={page}",
            headers=self.headers,
        )
        return r.json()