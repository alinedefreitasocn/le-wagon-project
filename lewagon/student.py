from datetime import date

class Student:
    # class attribute
    # not related to the object, but a general class
    # characteristic. It can not be changed
    # it can only be called with the class Student,
    # not on the object, the variable, that you created
    # ex.: david = Student('david', 30)
    # david.name
    # => David
    # Student.school
    # => lewagon
    school = 'lewagon'

    # initializer of instance attributes
    # characteristics of the object
    def __init__(self, name, age): # Note the `self` parameter
        self.name = name.capitalize()
        self.age = age

    # instance method
    # actions that the object can perform
    def says(self, something):
        # x.f(y) equivalent to Class.f(x,y)
        print(f'{self.name} says {something}')

    # Class method
    # also related to the class, not to the object.
    # in this case, instead of initiating the object with
    # its age, you input the birth year and the class method
    # calculated the student age.
    # this is also called a method, but a class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Note the `cls` parameter
        return cls(name, date.today().year - birth_year)
