import pytest
from zkmarek.field import Field


class TestField:
    def test_init(self):
        f = Field(1, 13)
        assert f.value == 1
        assert f.order == 13

    def test_init_underflow(self):
        f = Field(-1, 13)
        assert f.value == 12
        assert f.order == 13

    def test_init_overflow(self):
        f = Field(20, 13)
        assert f.value == 7
        assert f.order == 13

    def test_eq(self):
        assert Field(1, 13) == Field(1, 13)
        assert Field(28, 29) == Field(28, 29)
        assert Field(13, 1) == Field(13, 1)
        assert Field(12, 13) == Field(-1, 13)
        assert Field(2, 1) == Field(1, 1)

    def test_eq_unequal_values(self):
        assert Field(3, 29) != Field(4, 29)
        assert Field(-1, 29) != Field(1, 29)

    def test_eq_unequal_orders(self):
        with pytest.raises(AssertionError):
            Field(1, 13) == Field(1, 41)
        with pytest.raises(AssertionError):
            Field(3, 13) == Field(3, 29)

    def test_add(self):
        assert Field(1, 13) + Field(10, 13) == Field(11, 13)
        assert Field(10, 13) + Field(10, 13) == Field(7, 13)

    def test_add_unequal_orders(self):
        with pytest.raises(AssertionError):
            Field(2, 13) + Field(2, 41)

    def test_sub(self):
        assert Field(0, 13) - Field(1, 13) == Field(12, 13)
        assert Field(10, 13) - Field(20, 13) == Field(3, 13)

    def test_sub_unequal_orders(self):
        with pytest.raises(AssertionError):
            Field(2, 13) - Field(2, 41)

    def test_mul(self):
        assert Field(2, 13) * Field(2, 13) == Field(4, 13)
        assert Field(4, 13) * Field(4, 13) == Field(3, 13)

    def test_mul_unequal_orders(self):
        with pytest.raises(AssertionError):
            Field(2, 13) * Field(2, 41)

    def test_pow(self):
        assert Field(2, 13) ** 2 == Field(4, 13)
        assert Field(2, 13) ** 4 == Field(3, 13)

    def test_neg(self):
        assert -Field(1, 3) == Field(2, 3)
        assert -Field(2, 3) == Field(1, 3)
        assert -Field(17, 29) == Field(12, 29)
