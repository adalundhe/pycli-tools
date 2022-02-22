from .config_map import ConfigMap


class Assembler:

    def __init__(self, cli):
        self.config_maps = cli.get('config_maps', [])
        self.mapped = {}

    def __getitem__(self, map_name) -> object:
        config_map = self.mapped.get(map_name)
        value = None
        if config_map:
            value = config_map.get_value()
        return value

    def __setitem__(self, map_name, value) -> None:
        self.mapped[map_name] = value

    def copy(self) -> dict:
        config_map_copies = {}
        for map_key, config_map in self.mapped.items():
            config_map_copy = ConfigMap(
                map_name=config_map.map_name,
                map_type=config_map.map_type
            )
            config_map_copy._config_map = config_map.copy()
            config_map_copies[map_key] = config_map_copy
        
        return config_map_copies

    def update(self, map_name, map_value) -> None:
        self.mapped.get(map_name).update(map_value)

    def merge(self, from_map_name, to_map_name, sub_key=None) -> None:
        from_map = self.mapped.get(from_map_name).get_value()
        if sub_key:
            if type(from_map) == dict:
                update_value = from_map.get(sub_key)
            elif type(from_map) == list:
                update_value = from_map[sub_key]
            else:
                update_value = None

            if update_value:
                self.mapped.get(to_map_name).update(update_value)
        else:
            self.mapped.get(to_map_name).update(from_map)

    def generate_config_maps(self, config_maps=None) -> None:
        if config_maps is None:
            config_maps = self.config_maps

        for config_map in config_maps:
            map_name = config_map.get('map_name')
            self.mapped[map_name] = ConfigMap(
                map_name=map_name,
                map_type=config_map.get('map_type')
            )

    def map_arg(self, argument) -> None:
        self.mapped.get(argument.map_name).map(argument)
    