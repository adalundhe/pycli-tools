import configargparse
import sys
import os
import json
from .bundler import Bundler


class Argument:

    def __init__(self, argument):
        self.value = None
        self.parser = configargparse.ArgumentParser(add_env_var_help=False)
        self._args = None
        self.map_name = argument.get('map_name')
        self.data_type = argument.get('data_type')
        self.data_key = argument.get('data_key')
        self._arg_name = argument.get('arg_name')
        self._var_name = argument.get('var_name')
        self._envar_default = argument.get('envar_default')
        self._default = argument.get('default')
        self._default_filename = argument.get('default_filename')
        self._required = argument.get('required', False)
        self._help = argument.get('help')
        self.arg_type = argument.get('arg_type', 'value')
        self._class_type = argument.get('class_type')
        self.original_arg = None


    def _set_defaults(self):
        if self._default == "OS_CWD":
            self._default = '{current_directory}/{default_filename}'.format(
                current_directory=os.getcwd(),
                default_filename=self._default_filename
            )

            if os.path.isfile(self._default) is False:
                self._default = None

        if self._default is None and self._envar_default:
            self._default = os.getenv(self._envar_default, self._default)

    def add_argument(self):
        if self.arg_type == 'flag':
            self.parser.add_argument(self._arg_name, action='store_true', help=self._help)
        
        else:
            self._set_defaults()
            self.parser.add_argument(
                self._arg_name, 
                default=self._default, 
                required=self._required,
                help=self._help
            )

        try:
            arg_position = sys.argv.index(self._arg_name)
            self._args = sys.argv[arg_position:arg_position+2]
            sys.argv = sys.argv[0:arg_position] + sys.argv[arg_position+2:]
        except ValueError:
            self._args = []

    def parse(self, arg=None):
        parsed_arg = vars(
            self.parser.parse_args(args=self._args)
        ).get(self._var_name)
        
        if self.arg_type == 'file' and parsed_arg:
            try:
                with open(parsed_arg) as arg_file:
                    parsed_arg =  json.load(arg_file)
            except Exception:
                parsed_arg = {}

        elif self.arg_type == 'python-file' and parsed_arg:
            try:
                self.original_arg = parsed_arg
                bundler = Bundler(options={
                    'class_type': self._class_type,
                    'package_name': parsed_arg
                })

                parsed_arg = bundler.discover()
                
            except Exception as err:
                print(err)
                parsed_arg = None

        self.value = parsed_arg

    def add_config_to_args(self):
        for config_key, config_value in self.value.items():
            sys.argv.extend([config_key, config_value])