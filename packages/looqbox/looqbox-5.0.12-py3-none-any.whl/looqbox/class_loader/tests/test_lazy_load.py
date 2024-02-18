import unittest
from looqbox.class_loader.lazy_load import CLASS_PATHS
from looqbox.class_loader.class_loader import ClassLoader


class TestLazyLoading(unittest.TestCase):
    def test_class_loading(self):
        for class_name, class_path in CLASS_PATHS.items():
            class_loader = ClassLoader(class_name, class_path)
            try:
                class_loader.load_class()
            except Exception as e:
                self.fail(f"Failed to load class {class_name} from {class_path}: {e}")

    def test_class_loading_with_invalid_path(self):
        for class_name, _ in CLASS_PATHS.items():
            class_loader = ClassLoader(class_name, "correct.horse.battery.staple")
            with self.assertRaises(ImportError):
                class_loader.load_class()

    def test_class_loading_with_nonexistent_class(self):
        for _, class_path in CLASS_PATHS.items():
            class_loader = ClassLoader("SupercallifragilisticAbstractProxyBeamFactory", class_path)
            with self.assertRaises(AttributeError):
                class_loader.load_class()

    def test_class_loading_with_empty_class_name(self):
        for _, class_path in CLASS_PATHS.items():
            class_loader = ClassLoader("", class_path)
            with self.assertRaises(AttributeError):
                class_loader.load_class()

    def test_class_loading_with_empty_path(self):
        for class_name, _ in CLASS_PATHS.items():
            class_loader = ClassLoader(class_name, "")
            with self.assertRaises(ValueError):
               class_loader.load_class()

if __name__ == '__main__':
    unittest.main()
