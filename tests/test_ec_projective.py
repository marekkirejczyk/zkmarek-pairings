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

    def test_from_affine(self):
        affine = ECAffine.from_int([1, 7], 41)
        actual = ECProjective.from_affine(affine).coords
        assert actual == [Field(1, 41), Field(7, 41), Field(1, 41)]

    def test_from_to_affine(self):
        affine = ECAffine.from_int([1, 7], 41)
        actual = ECProjective.from_affine(affine).to_affine()
        assert actual.coords == affine.coords

