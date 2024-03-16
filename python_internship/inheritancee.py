# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# d1=Dog("jack")
# print(d1.name)
# print(d1.make_sound())

class Brands:
    brand_name_1="zudio"
    brand_name_2="lulu"
    brand_name_3="mcdonalds"

class Products:
    prod_1="clothing brand"
    prod_2="shopping mall"
    prod_3="food brand"

class Popularity(Brands,Products):
    prod_1_popularity=100
    prod_2_popularity=100
    prod_3_popularity=100


obj_1=Popularity()
print(obj_1.brand_name_1+"is a"+obj_1.prod_1+"is",obj_1.prod_1_popularity)