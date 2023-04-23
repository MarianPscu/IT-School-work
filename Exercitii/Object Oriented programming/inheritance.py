class Shape:

    def __init__(self, color,length) -> None:
        print("Hello din constructor Shape")
        self.color = color
        self.length = length

    def set_color(self, color):
        self.color = color

    # def __str__(self):
    #     return f"<{__class.__name__} color: {self.__color}>"

    def area(self):
         return self.length ** 2


class Square(Shape):

    def __init__(self, length, color = "red") -> None:
        super().__init__(color)
        self.length = length
        print("Hello din constructor Square")


class Triangle(Shape):
    
    def __init__(self, l1, l2, l3, color = "blue") -> None:
            self.l1 = l1
            self.l2 = l2
            self.l3 = l3
        
print("Hello din constructorul Triangle")

f1 = Square(5)
f1.set_color("blue")
print(f1.set_color)

print(f1.area)
print(Square.area)