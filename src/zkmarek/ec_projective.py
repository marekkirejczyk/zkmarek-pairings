from zkmarek.ec_affine import ECAffine
from zkmarek.field import Field


class ECProjective:
    coords: list[Field]

    def __init__(self, coords: list[Field]):
        assert(len(coords) == 3)
        assert(coords[0].order == coords[1].order == coords[2].order)
        self.coords = coords

    def __getitem__(self, key):
        return self.coords[key]

    @staticmethod
    def from_affine(other: ECAffine):
        return ECProjective([other[0], other[1], Field(1, other[0].order)])

    def to_affine(self):
        return ECAffine([self[0] / self[2], self[1] / self[2]])

    @staticmethod
    def from_int(coords: list[int], order) -> "ECProjective":
        return ECProjective([Field(c, order) for c in coords])
