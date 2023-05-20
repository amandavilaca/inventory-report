from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(self, file_path: str) -> list[dict]:
        raise NotImplementedError
