from .package_settings import package_settings
from .user_settings import user_settings


class multiple_settings:
    def __init__(self, system_settings_file: str, default_settings_file: str,
                 system_settings_module: str = "settings", default_settings_module: str = "settings"):
        self._cached_system_settings = package_settings(system_settings_file, system_settings_module)
        self._cached_default_settings = package_settings(default_settings_file, default_settings_module)
        self._cached_user_settings = user_settings()

    @property
    def system(self) -> package_settings:
        return self._cached_system_settings

    @property
    def default(self) -> package_settings:
        return self._cached_default_settings

    @property
    def user(self) -> user_settings:
        return self._cached_user_settings

    def get(self, key: str) -> str | None:
        result = self.user.get(key)
        if result is not None:
            return result
        result = self.default.get(key)
        if result is not None:
            return result
        result = self.system.get(key)
        if result is not None:
            return result
        return None
