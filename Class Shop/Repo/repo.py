from Domainnnn.Shop import Shop
class Repo():
    def __init__(self):
        self.__data_storage=[]
    def add_a_shop(self,shop:Shop):
        self.__data_storage.append(shop)
    def get_all_shops(self):
        return self.__data_storage
    def delete(self):
        maxi=-1
        for i in range(0,len(self.__data_storage)):
            if len(self.__data_storage[i].get_name())>maxi:
                maxi=len(self.__data_storage[i].get_name())

        for elm in range(len(self.__data_storage)-1,-1,-1):
            if  len(self.__data_storage[elm].get_name())==maxi:
                del self.__data_storage[elm]
    def update(self,index,new_name):
        if index<0 or index>len(self.__data_storage):
            raise ValueError("Out of range")
        self.__data_storage[index].set_name(new_name)
    def sort_desc(self):
        return sorted(self.__data_storage,key=lambda x:len(x.get_list_of_products()),reverse=True)
    def identify(self):
        return list(filter(lambda x:(x.get_id())%2==1,self.__data_storage))