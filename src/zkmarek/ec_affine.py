from zkmarek.field import Field

class ECAffine:
    coords: list[Field]

    def __init__(self, coords: list[Field]):
        assert(len(coords) == 2)
        assert(coords[0].order == coords[1].order)
        self.coords = coords

    def __getitem__(self, key: int) -> Field:
        return self.coords[key]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ECAffine):
            return NotImplemented
        return self.coords == other.coords

    @staticmethod
    def from_int(coords: list[int], order: int) -> "ECAffine":
        return ECAffine([Field(c, order) for c in coords])
