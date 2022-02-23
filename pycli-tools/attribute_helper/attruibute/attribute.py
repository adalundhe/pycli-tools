class Attribute:

    def __init__(self, attribute):
        self._types = {
            'boolean': bool,
            'string': str,
            'integer': int,
            'float': float,
            'dict': dict,
            'list': list
        }


        self.name = attribute.get('name')
        self.type = self._types.get(attribute.get('type'))
        self.default = attribute.get('default')

    def convert(self, value):
        return self.type(value)

    def blank(self):
        return self.type()

    def copy(self):
        return self.type(self.default)
