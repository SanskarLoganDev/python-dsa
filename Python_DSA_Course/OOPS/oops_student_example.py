class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # we have made an attribute where we have not passed any argument which is common and fine

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_avg_grade(self):
        value  = 0
        for student in self.students:
            value= value+ student.get_grade()
        return value/self.max_students # or return value/len(self.students)
    
s1 = Student("Logan", 19, 95)
s2 = Student("James", 18, 78)
s3 = Student("Marc", 20, 45)

course1 = Course("Science", 2)
course1.add_student(s1)
course1.add_student(s2)
# print(course.students) # students is an empty list defined in add_student() and this code displays the object location
print(course1.students[0].name) # s1 student can reference name from the student class
print(course1.get_avg_grade())
        