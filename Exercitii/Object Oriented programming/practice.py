class Person:

    def __init__(self):
        self.__height = 1.72
        self.__weight = 85
        

    def get_height(self):
        return self.__height
    
    def get_heigthcm(self):
        return self.__height * 100

    

Georgica = Person()

print(int(Georgica.get_heigthcm()))