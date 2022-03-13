from Domain.my_point import MyPoint


def test_my_point():
    point1 = MyPoint(12, 13, "red")
    assert point1.coord_x == 12
    assert point1.coord_y == 13
    assert point1.colour == "red"
    assert point1.getColour() == "red"
    point1.set_coord_x(1)
    point1.set_coord_y(2)
    point1.set_Colour("yellow")
    assert point1.getCoordinate_X() == 1
    assert point1.getCoordinate_Y() == 2
    assert point1.getColour() == "yellow"
    try:
        point2 = MyPoint('a', 'b', 'black')
    except ValueError:
        assert True
    except Exception:
        assert False
