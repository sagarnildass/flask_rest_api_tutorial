class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod  #see below why we changed it to a classmethod
    def friend(cls, origin, friend_name, salary):
        #return a new student called friend_name in the same school as self (The below line will return an error when called from WorkingStudent
        #because WorkingStudent now does not have access to the self. So we will have to create an origin to specify where it comes from )
        return cls(friend_name, origin.school, salary)

#sagar = Student('sagar', 'JU')
#friend = sagar.friend('souvik')

#print(friend.name)
#print(friend.school)

#class WorkingStudent has all the stuffs that Student contains (Inheritance)
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        #now here one thing we can do is copy paste the Student's init + additional stuffs like this:
        '''
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary'''
        #but we don't need to as this class inherits all the properties automatically. So we call the __init__ method of Student with the super() keyword like this:
        super().__init__(name, school)
        self.salary = salary

sagar = WorkingStudent('sagar', 'JU', 250000)
# This will not work - friend = sagar.friend('souvik')
friend = WorkingStudent.friend(sagar, 'souvik', 200000)
print(sagar.salary)
print(friend.salary)
