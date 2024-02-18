from pydantic import BaseModel

class DisplayConfiguration(BaseModel):
    width: int = 800
    height: int = 480
    colors: int = 7