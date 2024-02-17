import requests
from ..archivesspace import ArchivesSpace


class Accession(ArchivesSpace):
    """Class for working with Accessions in ArchivesSpace."""

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        super().__init__(url, user, password)

    # @todo: "Implement this method."
    def create(self):
        """Creates a new Accession.

        Schema found here: https://github.com/archivesspace/archivesspace/blob/master/common/schemas/accession.rb

        """
        model = {
            "jsonmodel_type": "accession",
        }

    def get(self, repo_id, accession_id):
        """Get a specific accession.

        Args:
            repo_id (int): The id of the repository you are querying.
            accession_id (int): The id of the accession you are requesting.

        Returns:
            dict: A dict representing your resource.

        Examples:
            >>> Accession().get(2, 1)
            {'error': 'Resource not found'}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/accessions/{accession_id}",
            headers=self.headers,
        )
        return r.json()

    def get_list_of_ids(self, repo_id):
        """Get a list of ids for Accessions in a Repository.

        Args:
            repo_id (int): The id of the repository you are querying.

        Returns:
            list: A list of ints that represent each Accession in the repository.

        Examples:
            >>> Accession().get_list_of_ids(2)
            [1, 2]

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/accessions?all_ids=true",
            headers=self.headers,
        )
        return r.json()

    def get_accessions_on_page(self, repo_id, page=1, page_size=10):
        """Get Accessions on a page.

        Args:
            repo_id (int): The id of the repository you are querying.
            page (int): The page of accessions you want to get.
            page_size (int): The size of the page you want returned.

        Returns:
            dict: A dict with information about the results plus all matching Accessions.

        Examples:
            >>> Accession().get_accessions_on_page(2, 2, 10)
            {'first_page': 1, 'last_page': 1, 'this_page': 2, 'total': 2, 'results': []}

        """
        r = requests.get(
            url=f"{self.base_url}/repositories/{repo_id}/accessions?page={page}&page_size={page_size}",
            headers=self.headers,
        )
        return r.json()