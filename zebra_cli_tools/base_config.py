from .config_helper import ConfigHelper

class BaseConfig:

    def __init__(self, cli=None, package_version=None):
        self.config_helper = ConfigHelper(
            cli, 
            package_version=package_version
        )

    def update(self, attribute_name, update_value, sub_key=None):
        self.config_helper.update_attribute(
            attribute_name, 
            update_value, 
            sub_key=sub_key
        )


    def copy(self, new_config):
        return self.config_helper.copy_attributes(self, new_config)
