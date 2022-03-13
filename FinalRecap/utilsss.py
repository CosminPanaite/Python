def search(lst,cond):
    for elem in lst:
        if cond(elem)!=False:
            lst2.append(elem)
    return lst2