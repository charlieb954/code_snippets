from abc import abstractmethod, ABC
class Toyota(ABC):
    def __init__(self, engine_size, colour):
        self.engine_size = engine_size
        self.colour = colour

    @abstractmethod
    def drive(self):
        pass
    
    def stop(self):
        return "Car is stopping"

class Yaris(Toyota):
    def __init__(self, engine_size, colour):
        super().__init__(engine_size, colour)
        self.bluetooth = True
        
    def __repr__(self):
        return f"Engine = {self.engine_size}\nColour = {self.colour}"

    def drive(self):
        '''
        As drive is an abstractmethod in the parent class there must 
        be one in the child class else there will be an error.
        '''
        return "The Yaris is driving"

yaris = Yaris(1.33, 'blue')
print(yaris)
print(yaris.drive())
print(yaris.stop())

# An interface is a class where all the methods are abstractmethods as below
class Rav4(Toyota):
    def __init__(self, engine_size, colour):
        self.engine_size = engine_size
        self.colour = colour

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass