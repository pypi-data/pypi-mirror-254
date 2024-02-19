from argparse import ArgumentParser

from jdlib.cli.commands import APICommand
from jdlib.do.v2.droplets import DropletClient


class Command(APICommand):
    client_class = DropletClient

    def add_create_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('name')
        parser.add_argument('--region', action='store', default='nyc')
        parser.add_argument('--size', action='store', default='s-1vcpu-1gb-35gb-intel')
        parser.add_argument('--image', action='store', default='debian-12-x64')
        parser.add_argument('--key-id', action='store', type=int, required=True)

    def handle(self, **options):
        if 'key_id' in options:
            options['key_id'] = [options['key_id']]
        super().handle(**options)
