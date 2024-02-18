from looqbox.class_loader.class_loader import ClassLoader
from looqbox.utils.utils import open_file
from typing import Dict
import os
import json


looqObjects_configuration_file = open_file(os.path.dirname(__file__), "..", "resources", "LooqObjects_path.json")
CLASS_PATHS = json.load(looqObjects_configuration_file)
looqObjects_configuration_file.close()


class LazyLoad:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return ClassLoader(self.function.__name__, CLASS_PATHS[self.function.__name__]).call_class(*args, **kwargs)

    def __instancecheck__(self, instance):
        self_class = ClassLoader(self.function.__name__, CLASS_PATHS[self.function.__name__]).load_class()
        return isinstance(instance, self_class)
