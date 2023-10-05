"""num = 1
bool = True
stri = "word"
print (num)
print (bool)
print (stri)
bool = False
print (bool)
num1 = 1
num2 = 2
num3 = 3
num1 = num3
num2 = num1
print (num2)
print (num1)

def __init__ (self, name, age):
    self.name = name
    self.age = age
    
def myfunc(self):
    print(self.name)

people = {
    "Rob": 11,
    "Jeff": 9
}

import json 
string = {"name": "Jeff", "age": "8"}

x = 5 
print(type(x))
print (dir(x))"""



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_people(people):
    for person in people.values():
        print(f"Name: {person.name}, Age: {person.age}")

def find_old(people_dict):
    if not people_dict:
        print("The dictionary is empty.")
        return

    oldest_person = max(people_dict, key=lambda x: people_dict[x])

    print(f"The oldest person is {oldest_person} with age {people_dict[oldest_person]}")

people_list = {
    "kid1": Person("kid1", 1),
    "kid2": Person("kid2", 2),
    "kid3": Person("kid3", 3)
}

print_people(people_list)

people_dict = {"kid1": 1, "kid2": 2, "kid3": 3}
find_old(people_dict)

