from argparse import ArgumentParser

from jdlib.cli.commands import APICommand
from jdlib.do.v2.keys import SSHKeyClient


class Command(APICommand):
    client_class = SSHKeyClient

    def add_create_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('--name', action='store', required=True)
        parser.add_argument('--public_key', action='store', required=True)

    def add_get_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('model_id')

    def add_update_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('model_id')
        parser.add_argument('--name', action='store', required=True)

    def add_delete_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('model_id')
