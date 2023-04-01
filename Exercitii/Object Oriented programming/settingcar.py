class Car:
    """Representation of a virtual car."""

    def __init__(self): # constructor
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False
    
    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 100
    
    def start_engine(self):
        if not self.__engine_running:
            self.__engine_running = True

    def stop_engine(self):
        if self.__engine_running:
            self.__engine_running = False

    def drive(self, km):
        """1. verifica daca motorul functioneaza, daca nu exceptie
        2. verifici daca poti parcurge km, daca nu ai combustibil ridici exceptie
        3. daca ai combustibil sa parcurgi km, trebuie consumat conbustibilul 
    - consuml per km se calculeaza ca fiind __cmc / 1000
        """
        if not self.__engine_running:
            raise ValueError("Engine off. Turn it on")
        
        if not self.can_drive(km):
            raise ValueError("Not enough resources")
        
        self.__gas_in_tank -= self.get_consumption * km

        

    def refill(self, litters):
        if litters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank = litters
    
    def get_doors(self):
        return self.__doors
    
    def can_drive(self, km):

        _range = self.__gas_in_tank / (self.__cmc / 1000 * 4)
        
        if _range < km:
            return False
        
        return True
    

    def get_consumption(self):
        return (self.__cmc / 1000 * 4) + 0.5 * len(self.__passengers)

    def add_person(self, person):
        if len(self.__passengers) == self.__doors:
            raise ValueError("Not enough spaces left")
        self.__passengers.append(person)


class Person:

    def __init__(self):  # constructor
        self.height = 187 # cm
        self.weight = 0


vlad = Person()
maria = Person()

vw = Car()
ford = Car()


# print(f"CMC VW: {vw.__cmc}")
# print(f"CMC Ford: {ford.__cmc}")

# vw.__cmc = 3000

# print(f"CMC VW: {vw.__cmc}")
# print(f"CMC Ford: {ford.__cmc}")


print(vw.get_doors())
print(f"Combustibil ramas {vw.get_gas_percentage()} %")
vw.refill(12)
print(f"Combustibil ramas {vw.get_gas_percentage():.2f} %")