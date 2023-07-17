import pytest
from zkmarek.ec_affine import ECAffine
from zkmarek.ec_projective import ECProjective
from zkmarek.field import Field


class TestECProjective:
    def test_from_int(self):
        actual = ECProjective.from_int([1, 2, 3], 41).coords
        assert actual == [Field(1, 41), Field(2, 41), Field(3, 41)]

    def test_init(self):
        actual = ECProjective([Field(1, 41), Field(2, 41), Field(3, 41)]).coords
        assert actual == [Field(1, 41), Field(2, 41), Field(3, 41)]

    def test_init_wrong_dimension(self):
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 41)])
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 41), Field(2, 41)])
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 7), Field(2, 7), Field(2, 7), Field(2, 7)])

    def test_init_unequal_orders(self):
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 17), Field(2, 41), Field(3, 41)])
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 41), Field(2, 17), Field(3, 41)])
        with pytest.raises(AssertionError):
            ECProjective([Field(1, 41), Field(2, 41), Field(3, 17)])

    def test_eq(self):
        a = ECProjective.from_int([1, 7, 1], 41)
        b = ECProjective.from_int([1, 7, 1], 41)
        assert a == b

    def test_not_eq(self):
        a = ECProjective.from_int([1, 7, 1], 41)
        b = ECProjective.from_int([1, 34, 1], 41)
        assert a != b

    def test_add(self):
        a = ECProjective.from_int([1, 7, 1], 41)
        b = ECProjective.from_int([22, 6, 1], 41)
        actual = (a + b).to_affine()
        assert actual.coords == [Field(22, 41), Field(35, 41)]
        assert actual == ECAffine.from_int([22, 35], 41)

    def test_add_infinity(self):
        a = ECProjective.from_int([1, 7, 1], 41)
        b = ECProjective.from_int([1, 34, 1], 41)
        actual = a + b
        assert actual.is_infinity()

    def test_from_affine(self):
        affine = ECAffine.from_int([1, 7], 41)
        actual = ECProjective.from_affine(affine).coords
        assert actual == [Field(1, 41), Field(7, 41), Field(1, 41)]

    def test_from_to_affine(self):
        affine = ECAffine.from_int([1, 7], 41)
        actual = ECProjective.from_affine(affine).to_affine()
        assert actual.coords == affine.coords

    def test_from_to_affine_inf(self):
        projective = ECProjective.from_int([0, 7, 0], 41)
        with pytest.raises(ZeroDivisionError):
            projective.to_affine()

