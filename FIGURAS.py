import math
from math import pi


class FIGURA:
    # Общая фигура
    angles = None
    name = None
    perimeter = None
    area = None

    def add_area(self, other_figure):
        if isinstance(other_figure, FIGURA):
            sum_areas = self.area + other_figure.area
            return sum_areas
        else:
            return 'Peredan klass ne figuri'

    def get_angles(self, figure):
        return figure.angles

    def get_name(self, figure):
        return figure.name


class TREUGOLNIK(FIGURA):

    def __init__(self, side_a, side_b, side_c):

        self.name = 'TREUGOLNIK'
        self.angles = 3
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    def calculate_area(self):

        half_perimeter = 0.5 * self.calculate_perimeter()
        area = math.sqrt(half_perimeter *
                         (half_perimeter - self.side_a) *
                         (half_perimeter - self.side_b) *
                         (half_perimeter - self.side_c))
        return area


class PRYAMOUGOLNIK(FIGURA):
    def __init__(self, side_a, side_b):
        self.name = 'PRYAMOUGOLNIK'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):

        area = self.side_a * self.side_b
        return area


class KVADRAT(FIGURA):

    def __init__(self, side_a, side_b):

        self.name = 'KVADRAT'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):

        area = self.side_a * self.side_b
        return area


class KRUG(FIGURA):

    def __init__(self, radius):

        self.name = 'KRUG'
        self.angles = 0
        self.radius = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):

        perimeter = round(2 * pi * self.radius)
        return perimeter

    def calculate_area(self):

        area = round(pi * (self.radius ** 2))
        return area