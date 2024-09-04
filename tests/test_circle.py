import pytest # type: ignore

import source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print (f"Setting up {method}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print (f"Tearing down {method}")
    def test_one(self):
        assert True
    
    def test_area(self):
        assert self.circle.area() == 3.14 * self.circle.radius ** 2

    def test_circumference(self):
        circumference = self.circle.perimeter()
        expected = 2 * 3.14 * self.circle.radius

        assert circumference == expected