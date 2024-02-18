import importlib
import pkgutil
from argparse import ArgumentParser

from types import ModuleType

import jdlib
from jdlib.cli.commands import BaseCommand


class JDCli():
    def __init__(self):
        self.parser = ArgumentParser()
        self.subparsers = self.parser.add_subparsers(title='modules', dest='module_name')
        self.subparsers.required = True

        self.command_map = {}

        self.process_modules()

    def run(self):
        args = self.parser.parse_args().__dict__
        module_name = args.pop('module_name')
        command_name = args.pop('command_name')
        self.command_map[module_name][command_name].handle(**args)

    def process_modules(self):
        for command_module in self.get_command_modules():
            module_name = command_module.__name__.split('.')[1]
            self.command_map[module_name] = {}

            module_parser = self.subparsers.add_parser(module_name)
            module_subparsers = module_parser.add_subparsers(title='commands', dest='command_name')
            module_subparsers.required = True

            self.process_commands(command_module, module_name, module_subparsers)

    def process_commands(self, command_module: ModuleType, module_name: str, module_subparsers):
        self.command_map[module_name] = self.get_commands(command_module)
        for name, instance in self.command_map[module_name].items():
            command_parser = module_subparsers.add_parser(name)
            instance.add_arguments(command_parser)

    def get_commands(self, command_module: ModuleType) -> dict[str, BaseCommand]:
        return {
            name: self.load_command_class(f'{command_module.__name__}.{name}')
            for _, name, ispkg in pkgutil.iter_modules(command_module.__path__)
            if not ispkg and not name.startswith('_')
        }

    def load_command_class(self, module_name: str):
        module = importlib.import_module(module_name)
        command_class = getattr(module, 'Command')
        return command_class()

    def get_command_modules(self) -> list[ModuleType]:
        command_modules = []
 
        for module in self.get_jdlib_modules():
            name = f'{module.__name__}.commands'
            if not importlib.util.find_spec(name):
                continue

            command_module = importlib.import_module(name)
            if hasattr(command_module, '__path__'):
                command_modules.append(command_module)

        return command_modules

    def get_jdlib_modules(self) -> list[ModuleType]:
        return [
            importlib.import_module(f'jdlib.{module_info.name}')
            for module_info in pkgutil.iter_modules(jdlib.__path__)
            if module_info.ispkg
        ]


def main():
    JDCli().run()
