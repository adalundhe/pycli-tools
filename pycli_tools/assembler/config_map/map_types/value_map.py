class ValueMap:

    def __init__(self, map_name=None, map_type=None):
        self.arg_name = None
        self.value = None
        self._types = {
            'string': str,
            'integer': int,
            'boolean': bool,
            'float': float,
            'dict': dict,
            'list': list
        }

    def update(self, map_value):
        if type(map_value) == dict:
            if self.value is None:
                self.value = {}
                
            self.value.update(map_value)
        else:
            self.value = map_value

    def map(self, argument) -> None:
        value = argument.value
        
        if argument.arg_type == 'value':
            if argument.value:
                converter = self._types.get(argument.data_type, str)
                value = converter(value)
                
        self.value = argument.value
            