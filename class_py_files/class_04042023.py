"""
Inheritance

Using the properties of one cladss in another class

Types:
1. Single
2. Multiple
3. Multi Level
4. Hybrid
"""


class Vehicle:
    type = None


class Car(Vehicle):
    def __init__(self, make, model, year):
        self.model = model
        self.make = make
        self.year = year

    def get_info(self):
        print("CAR INFO: ")
        info = "Type: {}, Model: {}, Make: {}, Year: {}".format(self.type, self.model, self.make, self.year)
        print(info)




"""
Write a class called College
    - college name
    - college address
    - get_college_info()

class Student Inherited from College
    - student no,
    - student name
    - get_student_info()
    

Final output:
    - Print, college name, address, student nuo and name
    
"""


class College:
    def __init__(self, name, address):
        self.cname = name
        self.caddress = address

    def get_college_info(self):
        info = "College Name: {}, College Address: {}".format(self.cname, self.caddress)
        print(info)


class Student(College):
    def __init__(self, name, number, cname, caddress):
        super(Student, self).__init__(cname, caddress)
        self.sname = name
        self.sno = number

    def get_student_info(self):
        info = "Student Name: {}, Student No: {}".format(self.sname, self.sno)
        print(info)


class Lecturer(College, Student):
    def __init__(self, lname, subject):
        self.lname = lname
        self.subject = subject

    def get_lecturer_info(self):
        info = "College Name: {}, College Address: {}".format(self.name, self.address)
        print(info)


if __name__ == '__main__':
    c = Car("BMW", "X5", "2023")
    c.type = "Car"
    c.get_info()

    s = Student("Venkat", "100", "ABC", "XYZ")
    s.get_student_info()
    s.get_college_info()





