# Develop a class ‘snake’ that has a method ‘introduction’. The method ‘introduction’ takes the name,
# color, and age of the snake. Make the object of snake class and specify the attributes to ‘introduction’
# method and print the attributes in same method.
class snake:
    def introduction(self,name,color,age):
        return f'Name:{name} Color:{color} Age:{age}'
obj=snake()
print(obj.introduction('kobra','red','23'))