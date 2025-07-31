class Person:
    pass

class Student(Person):
    pass

class Worker(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self, name):
        if name == 's':
            return Student()
        elif name == 'w':
            return Worker()
        else:
            return Teacher()

personFactory = PersonFactory()
worker = personFactory.get_person('w')
teacher = personFactory.get_person('t')
student = personFactory.get_person('s')