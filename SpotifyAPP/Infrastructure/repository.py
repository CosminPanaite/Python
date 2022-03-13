from Domain.MusicApp import MusicApp
class Repo(list):
    def add_a_song(self,s:MusicApp):
        self.append(s)
    def update_a_song(self,index,new_name,new_views,new_category):
        if self[index].get_views()<0:
           raise ValueError("This must be positive")
        self[index].set_name(new_name)
        self[index].set_views(new_views)
        self[index].set_category(new_category)
    def __str__(self):
        rock="Rock : "
        pop="Pop  : "
        for elem in self:
            if elem.get_category()==1:
                rock=rock+str(elem)
            if elem.get_category()==2:
                pop=pop+str(elem)
        return rock + "\n" + pop + "\n"
    def most_listened(self,c1,c2):
        if c1==c2 and c1<1 and c2>2 and c1 <1 and c2>2:
            raise ValueError("They must be 1 or 2 and different")
        a=self[0]
        b=self[0]
        for elem in range(len(self)):
            if self[elem].get_category() == c1:
                lst1 = filter(lambda x: x.get_category() == c1, self)
                lst2 = sorted(lst1, key=lambda x: x.get_views(), reverse=True)
                b = lst2[0]
        for elem in range(len(self)):
            if self[elem].get_category() == c2:
                lst3 = filter(lambda x:x.get_category()==c2,self)
                lst4=sorted(lst3,key=lambda x:x.get_views(),reverse=True)
                b=lst4[0]
        return a,b
    def less_vid_artist(self,c1,c2):
        a=""
        b=""
        for elem in range(len(self)):

            if   self[elem].get_category()==c1:
                lst=filter(lambda x:x.get_category()==c1,self)
                lst2=sorted(lst,key=lambda x:x.get_views(),reverse=False)
                a=lst2[0].get_name()
        for elem in range(len(self)):
            if self[elem].get_category() == c2:
                lst3 = filter(lambda x: x.get_category()==c2, self)
                lst4 = sorted(lst3, key=lambda x: x.get_views(), reverse=False)
                b = lst4[0].get_name()
        tupl=a,b
        return tupl
