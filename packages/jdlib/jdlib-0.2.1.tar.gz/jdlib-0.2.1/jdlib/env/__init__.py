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


class Env:
    def __init__(self, env_file='.env', recurse=True, load_environ=True):
        self.env_file = env_file
        self.environ = os.environ if load_environ else {}
        self.parsers = {
            'DATABASE_URL': parsers.DatabaseParser(),
        }
        self.load_env(recurse)

    def __call__(self, name, default=None):
        value = autocast(self.environ.get(name, default))
        if name in self.parsers:
            return self.parsers[name].parse(value)
        return value

    def load_env(self, recurse=True):
        env_path = self.find_env_file(recurse)
        if env_path is not None:
            self.parse_env(env_path)

    def parse_env(self, env_path):
        with open(env_path, 'r') as f:
            for line in f.read().splitlines():
                if line.strip().startswith('#'):
                    continue
                name, value = line.split('=', 1)
                self.environ[name] = value

    def find_env_file(self, recurse=True):
        paths = [Path.cwd() / self.env_file] + [path / self.env_file for path in Path.cwd().parents]
        if paths[0].exists() and recurse is False:
            return paths[0]
        for path in paths:
            if path.exists():
                return path
        return None
    
    @classmethod
    def get_env(cls, name, default=None):
        return autocast(os.environ.get(name, default))
