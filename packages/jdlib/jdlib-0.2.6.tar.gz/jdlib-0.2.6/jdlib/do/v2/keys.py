import json

from jdlib.do.v2.client import DOClient


class SSHKey:
    model_name = 'ssh_key'

    model_name_plural = 'ssh_keys'

    def __init__(self, id, fingerprint, public_key, name):
        self.id = id
        self.fingerprint = fingerprint
        self.public_key = public_key
        self.name = name

    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'fingerprint': self.fingerprint,
            'public_key': self.public_key,
            'name': self.name
        })


class SSHKeyClient(DOClient):
    path = 'account/keys'

    model = SSHKey

    def list(self):
        data = self.get()
        return self.deserialize(data)

    def create(self, name: str, public_key: str):
        data = self.post(json={'name': name, 'public_key': public_key})
        return self.deserialize(data)
        
    def retrieve(self, model_id):
        data = self.get(model_id=model_id)
        return self.deserialize(data)
    
    def update(self, model_id, name):
        data = self.put(model_id=model_id, json={'name': name})
        return self.deserialize(data)
    
    def destroy(self, model_id):
        self.delete(model_id=model_id)
        return f'{model_id} deleted successfully.'