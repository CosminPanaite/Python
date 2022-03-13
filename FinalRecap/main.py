from Domain.TeamClass import Team
from Repository.repo import TeamRepository
repo=TeamRepository()
def printRepo(repo):
    print("Current repo ")
    for elem in repo.get_data():
        print(elem)


t1=Team("t1",990,1)
t2=Team("t2",90,2)
t3=Team("t3",190,3)
try:
    repo.add_a_team(t1)

except Exception as e:
    print("Exception !")
try:
    repo.add_a_team(t2)

except Exception as e:
    print("Exception !")

try:
    repo.add_a_team(t3)

except Exception as e:
    print("Exception !")

print("Add a team: ")
printRepo(repo)
repo.delete_team_with_score_under_100()
printRepo(repo)
repo.filter_score_above_100()
printRepo(repo)
repo.update_score_of_a_given_team(0,300)
printRepo(repo)
repo.sort_descending()
printRepo(repo)