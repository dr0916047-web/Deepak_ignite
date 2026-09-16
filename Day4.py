#parametrized function
'''def classroom(name,marks):
    return (name,marks)
classroom("Rahul",15)'''

# *args
'''def college(age,*names):
    print(f"your age is:",age)
    for name in names:
        print(name)
    #print (age,name)
college (19,"Deepak","Rahul","Akash")'''

# *kwargs
'''def Profile(**kwargs):
    print(f"content type",type(kwargs))
    print(f"content present,{kwargs}")

    for key,value in kwargs.items():
        print(f"{key.capitalize()}:{value}")
Profile(name="Deepak",age=25,marks=95)'''



#Recursie function
'''def fact(n):
    if n==1:
        return 1
    else:
        return(n* fact(n-1))
fact(6)

def countdown(n):
    if n<=0:
        print ("blast off")
        return
    print(n)
    return (countdown(n-1))

countdown(3)'''

# Nested Function
'''def cal(a,b):

    def mul(x,y):
        return x*y
    return mul(a,b)

cal(10,20)'''

'''def outer (text):
    print("How are you")
    def inner ():
        return text
    return inner()
outer("I am fine")'''

# Function concept
'''def Calculator(a,b):
    while True:
        press=input()
        if press=='A':
            return a+b
        elif press=='B':
            return a-b
        elif press=='C':
            return a*b
        elif press=='D':
            return round(a/b,2)
        elif press=='E':
            return a%b
        elif press=='F':
            break
            
    
Calculator(20,15)'''


# Classes & Objects

'''class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

stu1 = Student()
stu2 = Student()

print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)'''


#constructor
'''class student:
    def __init__(self):
        print('Always call by default')

s1=student()
print(s1)'''

#Parametrized Constructor
'''class student:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

s1=student('Deepak','Data_Science')
print(s1.name," ",s1.subject)'''



'''class college:
    college='ABC College'
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
c1=college("Deepak","9cgpa")
print(c1.name,c1.gpa) '''



#Magic Methods in Python

'''Magic methods are special methods in Python that start and end with double underscores (__).

They are also called dunder methods (double underscore → dunder).'''

    




#Private acess (Encapsulation)
'''class employee:
    def __init__(self,salary):
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        self.__salary=new_salary

e=employee(50000)
print(e.get_salary())
e.set_salary(6000)
print(e.get_salary())
print(e._employee__salary)'''



#Inheritance (single level)
'''class school:
    #start_time='9AM'
    #end_time='6PM'
    def __init__(self,name):
        self.name=name

class Teacher(school):
    def __init__(self,subject,name):
        self.subject=subject
        super().__init__(name)

t1=Teacher('Data Science','Deepak')
print(t1.name,t1.subject)'''


# Inheritance(Multi level)
'''class Teacher:
    def __init__(self,salary):
        self.salary=salary

class student():
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher,student):
    def __init__(self,name,salary,gpa):
        self.name=name
        super().__init__(salary)
        student.__init__(self,gpa)
ta=TA('Deepak','10000','9')
print(ta.name,ta.salary,ta.gpa)'''


#Abstract method
'''from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('bark')

class cow(Animal):
    def make_sound(self):
        print("maao")

d=Dog()
c=cow()

d.make_sound()
c.make_sound()'''

# Polymorphism

# Example - Operator Overloading
'''print(1 + 2)    # adds 2 numbers
print("1" + "2") # concatenates 2 strings'''


# Function Overriding
'''class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
dog = Dog()

a.sound()  # Some generic sound
dog.sound()  # Bark'''






