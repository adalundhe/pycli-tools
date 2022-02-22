from .arguments import Argument
from .assembler import Assembler
from .attribute_helper import AttributeHelper
from zebra_automate_logging import Logger

class ConfigHelper:

    def __init__(self, cli, package_version=None):
        self.cli = cli
        self.package_version = package_version
        self._arguments = []
        self._assembler = Assembler(cli)
        self._attribute_helper = AttributeHelper(cli)  

        logger = Logger()
        logger.setup('info')
        self.session_logger = logger.generate_logger('cli')   

    def __getitem__(self, arg_name):
        value = self._assembler[arg_name]

        if value:
            return value

        attribute = self._attribute_helper[arg_name]
        if attribute:

            if attribute.default:
                return attribute.default
            else:
                return attribute.blank()
            
        return None

    def __setitem__(self, arg_name, value):
        self._assembler[arg_name] = value

    def generate_help_string(self):
        argument_help_strings = []

        for argument in self.cli.get('arguments'):
            
            arg_type = argument.get('data_type')

            if argument.get('arg_type') == "flag":
                arg_type = "flag"

            argument_help_string = "\n\t\t{arg_name} - {arg_type} - {help_string}\n".format(
                arg_name=argument.get('arg_name'),
                arg_type=arg_type,
                help_string=argument.get('help')
            )

            argument_help_strings.append(argument_help_string)

        if self.cli.get('name') and self.package_version:
            return """
            Name: {package_name}
            Version: {package_version}
            Description: {package_description}

            Args:
            {argument_help_strings}""".format(
                package_name=self.cli.get('name'),
                package_version=self.package_version,
                package_description=self.cli.get('description'),
                argument_help_strings=''.join(argument_help_strings)
            )

        else:
            return ''.join(argument_help_strings)

    def copy_attributes(self, from_config, to_config):
        copy = from_config.config_helper._assembler.copy()
        to_config.config_helper._assembler.mapped = copy
        return to_config

    def update_attribute(self, arg_name, update_value, sub_key=None):
        if self._assembler[arg_name]:
            arg_value = self._assembler[arg_name]
            if sub_key:
                arg_value[sub_key] = update_value
            else:
                arg_value = update_value
            
            self._assembler.update(arg_name, arg_value)

    def merge(self, from_key, to_key, sub_key=None):
        self._assembler.merge(from_key, to_key, sub_key=sub_key)
    
    def setup(self):
        if self.cli.get('config_maps'):
            self._assembler.generate_config_maps()

        if self.cli.get('attributes'):
            self._attribute_helper.create_attributes()

        for argument in self.cli.get('arguments'):
            self._arguments.append(
                Argument(argument)
            )

    def set_cli(self):
        for argument in self._arguments:
            argument.add_argument()

    def parse_cli(self):
        for argument in self._arguments:
            argument.parse()
            self._assembler.map_arg(argument)
