import os
from pathlib import Path

from jdlib.env import parsers


def boolify(s):
    if s.lower() == 'true':
        return True
    if s.lower() == 'false':
        return False
    raise ValueError('Not Boolean')

def noneify(s):
    if s.lower() == 'none' or s.lower() == 'null':
        return None
    raise ValueError('Not None')

def listify(s):
    if ',' not in s:
        raise ValueError('Not List')
    
    elements = s.split(',')
    cast = None
    for fn in [boolify, int, float, noneify, str]:
        try:
            fn(elements[0])
            cast = fn
            break
        except ValueError:
            pass

    try:
        return [cast(element) for element in elements]
    except ValueError:
        raise ValueError('Autocast list must contain same types.')
    
def autocast(value):
    if value is None:
        return None
    
    if type(value) != str:
        return value
    
    for cast in [boolify, int, float, noneify, listify, str]:
        try:
            return cast(value)
        except ValueError:
            pass

    return value


class EnvFile:
    def __init__(self, path: Path, raise_exception=True, load=True):
        self.path = path
        self.config = {}
        if not self.path.exists() and raise_exception:
            raise Exception(f'EnvFile {path} does not exist.')
        if load:
            self.load()

    def load(self):
        if not self.path.exists():
            return
        with open(self.path, 'r') as f:
            for line in f.read().splitlines():
                if line.strip().startswith('#'):
                    continue
                name, value = line.split('=', 1)
                self.config[name] = autocast(value)


class Env:
    def __init__(self, env_filename='.env', recurse=True, load_env=True):
        self.env_filename = env_filename
        self.recurse = recurse
        self.config = {}
        self.parsers = {
            'DATABASE_URL': parsers.DatabaseParser(),
        }
        if load_env:
            self.load_env()
        self.load_env_file()

    def __call__(self, name, default=None):
        value = self.config.get(name, default)
        if value is None:
            raise Exception(f'{name} not found in environment.')
        if name in self.parsers:
            return self.parsers[name].parse(value)
        return value

    def load_env(self):
        '''
        Load global environment variables
        '''
        for name, value in os.environ.items():
            self.config[name] = autocast(value)

    def load_env_file(self) -> None:
        '''
        Load environment variables from file
        '''
        if self.env_filename is None:
            return
        path = self.find_env_file()
        if path is not None:
            env_file = EnvFile(path, raise_exception=False)
            self.config.update(env_file.config)

    def find_env_file(self) -> Path | None:
        '''
        Find file matching `env_filename` by optionally
        searching recursively up from current directory
        '''
        paths = [Path.cwd() / self.env_filename] + [path / self.env_filename for path in Path.cwd().parents]
        if paths[0].exists() and not self.recurse:
            return paths[0]
        for path in paths:
            if path.exists():
                return path
        return None

    @classmethod
    def environment(cls):
        return dict(sorted(os.environ.items(), key=lambda x: x[0].lower()))

    @classmethod
    def get_env(cls, name, default=None):
        '''
        Directly retrieve global environment variable
        '''
        return autocast(os.environ.get(name, default))
