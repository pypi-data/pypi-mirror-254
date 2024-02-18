from hebill_multiple_settings.common_settings import common_settings


class user_settings(common_settings):
    def set(self, key: str, value):
        self._cached_settings[key] = value
