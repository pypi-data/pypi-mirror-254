import subprocess
from argparse import ArgumentParser
from pathlib import Path


class BaseCommand:
    def add_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def handle(self, **options):
        raise NotImplementedError(f'{self.__class__.__name__} must implement `.handle(self, **options)`')


class RunCommand(BaseCommand):
    def run_command(self, command):
        try:
            result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise e
        return result.stdout.decode('utf-8')


class TemplateCommand(BaseCommand):
    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('name')

    def get_target_path(self, template_path: Path) -> Path:
        target_path = str(self.target_dir / template_path.relative_to(self.template_dir))
        for var, val in self.variable_map.items():
            target_path = target_path.replace(f'{{{{ {var} }}}}', val)
        return Path(target_path)
    
    def get_path_mappings(self):
        paths = []
        for template_path in self.template_dir.rglob('*'):
            target_path = self.get_target_path(template_path)
            if template_path.is_dir() and target_path.name in ['.git', '__pycache__']:
                continue
            if template_path.is_file() and target_path.name.endswith(('.pyc', '.pyo', '.pyd', '.py.class', '.DS_Store')):
                continue
            paths.append((template_path, target_path))
        return paths

    def write_target_file(self, template_path, target_path):
        if target_path.suffix == '.py-tpl':
            target_path = target_path.with_suffix('.py')
        with open(template_path, 'r') as template_file:
            data = template_file.read()
        for var, val in self.variable_map.items():
            data = data.replace(f'{{{{ {var} }}}}', val)
        with open(target_path, 'w') as target_file:
            target_file.write(data)

    def handle(self, **options):
        self.template_dir = options['template_dir']
        self.target_dir = options['target_dir']
        self.variable_map = options['variable_map']

        paths = self.get_path_mappings()
        
        for template_path, target_path in paths:
            if target_path.exists():
                path_type = 'File' if template_path.is_file() else 'Directory'
                raise Exception(f'{path_type} {target_path.name} already exists.')
            
        for template_path, target_path in paths:
            if template_path.is_dir():
                target_path.mkdir()

            if template_path.is_file():
                self.write_target_file(template_path, target_path)


class APICommand(BaseCommand):
    client_class = None

    def get_client(self):
        if self.client_class is None:
            raise AttributeError(f'{self.__class__.__name__} must define .client_class or override .get_client()')
        return self.client_class()

    def add_arguments(self, parser: ArgumentParser) -> None:
        self.action_subparsers = parser.add_subparsers(title='action', dest='action_name')
        self.action_subparsers.required = True
        self.add_subparsers()

    def add_subparsers(self):
        list_parser = self.action_subparsers.add_parser('list')
        create_parser = self.action_subparsers.add_parser('create')
        get_parser = self.action_subparsers.add_parser('get')
        update_parser = self.action_subparsers.add_parser('update')
        delete_parser = self.action_subparsers.add_parser('delete')

        self.add_list_arguments(list_parser)
        self.add_create_arguments(create_parser)
        self.add_get_arguments(get_parser)
        self.add_update_arguments(update_parser)
        self.add_delete_arguments(delete_parser)

    def add_list_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def add_create_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def add_get_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def add_update_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def add_delete_arguments(self, parser: ArgumentParser) -> None:
        return None
    
    def handle(self, **options):
        client = self.get_client()
        action = options.pop('action_name')
        if action == 'list':
            obj = client.list(**options)
        if action == 'create':
            obj = client.create(**options)
        if action == 'get':
            obj = client.retrieve(**options)
        if action == 'update':
            obj = client.retrieve(**options)
        if action == 'delete':
            obj = client.destroy(**options)
        print(obj)
