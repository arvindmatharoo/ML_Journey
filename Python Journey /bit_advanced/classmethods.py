import datetime
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def from_birthyear(cls,name,birth_year):
        current_year = datetime.date.today().year 
        age = current_year - birth_year 
        return cls(name,age)
person1 = Person.from_birthyear("John Doe",1990)
print(person1.age)