from Repository.my_point_repository import PointRepository


def test_add_point_to_the_repository():
    list_of_points = PointRepository()
    list_of_points.add_point_to_the_repository(12, 14, 'red')
    assert len(list_of_points.get_all_points()) == 1
    try:
        list_of_points.add_point_to_the_repository(3, 4, 'purple')
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    list_of_points.add_point_to_the_repository(12.5, 14.23, 'yellow')
    assert len(list_of_points.get_all_points()) == 2
    try:
        list_of_points.add_point_to_the_repository(8.4, 5, 'olive')
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
    list_of_points.add_point_to_the_repository(23, 18, 'magenta')
    assert len(list_of_points.get_all_points()) == 3


def test_get_a_point_at_a_given_index():
    list_of_points = PointRepository()
    list_of_points.add_point_to_the_repository(20, 5, 'magenta')
    list_of_points.add_point_to_the_repository(10, 6, 'red')
    list_of_points.add_point_to_the_repository(3, 8, 'green')
    list_of_points.add_point_to_the_repository(73, 7, 'magenta')
    assert list_of_points.get_a_point_at_a_given_index(1) != None
    assert list_of_points.get_a_point_at_a_given_index(3) != None
    assert list_of_points.get_a_point_at_a_given_index(0) != None
    assert list_of_points.get_a_point_at_a_given_index(2) != None
    try:
        list_of_points.get_a_point_at_a_given_index(16)
        assert False
    except IndexError:
        assert True
    except Exception:
        assert False
    try:
        list_of_points.get_a_point_at_a_given_index(-16)
        assert False
    except IndexError:
        assert True
    except Exception:
        assert False
    try:
        list_of_points.get_a_point_at_a_given_index(6)
        assert False
    except IndexError:
        assert True
    except Exception:
        assert False


def test_update_a_point_at_a_given_index():
    list_of_points = PointRepository()
    list_of_points.add_point_to_the_repository(20, 5, 'magenta')
    list_of_points.add_point_to_the_repository(10, 6, 'red')
    list_of_points.update_a_point_at_a_given_index(0, 4, 7, "green")
    list_of_points.update_a_point_at_a_given_index(1, 40, 70, "green")
    list1 = list_of_points.get_all_points()
    point = list1[0]
    point1 = list1[1]
    assert point.coord_x == 4
    assert point.coord_y == 7
    assert point.colour == "green"
    assert point1.coord_x == 40
    assert point1.coord_y == 70
    assert point1.colour == "green"
    try:
        list_of_points.update_a_point_at_a_given_index(-1, 2, 4, "red")
        assert False
    except IndexError:
        assert True
    except Exception:
        assert False
    try:
        list_of_points.update_a_point_at_a_given_index(-17, 2, 4, "red")
        assert False
    except IndexError:
        assert True
    except Exception:
        assert False
    try:
        list_of_points.update_a_point_at_a_given_index(1, 22, 40, "purple")
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False
