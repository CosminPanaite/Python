
from Domain.restaurant import Restaurant
from Infrastructure.repo import Repo

d1=Restaurant("rICE",400,1)
d2=Restaurant("Pilaf",600,1)
d3=Restaurant("sarmale",2300,2)
d4=Restaurant("Nutella",1000,2)
repo=Repo([d1,d2,Restaurant("Chilaf",500,1),Restaurant("Pulpe",400,2),Restaurant("Paste",400,1),Restaurant("Piure cu carne",900,2)])
def printRepo():
    for elem in repo:
        print(elem)
printRepo()
repo.add_a_restaurant(d1)
print(repo)
t=repo.min_cal()
print(t[0])
print(t[1])