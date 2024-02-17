import json
import requests
from ..archivesspace import ArchivesSpace


class Repository(ArchivesSpace):
    """Class for working with repositories in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def get(self, repo_id):
        """Get a repository.

        Args:
            repo_id (int): The id of the repository you are querying.

        Returns:
            dict: Metadata about the repository or an error saying it does not exits

        Examples:
            >>> Repository().get(2)
            {'lock_version': 0, 'repo_code': 'UTK', 'name': 'Betsey B. Creekmore Special Collections and University
            Archives', 'created_by': 'admin', 'last_modified_by': 'admin', 'create_time': '2021-04-29T16:08:29Z',
            'system_mtime': '2021-04-29T16:08:29Z', 'user_mtime': '2021-04-29T16:08:29Z', 'publish': True,
            'oai_is_disabled': False, 'jsonmodel_type': 'repository', 'uri': '/repositories/2', 'display_string':
            'Betsey B. Creekmore Special Collections and University Archives (UTK)', 'agent_representation': {'ref':
            '/agents/corporate_entities/1'}}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}",
            headers=self.headers,
        )
        return r.json()