from Domain.Validator import VectorValidator
from Repository.repo import VectorRepository
from Domain.MyVector import MyVector


def data_examples():
    validator = VectorValidator()
    list_of_vectors = VectorRepository(validator)
    v = MyVector(1105, "y", 160, [7, 9])
    v1 =MyVector(1106, "m", 150, [4, 2])
    v2 =MyVector(1107, "g", 140, [3, 5])
    v3 =MyVector(1108, "r", 130, [45, 62])
    v4 =MyVector(1109, "r", 110, [4, 2])
    v5 =MyVector(1110, "r", 210, [7, 3])
    v6 = MyVector(1111, "r", 210, [177, 3])

    list_of_vectors.add_a_vector(v)
    list_of_vectors.add_a_vector(v1)
    print(list_of_vectors)
    list_of_vectors.add_a_vector(v2)
    list_of_vectors.add_a_vector(v3)
    list_of_vectors.add_a_vector(v4)
    list_of_vectors.add_a_vector(v5)
    list_of_vectors.get_all_vectors()
    for vec in list_of_vectors.get_all_vectors():
        print(vec, end=" ; ")
    print()
    print(list_of_vectors.get_a_vector_at_an_index(1))
    list_of_vectors.update_a_vector(0,"r",25000,[25,30,45])
    for vec1 in list_of_vectors.get_all_vectors():
        print(vec1, end=" ; ")
    print()
    list_of_vectors.update_a_vector_by_name(1106,"g",2552,[1,2,3,4,5])
    for vec2 in list_of_vectors.get_all_vectors():
        print(vec2, end=" ; ")
    print()
    list_of_vectors.delete_a_vector_by_index(0)
    for vec3 in list_of_vectors.get_all_vectors():
        print(vec3, end=" ; ")
    print()
    list_of_vectors.delete_a_vector_by_name(1106)
    for vec4 in list_of_vectors.get_all_vectors():
        print(vec4, end=" ; ")
    print()
    print(list_of_vectors.get_the_sum_of_all_vectors()," --> sum of all vectors")
    list_of_vectors.add_a_vector(v6)
    print(list_of_vectors.get_the_sum_of_all_vectors(), " --> sum of all vectors")

    list_of_vectors.get_the_list_of_vector_with_minimum_elements(6)
    for vec5 in list_of_vectors.get_all_vectors():
        print(vec5, end=" ; ")
    print()
    print()