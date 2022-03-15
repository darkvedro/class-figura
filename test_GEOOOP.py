import pytest
from FIGURAS import FIGURA
from FIGURAS import TREUGOLNIK
from FIGURAS import PRYAMOUGOLNIK
from FIGURAS import KVADRAT
from FIGURAS import KRUG

FIGURA = FIGURA()
TREUGOLNIK = TREUGOLNIK(20, 20, 20)
PRYAMOUGOLNIK = PRYAMOUGOLNIK(30, 30)
KVADRAT = KVADRAT(40, 40)
KRUG = KRUG(50)

class TestFigures:

    def test_TREUGOLNIK_name(self):
        assert FIGURA.get_name(TREUGOLNIK) == 'TREUGOLNIK'

    def test_TREUGOLNIK_angles(self):
        assert FIGURA.get_angles(TREUGOLNIK) == 3

    def test_TREUGOLNIK_area(self):
        assert round(TREUGOLNIK.calculate_area()) == 173

    def test_TREUGOLNIK_perimeter(self):
        assert TREUGOLNIK.calculate_perimeter() == 60

    def test_TREUGOLNIK_size(self):
        assert TREUGOLNIK.calculate_perimeter() < TREUGOLNIK.calculate_area()

    def test_PRYAMOUGOLNIK_name(self):
        assert FIGURA.get_name(PRYAMOUGOLNIK) == 'PRYAMOUGOLNIK'

    def test_PRYAMOUGOLNIK_angles(self):
        assert FIGURA.get_angles(PRYAMOUGOLNIK) == 4

    def test_PRYAMOUGOLNIK_area(self):
        assert PRYAMOUGOLNIK.calculate_area() == 900

    def test_PRYAMOUGOLNIK_perimeter(self):
        assert PRYAMOUGOLNIK.calculate_perimeter() == 120

    def test_PRYAMOUGOLNIK_size(self):
        assert PRYAMOUGOLNIK.calculate_perimeter() < PRYAMOUGOLNIK.calculate_area()

    def test_KVADRAT_name(self):
        assert FIGURA.get_name(KVADRAT) == 'KVADRAT'

    def test_KVADRAT_angles(self):
        assert FIGURA.get_angles(KVADRAT) == 4

    def test_KVADRAT_area(self):
        assert KVADRAT.calculate_area() == 1600

    def test_KVADRAT_perimeter(self):
        assert KVADRAT.calculate_perimeter() == 160

    def test_KVADRAT_size(self):
        assert KVADRAT.calculate_perimeter() < KVADRAT.calculate_area()

    def test_KRUG_name(self):
        assert FIGURA.get_name(KRUG) == 'KRUG'

    def test_KRUG_angles(self):
        assert FIGURA.get_angles(KRUG) == 0

    def test_KRUG_area(self):
        assert round(KRUG.calculate_area()) == 7854

    def test_KRUG_perimeter(self):
        assert KRUG.calculate_perimeter() == 314

    def test_KRUG_size(self):
        assert KRUG.calculate_perimeter() < KRUG.calculate_area()

    @pytest.mark.parametrize('other_figure', [PRYAMOUGOLNIK, TREUGOLNIK, KVADRAT, KRUG, 111])
    @pytest.mark.parametrize('FIGURA', [TREUGOLNIK, PRYAMOUGOLNIK, KVADRAT, KRUG])
    def test_add_KVADRAT(self, other_figure, FIGURA):
        assert FIGURA.add_area(other_figure) == FIGURA.area + other_figure.area
