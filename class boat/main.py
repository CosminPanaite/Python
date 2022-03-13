from Domain.Boat import Boat
from Repo.repo import Repo
repo=Repo()
tip=input("tip ")
b1=Boat(1,"New",20.7,False)
b3=Boat(2,"New1",670.7,False)
b2=Boat(3,"New2",50.7,True)
b4=Boat(4,"New3",40.7,False)
repo.add_a_boat(b1)
repo.add_a_boat(b2)
repo.add_a_boat(b3)
repo.add_a_boat(b4)

def printRepo(repo):
    print("Our repo!")
    for elem in repo.get_all_boats():
        print (elem)
printRepo(repo)

printRepo(repo)
repo.delete()
printRepo(repo)
print("((")
lst1=repo.sort_unrented()
for elm in lst1:
    printI(elm)

lst=repo.identify_givven(0)
for el in lst:
    print(el)


