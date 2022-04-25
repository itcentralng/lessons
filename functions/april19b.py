class Student():
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

student1 = Student('Qasim Jibrilu', 15, 'Jamal International')
student2 = Student('Mohammad Bishir', 25, 'Alqalam International')
student3 = Student('Mustapha Abubakar', 16, 'Lessons Academy')

print(student1.name)
print(student2.name)
print(student3.name)

from april14 import get_years


class Student():
    def __init__(self, name, dob, level, school):
        self.name = name
        self.dob = dob
        self.school = school
        self.age = get_years(self.dob)
        self.classmates = []
        self.level = level 
    def add_classmate(self, student):
        """
        The add_classmethode takes student which is another object of the class Student
        """
        if self.school == student.school and self.level == student.level:
            self.classmates.append(student)
    def show_classmates(self):
        students = [student.name for student in self.classmates]
        students = ", ".join(students)
        return 'My classmates are: '+students

student1 = Student('Qasim Jibrilu', "1990-01-01", "Primary 2", 'Jamal International')
student2 = Student('Mohammad Bishir', "2000-10-01", "Nursery 1", 'Alqalam International')
student3 = Student('Mustapha Abubakar', "2002-02-14", "Primary 2", 'Jamal International')
student4 = Student('Kassandra Abubakar', "2002-02-14", "Primary 2", 'Jamal International')

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student3.name)
print(student3.age)
student1.add_classmate(student2)
student1.add_classmate(student3)
student1.add_classmate(student4)
print(student1.show_classmates())

# CLASS WORK

"""
(1) Create a class Person:
    (a) A person should have firstname, lastname, dob, state of origin.
    (b) The class should have a method add_hobby that can add a hobby to the person
    (c) The class should also have a method show_hobbies that return all the hobbies of that person
    (b) The class should have a method add_parent that can add a parent to the person
    (e) The class should also have a method show_parent that return all the parent of that person
    (f) The class should have a method add_sibling that can add a sibling to the person
    (g) The class should also have a method show_siblings that return all the siblings of that person
    (h) The class should have a status to determine whether the person is alive or not
    (i) A deceased sibling, or parent should not be displayed when the show_siblings or show_parent method is called
    (j) The class should have a methods that allow for other people to be added or removed as friends
(2) Create a class Car:
    (a) The constructor should take a model, brand, color, speed limit, chasis number, engine type and year
    (b) The class should have a method that when called will add cars of the same model and year together
    (c) The class should also have a method that shows all related cars
"""


print('Kassandrah')
class Person():
    def __init__(self,firstname,lastname,dob, state_of_origin,):
        self.lastname=lastname
        self.firstname=firstname
        self.dob=dob
        self.state_of_origin=state_of_origin
        self.hobbies=[]
        self.parents=[]
        self.siblings=[]
        self.dob = get_years(self.dob)
    def add_hobbies(self,hobby):
        self.hobbies.append(hobby)
        """
     The hobbies function takes in a hobby which is another object of the class Student
        """
    def show_hobbies(self):
        hobbies = ", ".join(self.hobbies)
        return f"{self.lastname}'s hobbies are {hobbies}"
    def add_parents(self,parent):
            self.parents.append(parent)
    """the add_parent function takes parent information of the specified person which is an instance 
        of the class person.
        """
    def show_parent(self):
        parents=[parent.firstname for parent in self.parents]
        parents=" , ".join(parents)
        return f"{self.lastname}'s parents are {parents}"
    def add_sibling(self,sibling):
        if self.lastname == sibling.lastname and self.state_of_origin == sibling.state_of_origin:
            self.siblings.append(sibling)
            sibling.siblings.append(self)
            for sibling in self.siblings:
                if sibling  not in self.siblings:
                 # add all siblings of self to sibling
                    sibling.siblings += self.siblings
                 # add all siblings of sibling to self
                    self.siblings += sibling.siblings
    def show_sibling(self):
        siblings = [sibling.firstname for sibling in self.siblings]
        siblings=" , ".join(siblings)
        return f"{self.firstname}'s siblings are {siblings}"

person1 = Person('Qasim ','Jibrilu', "1990-01-01", 'katsina')
person2=Person('kabirah','Jibrilu', "1995-01-01", 'katsina')
person3=Person('Jibrilu ','Qasim', "1999-06-17", 'kaduna')
person4=Person('Nasir ','Jibrilu', "1890-11-01", 'katsina')
person5=Person('Yasir ','Jibrilu', "1890-11-01", 'katsina')
print(person1.firstname)
print(person2.dob)
print(person3.firstname)
print(person4.dob)

person1.add_hobbies('Eating rice')
person1.add_hobbies('Running in the morning')
person2.add_sibling(person4)
person1.add_sibling(person2)
person2.add_sibling(person5)
print(person2.show_sibling())
print(person1.show_sibling())
print(person1.show_hobbies())

