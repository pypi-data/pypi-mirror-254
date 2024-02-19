import requests
from requests import Response


class BaseClient:
    host = None

    def __init__(self, **params):
        self.params = params
        self.session = requests.Session()

    def get(self, path: str, parse_response=True, **params):
        return self.request('GET', path, parse_response, **params)
    
    def post(self, path: str, parse_response=True, **params):
        return self.request('POST', path, parse_response, **params)
    
    def put(self, path: str, parse_response=True, **params):
        return self.request('PUT', path, parse_response, **params)
    
    def patch(self, path: str, parse_response=True, **params):
        return self.request('PATCH', path, parse_response, **params)
    
    def delete(self, path: str, parse_response=True, **params):
        return self.request('DELETE', path, parse_response, **params)

    def get_host(self) -> str:
        if self.host is None:
            raise AttributeError(f'{self.__class__.__name__} must define .host or override .get_host()')
        return self.host
    
    def get_url(self, path: str):
        return f"{self.get_host().rstrip('/')}/{path.lstrip('/')}"
    
    def request(self, method: str, path: str, parse_response=True, **params):
        response = self.session.request(method, self.get_url(path), **{**self.params, **params})
        if parse_response:
            return self.get_response_data(response)
        return response

    def get_response_data(self, response: Response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise e
        
        if not response.content:
            return None
        if 'application/json' in response.headers['content-type']:
            return response.json()
        return response.text
    

class APIClient(BaseClient):
    path = None

    def get_path(self) -> str:
        if self.path is None:
            raise AttributeError(f'{self.__class__.__name__} must define .path or override .get_path()')
        return self.path
    
    def get_url(self, **params):
        model_id = params.pop('model_id', None)
        url = f"{self.get_host().rstrip('/')}/{self.get_path().lstrip('/')}"
        if model_id is not None:
            return f"{url.rstrip('/')}/{model_id.lstrip('/')}"
        return url
    
    def get(self, parse_response=True, **params):
        return self.request('GET', parse_response, **params)
    
    def post(self, parse_response=True, **params):
        return self.request('POST', parse_response, **params)
    
    def put(self, parse_response=True, **params):
        return self.request('PUT', parse_response, **params)
    
    def patch(self, parse_response=True, **params):
        return self.request('PATCH', parse_response, **params)
    
    def delete(self, parse_response=True, **params):
        return self.request('DELETE', parse_response, **params)
    
    def request(self, method: str, parse_response=True, **params):
        url = self.get_url(**params)
        params.pop('model_id', None)
        response = self.session.request(method, url, **{**self.params, **params})
        if parse_response:
            return self.get_response_data(response)
        return response
