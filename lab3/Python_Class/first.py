class StringOperations:
    def __init__(self, name = None, age = None):
        self.__name = name 
        self.__age = age

    def clear(self):
        self.name = None
        self.age = None



    
meowing = StringOperations('Tamirlan', 18)
print(meowing.__name)
meowing.clear()
print(meowing.name)