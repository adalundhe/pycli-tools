from .value_map import ValueMap


class DictMap(ValueMap):

    def __init__(self, map_name=None, map_type=None):
        super(DictMap, self).__init__(map_name=map_name, map_type=map_type)
        self.arg_name = None
        self.value = {}

    def update(self, map_value):
        self.value.update(map_value)

    def map(self, argument) -> None:
        value = argument.value

        if argument.value:            
            if argument.arg_type == "file":                
                if argument.data_type == "dict" and argument.data_key is None:
                    self.value.update(argument.value)
                else:
                    self.value[argument.data_key] = value
            else:
                converter = self._types.get(argument.data_type, str)
                value = converter(value)
                self.value[argument.data_key] = value
