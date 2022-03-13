def bubbleSort(my_list, condition):
    '''
    Bubble sort method
    :param my_list:
    :param condition:
    :return:
    '''
    ok = False
    while (not ok):
        ok = True
        for i in range(0, len(my_list) - 1):
            if condition(my_list[i]) > condition(my_list[i + 1]):
                aux = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = aux
                ok = False
    return my_list


def seqSearch(my_list, condition):
    '''
    Sequential search: implementati on Unordered list
    :param elem:
    :param l:
    :return:
    '''
    result = []
    for i in my_list:
        if condition(i) != False:
            result.append(i)
    return result
