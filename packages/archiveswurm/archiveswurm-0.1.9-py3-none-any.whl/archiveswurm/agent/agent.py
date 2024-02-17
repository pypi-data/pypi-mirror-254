import requests
from ..archivesspace import ArchivesSpace

class PersonAgent(ArchivesSpace):
    """Class for working with Person Agents in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    def get(self, agent_id):
        """Get a specific agent.

        Args:
            agent_id (int): The id of the person agent you are requesting.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Agent().get(1)
            {'error': 'Resource not found'}

        """
        r = requests.get(
            url=f"{self.base_url}/agents/people/{agent_id}",
            headers=self.headers,
        )
        return r.json()

    def delete(self, agent_id):
        """Delete a specific person agent.

        Args:
            agent_id (int): The id of the person agent you are deleting.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Agent().delete(1)
            {'error': 'Resource not found'}

        """
        r = requests.delete(
            url=f"{self.base_url}/agents/people/{agent_id}",
            headers=self.headers,
        )
        return r.json()

    def list(self):
        """List all person agents.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Agent().list()
            {'error': 'Resource not found'}

        """
        r = requests.get(
            url=f"{self.base_url}/agents/people",
            headers=self.headers,
        )
        return r.json()