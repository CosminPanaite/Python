from  Domain.MusicApp import MusicApp
from Infrastructure.repository import Repo
s1=MusicApp("Song1 ",60000,1)
s2=MusicApp("Song2 ",30000,2)
s3=MusicApp("Song3 ",40000,2)
s4=MusicApp("Song4 ",70000,2)
s5=MusicApp("Song5 ",50000,1)
s6=MusicApp("Song6 ",40000,1)
repo=Repo([s1,s2,s3,s4,s5])
repo.add_a_song(s6)
print(repo)
t=repo.most_listened(1,2)
print(t[0])
print(t[1])

t1=repo.less_vid_artist(1,2)

print(t1[0])
print(t1[1])
def test_less_vid_artist():
    s1 = MusicApp("Song1 ", 60000, 1)
    s2 = MusicApp("Song2 ", 30000, 2)
    s3 = MusicApp("Song3 ", 40000, 2)
    s4 = MusicApp("Song4 ", 70000, 2)
    s5 = MusicApp("Song5 ", 50000, 1)

    reppo = Repo([s1, s2, s3, s4, s5])
    reppppo= Repo([])
    repppooo= Repo([s1,s2])
    assert reppppo.less_vid_artist(1, 2) == ("","")
    assert repppooo.less_vid_artist(1,2)==('Song1 ',"Song2 ")

test_less_vid_artist()