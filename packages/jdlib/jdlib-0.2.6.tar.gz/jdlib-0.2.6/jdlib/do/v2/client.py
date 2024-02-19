from jdlib.api.clients import APIClient
from jdlib.env import Env


class DOClient(APIClient):
    host = 'https://api.digitalocean.com/v2/'

    model = None

    def __init__(self, token=None, **params):
        if token is None:
            token = Env.get_env('JDLIB_DO_API_TOKEN')
        headers = params.pop('headers', {})
        headers['Authorization'] = f'Bearer {token}'
        params['headers'] = headers
        super().__init__(**params)

    def get_model(self):
        if self.model is None:
            raise AttributeError(f'{self.__class__.__name__} must define .model or override .get_model()')
        return self.model
    
    def deserialize(self, data):
        if self.model.model_name in data.keys():
            return self.model(**data[self.model.model_name])
        return [self.model(**obj) for obj in data[self.model.model_name_plural]]
