class Student:
    school_name = " ABC school "
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no 
s1 = Student("emma",123)
print(s1.name , s1.roll_no , school_name)
s2 = Student("john",1234)
print(s2.name,s2.roll_no, school_name)
