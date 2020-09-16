class BaseHouse:
    def __init__(self, bedrooms):
        self.bricks = True
        self.mortar = True
        self.bedrooms = bedrooms
        
    def __repr__(self):
        return f"Bricks = {self.bricks}\nMortar = {self.mortar}\nBedrooms = {self.bedrooms}"
        
class SemiDetachedHouse(BaseHouse):
    def __init__(self, bedrooms, addr = None):
        self.semi_detatched = True
        self.addr = addr
        super().__init__(bedrooms)
        
    def __repr__(self):
        return f"Address = {self.addr}\n" + super().__repr__() + f"\nSemi Detatched = {self.semi_detatched}"
        
        
h = BaseHouse(2)
print(h)

print('\n\n')

h2 = SemiDetachedHouse(2, addr = "Test Avenue")
print(h2)