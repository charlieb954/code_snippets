class Toyota:
    def __init__(self):
        # standard variable
        self.engine = 1.2
        # protected variable, should not be accessed directly, but nothing stops you except convention
        self._speed = 90 
        # private variable, harder to access but still possible
        self.__emissions = 1000

car = Toyota()
print(car.engine)
print(car._speed)
# this will error
#print(car.__emissions) 

# this will work and is name wrangling used to extract private variables. _CLASS__VARIABLE
print(car._Toyota__emissions) 