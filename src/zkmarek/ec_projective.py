from zkmarek.ec_affine import ECAffine
from zkmarek.field import Field


class ECProjective:
    coords: list[Field]

    def __init__(self, coords: list[Field]):
        assert(len(coords) == 3)
        assert(coords[0].order == coords[1].order == coords[2].order)
        self.coords = coords

    def __getitem__(self, key: int) -> Field:
        return self.coords[key]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ECProjective):
            return NotImplemented
        return self.coords == other.coords

    def to_affine(self):
        return ECAffine([self[0] / self[2], self[1] / self[2]])

    @staticmethod
    def from_affine(other: ECAffine):
        return ECProjective([other[0], other[1], Field(1, other[0].order)])

    @staticmethod
    def from_int(coords: list[int], order: int) -> "ECProjective":
        return ECProjective([Field(c, order) for c in coords])
