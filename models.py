from pydantic import BaseModel


class Item(BaseModel):
    title: str
    pubdate: str
    link: str


class Items(BaseModel):
    items: list[Item]
