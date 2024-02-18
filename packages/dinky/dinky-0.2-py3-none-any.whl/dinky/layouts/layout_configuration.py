from pydantic import BaseModel
from typing import List

from dinky.display_configuration import DisplayConfiguration

class Zone(BaseModel):
    id: str
    x: int
    y: int
    width: int
    height: int
    padding: int

class BaseLayoutConfiguration(BaseModel):
    display_configuration: DisplayConfiguration
    title: str
    zones: List[Zone]

    def is_valid(self) -> bool:
        raise Exception(f"'is_valid' not implemented for {self.__module__}")