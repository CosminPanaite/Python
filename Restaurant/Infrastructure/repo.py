from Domain.restaurant import Restaurant
class Repo(list):

    def add_a_restaurant(self,r:Restaurant):
        self.append(r)
    def __str__(self):
        vegetarian="Vegetarian :"
        non_vegetarian = "Non-Vegetarian :"
        for elem in self:
            if elem.get_category()==1:
                vegetarian=vegetarian+ str(elem) + " // "
            if elem.get_category()==2:
                non_vegetarian=non_vegetarian+str(elem) + " // "
        return vegetarian + '\n' + non_vegetarian + '\n\n'
    def update(self,index,new_name,new_calories):
        if index<0 and index>len(self):
            raise ValueError("No out of range")
        if self[index].get_calories()<0:
            raise ValueError("This must be positive!")

        self[index].set_calories(new_calories)
        self[index].set_name(new_name)
    def min_cal(self):
        min1=self[0]
        min_cal=999999
        min2=self[0]
        for elem in range(len(self)):
            if self[elem].get_category()==1 and self[elem].get_category()<min_cal:
                min1=self[elem]
        for elem in range(len(self)):
            if self[elem].get_category() == 2 and self[elem].get_category() < min_cal:
                min1 = self[elem]


        return min1,min2
