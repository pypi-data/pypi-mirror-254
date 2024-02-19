from jdlib.cli.commands import BaseCommand
from jdlib.env import Env


class Command(BaseCommand):
    def handle(self, **options):
        for name, value in Env.environment().items():
            print(f'{name}: {value}')
