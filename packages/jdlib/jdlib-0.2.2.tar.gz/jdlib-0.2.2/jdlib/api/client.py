from urllib.parse import urljoin

from requests import Session


class Client(Session):
    def __init__(self, base_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        return super().request(method, urljoin(self.base_url.rstrip('/') + '/', url.lstrip('/')), *args, **kwargs)
