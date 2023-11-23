#!/usr/bin/python3
"""Module of a class that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all([type(i) == str for i in attrs]):
            dico = {}
            for i in self.__dict__:
                if i in attrs:
                    dico[i] = self.__dict__[i]
            return dico

        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
