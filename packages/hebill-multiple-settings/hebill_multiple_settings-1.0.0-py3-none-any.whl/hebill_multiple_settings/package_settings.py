from .common_settings import common_settings


class package_settings(common_settings):
    def __init__(self, file: str, name: str = "settings"):
        super().__init__()
        self._file = file
        self._name = name
        self.load()

    @property
    def file(self):
        return self._file

    def load(self):
        import importlib.machinery
        try:
            loader = importlib.machinery.SourceFileLoader(self._name, self._file)
            loaded_module = loader.load_module()
            loaded_attr = getattr(loaded_module, self._name)
            if isinstance(loaded_attr, dict):
                result = loaded_attr
            else:
                result = {}
        except (FileNotFoundError, ImportError, AttributeError, Exception):
            result = {}
        self._cached_settings = result
