def search(lst,cond):
    lst2=[]
    for elem in lst:
        if cond(elem)!=False:
            lst2.append(elem)
    return lst2