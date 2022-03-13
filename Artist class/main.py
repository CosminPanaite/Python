from Repository.repo import Repo
from Domain.Artist import Artist

repo=Repo()
a1=Artist(1,"Abb","Nop",2000)
a2=Artist(2,"Acc","Dop",2000)
a3=Artist(3,"C","Cop",2000)
a4=Artist(4,"D","Nop",2000)
repo.add_an_artist(a1)
repo.add_an_artist(a2)
repo.add_an_artist(a3)
repo.add_an_artist(a4)

def printRepo(repo):
    print("Current repo")
    for elem in repo.get_all_artists():
        print(elem)
printRepo(repo)
repo.update_artist(0,2,"Trey","Yeah",2003)
printRepo(repo)
repo.delete_by_style()
printRepo(repo)
repo.sort_after_filter()
printRepo(repo)
repo.identify()
printRepo(repo)