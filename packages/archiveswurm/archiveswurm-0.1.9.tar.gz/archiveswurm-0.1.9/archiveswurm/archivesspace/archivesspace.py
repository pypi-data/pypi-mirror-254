import json
import requests

class ArchivesSpace:
    """Base class for all ArchivesSpace Classes with methods built on requests.

    Attributes:
        base_url (str): The base_url of your ArchivesSpace API.
        headers (dict): The HTTP header containing your authentication information.
    """

    def __init__(self, url="http://localhost:9089", user="admin", password="admin"):
        self.base_url = url
        self.headers = {"X-ArchivesSpace-Session": self.__authenticate(user, password)}

    def __authenticate(self, username, password):
        r = requests.post(
            url=f"{self.base_url}/users/{username}/login?password={password}"
        )
        return r.json()["session"]