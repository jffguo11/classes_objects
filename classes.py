import random
# name = raw_input("What is your name?")

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1,self.sides + 1)
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

class exampleClass:
    eyes = "brown"
    age = 22
    def firstMethod(self):
        return "the first method has self as an argument"
    
class class_name:
    def __init__(self, name):
        self.createName(name)
        self.displayName()
        self.saying()
        
    def createName(self, name):
        """ Self is created here as a placeholder, referring to the object
        because we do not yet know what the object is going to be """
        self.name = name
    
    def displayName(self):
        return self.name
    
    def saying(self):
        print "hello %s" %self.name

class student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        
    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours
    
    def getQPoints(self):
        return self.qpoints
        
    def gpa(self):
        GPA = self.qpoints / self.hours
        return GPA

class mom:
    var1 = "this is mom"
    
class dad:
    var2 = "this is dad"
    
class child(mom, dad):
    var3 = "this is new variable"
childObject = child()
print childObject.var1
print childObject.var2
print childObject.var3


        
    
    
    
    
    
    