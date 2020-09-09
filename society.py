import math
from random import *

class Person:
    whole_society = []
    society_size = {"x":1300,"y":700}
    max_life = 70
    recent_time = 0
    time_passed = 0

    def __init__(self, **args):
        

        #Sets the ID
        if "id" in args:
            self.id= args["id"]
        else:
            self.id = len(Person.whole_society)+1
        #Sets the Age
        if "age" in args:
            self.age = args["age"]
        else:
            self.age = math.floor(Person.rangen()* Person.max_life)
        #Setes the sex
        if "sex" in args and (args["sex"]== "male" or args["sex"]=="female"):
            self.sex = args["sex"]
        else:
            if Person.rangen() > 0.5:
                self.sex = "male"
            else:
                self.sex= "female"
        #Sets the X Location
        if "x_locate" in args and args["x_locate"] <= Person.society_size["x"]:
            self.x_locate = args["x_locate"]
        else:
            self.x_locate = math.floor(Person.rangen()* Person.society_size["x"])
        #Sets the Y Location
        if "y_locate" in args and args["y_locate"] <= Person.society_size["y"]:
            self.y_locate = args["y_locate"]
        else:
            self.y_locate = math.floor(Person.rangen()* Person.society_size["y"])
        #Sets the Ralationship Status
        if ("relationship" in args) and (args["relationship"]== "married" or args["relationship"]== "single"):
            self.relationship = args["relationship"]
        else:
            if Person.rangen() > 0.5:
                self.relationship = "married"
            else:
                self.relationship= "single"
        
        Person.whole_society.append(self)


    # the class method to generate random numbers /// Could be modified for better later
    @classmethod
    def rangen(cls,**args):
        return random()
    
    def add_to_society(self):
        Person.whole_society.append(self)

    @classmethod
    def move_one_step(cls,**arg):
        Person.recent_time = Person.recent_time + 1
        recent_locations = []
        step_length = 10
        x = 0
        for any_person in Person.whole_society:
            recent_locations.append ( [any_person.id,any_person.x_locate, any_person.y_locate])
        for any_person in Person.whole_society:
            x= Person.rangen()
            if x*3 > 2:
                any_person.x_locate = any_person.x_locate + step_length
            if x*3 <2 and x*3 >1:
                any_person.x_locate = any_person.x_locate + 0
            if x*3 < 1 :
                any_person.x_locate = any_person.x_locate -step_length
            
            x = Person.rangen()
            if x*3 > 2:
                any_person.y_locate = any_person.y_locate + step_length
            if x*3 <2 and x*3 >1:
                any_person.y_locate = any_person.y_locate + 0
            if x*3 < 1 :
                any_person.y_locate = any_person.y_locate -step_length
        
        #just for debug must be deleted later
        return recent_locations

        #check of locations and modify must happen here


    def time_forward(self):
        Person.recent_time = Person.recent_time + 1
        Person.move_one_step()

