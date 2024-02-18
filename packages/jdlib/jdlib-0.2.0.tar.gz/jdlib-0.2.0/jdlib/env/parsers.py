class Parser:
    def parse(self, value):
        raise NotImplementedError(f'{self.__class__.__name__} must implement `.parse(self, value)`')
    

class DatabaseParser(Parser):
    ENGINE_MAP = {
        'postgres': 'django.db.backends.postgresql',
    }

    def parse(self, value):
        engine, uri = value.split('://', 1)
        credentials, db = uri.split('@', 1)
        user, password = credentials.split(':', 1)
        addr, name = db.split('/', 1)
        host, port = addr.split(':', 1)
        return {
            'default': {
                'ENGINE': DatabaseParser.ENGINE_MAP[engine],
                'HOST': host,
                'PORT': port,
                'NAME': name,
                'USER': user,
                'PASSWORD': password,
            }
        }
