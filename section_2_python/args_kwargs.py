#We can pass in unlimited numbers to sum them with the keyword *args
def addition_simplified(*args):
    return sum(args)

print(addition_simplified(2+3))
print(addition_simplified(2+3+4+5+6))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

#This returns
#(2,3,4) and {}. So Kwargs is a set
what_are_kwargs(2,3,4)
#This returns first three as args and last two named arguments as kwargs
what_are_kwargs(2, 3, 4, name='sagar', location='kolkata')

#SO now we can change our inheritance code like This
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod  #see below why we changed it to a classmethod (*args can take any number of arguments here. Here it takes salary.The advantage is
    #that now we can add additional parameters to the __init__ method of WorkingStudent class on the fly like job_title)
    #we could also have made it keyword argument or kwargs. But then we would have to pass salary=x, job_title=y
    def friend(cls, origin, friend_name, *args):
        #return a new student called friend_name in the same school as self (The below line will return an error when called from WorkingStudent
        #because WorkingStudent now does not have access to the self. So we will have to create an origin to specify where it comes from )
        return cls(friend_name, origin.school, *args)

#sagar = Student('sagar', 'JU')
#friend = sagar.friend('souvik')

#print(friend.name)
#print(friend.school)

#class WorkingStudent has all the stuffs that Student contains (Inheritance)
class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        #now here one thing we can do is copy paste the Student's init + additional stuffs like this:
        '''
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary'''
        #but we don't need to as this class inherits all the properties automatically. So we call the __init__ method of Student with the super() keyword like this:
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

sagar = WorkingStudent('sagar', 'JU', 250000, 'Python Data Scientist')
# This will not work - friend = sagar.friend('souvik')
friend = WorkingStudent.friend(sagar, 'souvik', 200000, 'R Data Scientist')
print(sagar.salary)
print(friend.salary)
print(sagar.job_title)
print(friend.job_title)
