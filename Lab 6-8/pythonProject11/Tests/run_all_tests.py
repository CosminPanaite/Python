from Tests.test_domain import test_my_point
from Tests.test_my_point_repository import test_add_point_to_the_repository, test_get_a_point_at_a_given_index, \
    test_update_a_point_at_a_given_index


def run_all_tests():
    test_my_point()
    test_add_point_to_the_repository()
    test_get_a_point_at_a_given_index()
    test_update_a_point_at_a_given_index()