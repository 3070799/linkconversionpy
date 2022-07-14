class Link:
    def __init__(self, original_url: str, short_url: str):
        self._original_url = original_url
        self._short_url = short_url

    def get_original_url(self):
        return self._original_url

    def get_short_url(self):
        return self._short_url

    def set_original_url(self, value: str):
        self._original_url = value

    def set_short_url(self, value: str):
        self._short_url = value
