from zkmarek.field import Field
from typing import Generic, TypeVar

FieldType = TypeVar("FieldType")

class ECAffine(Generic[FieldType]):
    coords: list[Field]

    def __init__(self, coords: list[Field]):
        assert(len(coords) == 2)
        assert(coords[0].order == coords[1].order)
        self.coords = coords

    def __getitem__(self, key):
        return self.coords[key]

    @staticmethod
    def from_int(coords: list[int], order) -> "ECAffine":
        return ECAffine([Field(c, order) for c in coords])
