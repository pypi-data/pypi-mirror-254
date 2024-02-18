class common_settings:
    def __init__(self):
        self._cached_settings = {}

    @property
    def all(self) -> dict:
        return self._cached_settings

    def get(self, key: str) -> str:
        return self._cached_settings.get(key)
