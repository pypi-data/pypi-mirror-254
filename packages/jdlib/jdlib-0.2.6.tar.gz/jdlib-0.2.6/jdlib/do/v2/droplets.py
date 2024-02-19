import json

from jdlib.do.v2.client import DOClient


class Droplet:
    model_name = 'droplet'

    model_name_plural = 'droplets'

    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

        # we do not need to display all region sizes
        if hasattr(self, 'region'):
            del getattr(self, 'region')['sizes']

    def __repr__(self):
        attrs = [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr))
            and not attr.startswith('__')
            and not attr.startswith('model_name')
        ]
        return json.dumps({
            attr: getattr(self, attr)
            for attr in attrs
        })


class DropletClient(DOClient):
    path = 'droplets'

    model = Droplet

    def list(self):
        data = self.get()
        return self.deserialize(data)
    
    def create(self, name, size, image, region='nyc', **kwargs):
        names = [droplet.name for droplet in self.list()]
        if name in names:
            raise Exception(f'Droplet with name {name} already exists.')
        
        data = self.post(json={'name': name, 'size': size, 'image': image, 'region': region, **kwargs})
        return self.deserialize(data)
