from pathlib import Path

from jdlib import BASE_DIR
from jdlib.cli.commands import TemplateCommand
from jdlib.django import SECRET_KEY_INSECURE_PREFIX, get_random_secret_key


class Command(TemplateCommand):
    def handle(self, **options):
        options['template_dir'] = BASE_DIR / 'django' / 'conf' / 'project_template'
        options['target_dir'] = Path.cwd()
        options['variable_map'] = {
            'docs_version': '5.0',
            'jdlib_version': '0.1.6',
            'project_name': options['name'],
            'secret_key': SECRET_KEY_INSECURE_PREFIX + get_random_secret_key(),
        }

        super().handle(**options)
