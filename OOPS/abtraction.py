from abc import ABC, abstractmethod

class EntryDoor(ABC):   
    @abstractmethod
    def MainDoor(self):
        pass
    def Gate(self):
        print("aja bhai")
    
class FirstDoor(EntryDoor):
    def MainDoor(self):
        print("Entered the First Door")

class SecondDoor(EntryDoor):
    def MainDoor(self):
        print("Entered the second door")
        
obj = SecondDoor()
obj.MainDoor()  
obj.Gate()