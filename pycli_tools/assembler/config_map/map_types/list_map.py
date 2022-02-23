from .value_map import ValueMap

class ListMap(ValueMap):

    def __init__(self, map_name=None, map_type=None):
        super(ListMap, self).__init__(map_name=map_name, map_type=map_type)
        self.arg_name = None
        self.value = []

    def update(self, map_value):
        self.value.append(map_value)

    def map(self, argument) -> None:
        value = argument.value

        if argument.arg_type == 'value':
            if argument.value:
                converter = self._types.get(argument.data_type, str)
                value = converter(value)
        
        self.value.append(value)