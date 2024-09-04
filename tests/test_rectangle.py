import pytest

import source.shapes as shapes

def test_area():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.area() == 200