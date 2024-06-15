class LoggerMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class DB(metaclass=LoggerMeta):
    def __init__(self):
        self._client = "REDIS"
        self._data: dict[any, any] = dict()

    def delete(self, key: any) -> None:
        del self._data[key]

    def get(self, key: any) -> any:
        return self._data.get(key)

    def set(self, key: any, value: any) -> None:
        self._data[key] = value
