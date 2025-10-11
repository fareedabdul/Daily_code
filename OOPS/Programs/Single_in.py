class Bhaiya:
    Mom_name = "Abdul Shabana"
    
    def __init__(self,bike,home,fav_dish):
        self.bike = bike
        self.home = home
        self.fav_dish = fav_dish
class bhai(Bhaiya):
    
    def __init__(self,childrens,bike,home,fav_dish):
        super().__init__(bike,home,fav_dish)
        self.children = childrens
        
items = bhai(2,"Activa 6G","same","biryani")
# Checking values   
print(items.bike)       # Activa 6G
print(items.home)       # Same
print(items.fav_dish)   # Biryani
print(items.children)   # 2
print(items.Mom_name)
