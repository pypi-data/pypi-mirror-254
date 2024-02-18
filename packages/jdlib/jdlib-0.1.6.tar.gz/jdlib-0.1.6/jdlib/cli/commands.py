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
