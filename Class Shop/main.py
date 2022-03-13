from Domainnnn.Shop import Shop
from Repo.repo import Repo
reppo=Repo()
s1=Shop(20,"n12222222","here",[1,2,3,32,2,4,5])
s2=Shop(21,"n22","heres",[1,2,3,4])
s3=Shop(22,"n03","herep",[1,2,3,56,7])
s4=Shop(23,"nooo4","her",[1,2,3,4])
reppo.add_a_shop(s1)
reppo.add_a_shop(s2)
reppo.add_a_shop(s3)
reppo.add_a_shop(s4)


def printRepo(reppo):
    print("Repo ")
    for elem in reppo.get_all_shops():
        print(elem)
printRepo(reppo)
reppo.delete()
printRepo(reppo)