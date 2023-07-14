import secrets

class Field:
    value: int
    order: int

    def __init__(self, value: int, order: int):
        self.value = value % order
        self.order = order

    def __eq__(self, other: "Field") -> bool:
        assert self.order == other.order
        return self.value == other.value

    def __add__(self, rhs: "Field") -> "Field":
        assert self.order == rhs.order
        return Field(self.value + rhs.value, self.order)

    def __sub__(self, rhs: "Field") -> "Field":
        assert self.order == rhs.order
        return Field(self.value - rhs.value, self.order)

    def __mul__(self, rhs: "Field") -> "Field":
        assert self.order == rhs.order
        return Field(self.value * rhs.value, self.order)

    def __pow__(self, rhs: int) -> "Field":
        return Field(pow(self.value, rhs, self.order), self.order)

    def __neg__(self) -> "Field":
        return Field(-self.value % self.order, self.order)

    def inv(self) -> "Field":
        if self.value == 0:
            raise ZeroDivisionError()
        prev_r = self.order
        r = self.value
        prev_t, t = 0, 1
        while (r != 0):
            quotient = prev_r // r
            prev_r, r = r, prev_r - quotient * r
            prev_t, t = t, prev_t - quotient * t
        return Field(prev_t, self.order)

    def __str__(self) -> str:
        return f"({self.value} % {self.order})"

    def __repr__(self) -> str:
        return f"({self.value} % {self.order})"

    def __truediv__(self, other) -> "Field":
        return self * other.inv()

    def __hash__(self):
        return hash((self.value, self.order))

    @staticmethod
    def random(p) -> "Field":
        return Field(secrets.randbelow(p), p)
