import dbm
import typing as t
from pathlib import Path
from uuid import UUID, uuid4

from . import const
from .typing import PathLike


class _Messages:
    def __init__(self, db: dbm._Database):
        self.db = db

    def __getitem__(self, index: int) -> t.Any:
        return self.db.get(f"messages:{index}", None)

    def __setitem__(self, index: int, value: t.Any):
        self.db[f"messages:{index}"] = value

class Conversation:
    def __init__(
        self,
        uuid: UUID | None = None,
        path: PathLike,
    ):
        self.path = Path(path)

    @property
    def db(self) -> dbm._Database:
        if (_db := getattr(self, "_db", None)) is not None:
            return _db
        setattr(self, "_db", self._create_db())
        return getattr(self, "_db")

    def _create_db(self) -> dbm._Database:
        return dbm.open(str(self.path), "w")

    @classmethod
    def create(cls, addr: tuple[str, int]) -> "Conversation":
        uuid = uuid4()
        conversation = cls(uuid, const.DATA_PATH / str(uuid))
        conversation.addr = addr
        return conversation

    @property
    def uuid(self) -> UUID:
        return t.cast(UUID, UUID(self.db["uuid"].decode()))

    @uuid.setter
    def uuid(self, uuid: UUID):
        self.db["uuid"] = str(uuid)

    @property
    def addr(self) -> tuple[str, int]:
        return t.cast(tuple[str, int], self.db["addr"].decode().split(":"))

    @addr.setter
    def addr(self, addr: tuple[str, int]):
        self.db["addr"] = f"{addr[0]}:{addr[1]}"
