from typing import Optional
from pydantic import BaseModel


class MemeBase(BaseModel):
    description: Optional[str] = None


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    pass


class Meme(MemeBase):
    id: int
    image_url: str

    class Config:
        orm_mode = True
