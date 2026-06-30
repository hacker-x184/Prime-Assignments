class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def set_name(self,name):
        if (name!=""):
            self.__name = name
        else:
            print("Name cannot be empty")
    
    def set_roll_no(self,roll_no):
        if(roll_no<=1 and roll_no<=100):
            self.__roll_no=roll_no
        else:
            print("Your Roll can't be less 0 and greater than 100")    

    def set_marks(self,marks):
        if (marks<0):
            print("marks can't be negative")
        else:
            self.set__marks = marks
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks