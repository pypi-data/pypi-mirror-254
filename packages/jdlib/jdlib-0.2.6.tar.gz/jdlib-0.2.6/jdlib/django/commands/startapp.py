from pathlib import Path

from jdlib import BASE_DIR
from jdlib.cli.commands import TemplateCommand


class Command(TemplateCommand):
    def handle(self, **options):
        options['template_dir'] = BASE_DIR / 'django' / 'conf' / 'app_template'
        options['target_dir'] = Path.cwd()
        options['variable_map'] = {
            'app_name': options['name'],
        }

        if not (options['target_dir'] / 'manage.py').is_file():
            raise Exception('File manage.py not found. Please run in root directory of Django project.')

        for path in options['target_dir'].rglob('*'):
            if path.is_dir() and (path / 'settings.py').is_file():
                options['target_dir'] = path / 'apps'
                options['target_dir'].mkdir(exist_ok=True)
                break

        super().handle(**options)
