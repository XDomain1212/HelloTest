class Person():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def say_hello(self):
        print(f'Hello, my name is {self.name}')

class Student(Person):
    def __str__(self):
        return 'Studen '+ super().__str__()
    def say_hello(self):
        print(f"Hey, I'm a student. My name is {self.name} . Hello !")


# person=Person('Lee Min')
# print(person)
# person.say_hello()

# student1=Student("Lee Min")
# print(student1)
# student1.say_hello()
# print(isinstance(student1,Student))
