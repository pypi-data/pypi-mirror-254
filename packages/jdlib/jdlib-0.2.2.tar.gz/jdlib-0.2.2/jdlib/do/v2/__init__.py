from jdlib.api.client import client as BaseClient


class Client(BaseClient):
    def __init__(self):
        super().__init__(self, 'https://api.digitalocean.com/v2/')
