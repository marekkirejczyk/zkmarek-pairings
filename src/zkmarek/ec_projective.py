from zkmarek.ec_affine import ECAffine
from zkmarek.field import Field


class ECProjective:
    coords: list[Field]

    def __init__(self, coords: list[Field]):
        assert len(coords) == 3
        assert coords[0].order == coords[1].order == coords[2].order
        self.coords = coords

    def __getitem__(self, key: int) -> Field:
        return self.coords[key]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ECProjective):
            return NotImplemented
        return self.coords == other.coords

    def to_affine(self):
        return ECAffine([self[0] / self[2], self[1] / self[2]])

    def __str__(self):
        return f"({self[0]}:{self[1]}:{self[2]})"

    #dbl-1998-cmo-2 from https://www.hyperelliptic.org/EFD/g1p/auto-shortw-projective.html
    def double(self):
        pass

    #add-1998-cmo-2 from https://www.hyperelliptic.org/EFD/g1p/auto-shortw-projective.html
    def __add__(self, other: "ECProjective"):
        x1, y1, z1 = self.coords
        x2, y2, z2 = other.coords
        two = Field(2, x1.order)
        y1z2 = y1*z2
        x1z2 = x1*z2
        z1z2 = z1*z2
        u = y2*z1-y1z2
        uu = u * u
        v = x2*z1-x1z2
        vv = v*v
        vvv = v*vv
        r = vv*x1z2
        a = uu*z1z2-vvv-r*two
        x3 = v*a
        y3 = u*(r-a)-vvv*y1z2
        z3 = vvv*z1z2
        return ECProjective([x3, y3, z3])

    def is_infinity(self):
        return self[0].value == 0 and self[2].value == 0

    @staticmethod
    def from_affine(other: ECAffine):
        return ECProjective([other[0], other[1], Field(1, other[0].order)])

    @staticmethod
    def from_int(coords: list[int], order: int) -> "ECProjective":
        return ECProjective([Field(c, order) for c in coords])
