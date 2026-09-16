
#Regular Expression=A Regular Expression is used to search, match, validate, or extract text patterns from strings.
#Python provides the re module.
'''import re

text='I am a python developer'

result=re.search('python',text)

print(result)'''


'''import re

text = "I have 10 apples and 20 oranges"

numbers = re.findall(r"+", text)

print(numbers)'''

#@property is used when we want to access a method like an attribute.

# It is commonly used for encapsulation and controlled access to data.

'''class student:
    def __init__(self,name,age):
        self.name=name
        self._age=age

    @property
    def age(self):
        return self._age

s=student('Deepak',24)
print(s.age)'''

# Setter
'''class student:
    def __init__(self,name,age):
        self.name=name
        self._age=age

    @property
    def age(self):
        return self._age

    @age.setter

    def age(self,value):
        if value<0:
            print('enter a valid value')

        else:
            self._age=value

s=student('Deepak',25)
print(s.age)
s.age=20
print(s.age)'''


#private just for revise
'''class salary:
    def __init__(self,salary):
        self.__salary=salary

    def get(self):
        return self.__salary

    def set(self,new_salary):
        self.__salary=new_salary

s=salary(50000)
print(s.get())
s.set(60000)
print(s.get())'''

#A named tuple is like a tuple where we can access values using names instead of indexes.
'''from collections import namedtuple

student=namedtuple('students',['name','age','city'])
s=student('Deepak','age','jaipur')

print(s.name)
print(s.age)
print(s.city)'''


# Counter is used to count how many times each item occurs.

# It comes from the collections module.

'''from collections import Counter

student=[1,1,2,3,3,3,2,4]

result=Counter(student)
print(result)

text='banana'
result1=Counter(text)
print(result1)'''


#Double Ended Queue

#It allows us to add and remove elements from both ends

'''from collections import deque
student=[10,20,30,40,50]
d=deque([10,20,30,40,50])
d.append(60)
d.appendleft(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)'''


#defaultdict is similar to a normal dictionary, but it provides a default value when a key doesn't exist.

#from collections import defaultdict

'''data=defaultdict(int)
print(data['Name'])'''


#Counting
'''count=defaultdict(int)

words=['apple','banana','apple','banana','grapes','grapes','apple']

for word in words:
    count[word]+=1

print(count)'''


#Creating list in dictionary

'''students=defaultdict(list)

students['python'].append('Rahul')
students['python'].append('Deepak')
students['java'].append('Rishi')
print(students)'''

#OrderedDict is a dictionary from the collections module that provides operations specifically related to maintaining/manipulating key order.

from collections import OrderedDict

'''data=OrderedDict()
data['name']='Deepak'
data['age']=24
data['sunject']='python'

print(data)'''

'''data=OrderedDict([
    ('A',1),
    ('B',2),
    ('C',3)
])
data.move_to_end('A')
print(data)
data.move_to_end('A',False)
print(data)'''


'''import re

text= "My phone number is 9876543210"

result=re.search(r"\d+",text)

print(result.group())'''

'''import re 

email='abc@gmail.com'

pattern=r"[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern,email):
    print("valid email")

else:
    print('Invalid email')'''







    
        