from .map_types import (
    ValueMap,
    ListMap,
    DictMap
)


class ConfigMap:

    def __init__(self, map_name=None, map_type=None):
        self.map_name = map_name
        self.map_type = map_type

        self.maps = {
            'value': ValueMap,
            'list': ListMap,
            'dict': DictMap
        }

        self._config_map = self.maps.get(self.map_type, ValueMap)(
            map_name=self.map_name,
            map_type=self.map_type
        )

        self.argument = None

    def copy(self):
        new_map = self.maps.get(self.map_type, ValueMap)(
            map_name=self.map_name,
            map_type=self.map_type
        )
        new_map.update(self._config_map.value)
        return new_map

    def update(self, map_value):
        self._config_map.update(map_value)

    def map(self, argument) -> None:
        self.argument = argument
        self._config_map.map(argument)

    def get_value(self):
        return self._config_map.value
