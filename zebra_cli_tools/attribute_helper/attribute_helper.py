from .attruibute import Attribute

class AttributeHelper:

    def __init__(self, cli):
        self._attributes_config = cli.get('attributes', [])
        self.attributes = {}

    def __iter__(self):
        for attribute in self.attributes.values():
            yield attribute
    
    def __getitem__(self, attribute_name):
        return self.attributes.get(attribute_name)

    def create_attributes(self):
        for attribute_data in self._attributes_config:
            attribute = Attribute(attribute_data)
            self.attributes[attribute.name] = attribute
            