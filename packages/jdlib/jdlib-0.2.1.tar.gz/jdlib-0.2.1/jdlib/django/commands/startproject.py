from pathlib import Path

from jdlib import BASE_DIR, __version__
from jdlib.cli.commands import TemplateCommand
from jdlib.django import SECRET_KEY_INSECURE_PREFIX, get_random_secret_key


class Command(TemplateCommand):
    def add_arguments(self, parser):
        parser.add_argument('--plugins', action='store', type=str, nargs='*')
        super().add_arguments(parser)

    def get_plugin_dirs(self, plugins: list[str]) -> list[Path]:
        return [
            BASE_DIR / 'django' / 'conf' / 'plugins' / plugin
            for plugin in plugins
        ]

    def process_plugin_requirements(self, plugin_dir):
        '''
        Add plugin requirements to project requirements
        '''
        requirements = []
        
        with open(self.target_dir / 'requirements.txt', 'r') as f:
            requirements.extend(f.readlines())
        with open(plugin_dir / 'requirements.txt', 'r') as f:
            requirements.extend(f.readlines())

        with open(self.target_dir / 'requirements.txt', 'w') as f:
            f.writelines(sorted(requirements, key=lambda s: s.lower()))

    def process_plugin_settings(self, plugin_dir):
        '''
        Merge plugin settings with project settings
        '''
        project_settings = self.target_dir / self.variable_map['project_name'] / 'settings.py'

        with open(project_settings, 'r') as f:
            settings = f.readlines()
        with open(plugin_dir / 'settings.py-tpl', 'r') as f:
            plugin_settings = f.readlines()

        pointer = 0
        for index, line in enumerate(settings):
            if line.startswith('WSGI_APPLICATION'):
                pointer = index + 2
                break
        for index, line in enumerate(plugin_settings):
            settings.insert(pointer + index, line)
        settings.insert(pointer + len(plugin_settings), '\n')

        with open(project_settings, 'w') as f:
            f.writelines(settings)
        
    def handle(self, **options):
        options['template_dir'] = BASE_DIR / 'django' / 'conf' / 'project_template'
        options['target_dir'] = Path.cwd()
        options['variable_map'] = {
            'docs_version': '5.0',
            'jdlib_version': __version__,
            'project_name': options['name'],
            'secret_key': SECRET_KEY_INSECURE_PREFIX + get_random_secret_key(),
        }

        # process list of plugins before generating
        # project in case a plugin does not exist
        plugin_dirs = self.get_plugin_dirs(options['plugins'])
        for plugin_dir in plugin_dirs:
            if not plugin_dir.is_dir():
                raise Exception(f'Plugin {plugin_dir.stem} not found.')

        super().handle(**options)

        # apply plugins to newly generated project
        for plugin_dir in plugin_dirs:
            self.process_plugin_requirements(plugin_dir)
            self.process_plugin_settings(plugin_dir)
