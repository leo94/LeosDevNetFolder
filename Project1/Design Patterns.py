"""
class ConfigValues:
    __instance = None
    
    @staticmethod
    def getInstance():
        if ConfigValues.__instance == None:
            ConfigValues()
        return ConfigValues.__instance
    
    def __init__(self):
        
        if ConfigValues.__instance != None:
            raise Exception("This Class is a Singleton")
        else:
            ConfigValues.__instance = self
            

s = ConfigValues.getInstance()
print(s)

s = ConfigValues.getInstance()
print(s)

"""

class Observer():
    def update(self, subject):
        print("Observer: My Subject just updated and told me about it")
        print("Observer: It's state is now - " + str(subject._state))
        
class Subject():
    _state = 0
    _observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
        
    def notify(self):
        
        print("Subject: I'm notifying my observers...")
        for observer in self._observers:
            observer.update(self)
            
    def updateState(self,n):
        
        print("Subject: I've received a state update!")
        self._state = n
        
        self.notify()

s = Subject()

obj1 = Observer()
obj2 = Observer()
obj3 = Observer()

s.attach(obj1)
s.attach(obj2)
s.attach(obj3)

s.updateState(5)