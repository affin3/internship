# a=10
# b=10
# print("addition of two numbers",a+b)

# str1="very"
# str2="good"
# print("concatenation of two strings",str1+str2)

# list1=[1,2,3]
# list2=['a','b']
# print("concatenation of two lists",list1+list2)

# class shape:
#     def area(self):
#         return 0
# class Circle(shape):
#     def __init__(self,radius):
#           self.radius=radius
#     def area(self):
#         return 3.14 * self.radius**2
#         circle=Circle(radius=2)
#         print(circle.area())

# class shape:
#     def area(self):
#         return 0
# class Square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side **2
# square=Square(side=8)
# print(square.area())

class Geek:

    def __init__(self,name,age):

        self.geekName=name
        self.geekAge=age

        def displayAge(self):
            print("Age:",self.geekAge)

obj=Geek("R2J",20)
print("Name:",obj.geekName)
obj.displayAge()