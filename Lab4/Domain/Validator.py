from Domain.MyVector import MyVector


class VectorValidator:
    def validate_vector(self, vector: MyVector):
        '''
        It validates errors from class MyVector
        :param vector:
        :return:
        '''
        errors_list = []

        if type(vector.get_name_id()) not in [str, int]:
            errors_list.append((f"Diffrent value type required: integer or string. {type(vector.get_name_id())} found"))

        if vector.get_colour() not in ["r", "g", "b", "y", "m"]:
            errors_list.append("The colour should belong to list of specified colours")

        if vector.get_vector_type() != int(vector.get_vector_type()) or vector.get_vector_type() < 1:
            errors_list.append("Number should be greater than 1 and integer")

        if len(errors_list) :
            raise ValueError(errors_list)
