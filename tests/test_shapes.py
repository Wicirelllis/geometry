import pytest
from pytest import approx

from geometry.shapes import Circle, Triangle


class TestCircle:
    def test_negative_radius(self):
        with pytest.raises(ValueError):
            c = Circle(-1)

    @pytest.mark.parametrize('r,expected', [
        (0, 0),
        (1, 3.14),
        (2, 12.56),
    ])
    def test_area(self, r, expected):
        c = Circle(r)
        assert c.area == approx(expected, abs=0.01)


class TestTriangle:
    @pytest.mark.parametrize('a,b,c', [
        (0, -1, 0),
        (1, 1, -1),
    ])
    def test_negative_edge(self, a, b, c):
        with pytest.raises(ValueError):
            t = Triangle(a, b, c)

    @pytest.mark.parametrize('a,b,c', [
        (0, 0, 1),
        (1, 5, 0),
    ])
    def test_triangle_inequality(self, a, b, c):
        with pytest.raises(ValueError):
            t = Triangle(a, b, c)

    @pytest.mark.parametrize('a,b,c,expected', [
        (0, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 3, 2, 0),
        (1, 1, 1, 0.43),
        (3, 4, 5, 6),
    ])
    def test_area(seelf, a, b, c, expected):
        t = Triangle(a, b, c)
        assert t.area == approx(expected, abs=0.01)
