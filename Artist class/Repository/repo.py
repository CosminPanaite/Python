from Domain.Artist import Artist
from Utils import search
class Repo():
    def __init__(self):
        self.__data_storage=[]
    def get_all_artists(self):
        return self.__data_storage
    def add_an_artist(self,artist:Artist):
        self.__data_storage.append(artist)
    def update_artist(self,index,new_id,new_name,new_style,new_birth):
        self.__data_storage[index].set_id(new_id)
        self.__data_storage[index].set_name(new_name)
        self.__data_storage[index].set_style(new_style)
        self.__data_storage[index].set_birth(new_birth)
    def delete_by_style(self):
        for elem in range(len(self.__data_storage)-1,-1,-1):
            if self.__data_storage[elem].get_style()=="Nop":
                del self.__data_storage[elem]
    def sort_after_filter(self):
        lst=list(filter(lambda x:x.get_name()[0]=="A",self.__data_storage))
        return sorted(lst,key=lambda x:x.get_name(),reverse=True)
    def identify(self):
        return search(self.__data_storage,lambda x:x.get_name()=="A")
