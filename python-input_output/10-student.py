#!/usr/bin/python3
"""Module of a class that defines a student"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all([type(i) == str for i in attrs]):
            dico = "{"
            for count, i in enumerate(self.__dict__):
                if i in attrs:
                    dico += f"'{i}': {self.__dict__[i]}"
                    if (count + 1) != len(self.__dict__):
                        dico += ","
            dico += "}"
            return dico

        return self.__dict__

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)