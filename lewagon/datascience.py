"""
Class inheritance from another py file
Good practice: Keep one class per .py file
"""
from student import Student

class DataStudent(Student):
    cursus = 'datascience'
    def __init__(self, name, age, batch):
        # the super gets all the atributes of the upper class
        super().__init__(name, age)
        # and this is the specific fro the class DataStudent
        self.batch = batch
