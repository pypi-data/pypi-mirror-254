from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Database:

    database_name: str
    server: str
    port: int
    database: str
    username: str
    password: str
    dialect: str
    project_uid: str = "0"

    uid: str = field(init=False)
    instance_counter: ClassVar[int] = 0

    def __post_init__(self):
        self.__class__.instance_counter += 1
        self.uid = str(self.instance_counter)
