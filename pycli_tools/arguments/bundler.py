

import os
import sys
import importlib
from easy_logger import Logger


class Bundler:

    def __init__(self, options={}):

        self.class_type = options.get('class_type')
        self.package_name = options.get('package_name')

        if self.package_name and len(self.package_name) > 0:
            self.module_name = self.package_name.split('.')[0]
        else:
            self.module_name = 'custom'

        base_dir = options.get(
            'base_dir',
            '{working_dir}'.format(
                working_dir=os.getcwd(),
            )
        )

        self.search_dir = f'{base_dir}'
        if self.package_name:
            self.search_dir = f'{self.search_dir}/{self.package_name}'

        self._module_path = os.path.basename(
            os.path.normpath(base_dir)
        )

        self.discovered = {}

        logger = Logger()
        self.session_logger = logger.generate_logger()

    def __iter__(self):
        for item in self.discovered:
            yield item

    def discover(self) -> str:

        spec = importlib.util.spec_from_file_location(self.module_name, self.search_dir)

        if self.search_dir not in sys.path:
            sys.path.append(self.search_dir)

        module = importlib.util.module_from_spec(spec)

        sys.modules[self.module_name] = module
        spec.loader.exec_module(module)
        self.discovered = {cls.__name__: cls for cls in self.class_type.__subclasses__()}

        return list(self.discovered.values())
