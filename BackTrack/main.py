def permut3():
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):

                possibleSolution = [i,j,k]

                if i!=j and j!=k and k!=i:
                    yield   possibleSolution
def callPermut3():
    for p in permut3():
        print(p)
callPermut3()