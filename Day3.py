#List
'''Q.1 Write a Python program to find the largest and smallest element in a list without using max() or min().
'''
'''l=[20,30,10,15,50,40]
a=l[0]
b=l[0]
for i in l:
    if i>a:
        a=i
for i in l:
    if i<b:
        b=i
print(a)
print(b)'''

'''Q.2 Write a Python program to find the second largest element in a list without using sort().'''
'''l1=[20,30,10,15,50,40]
largest = max(l1)
l1.remove(largest)
second_largest=max(l1)
print(second_largest)'''


'''Q.3 Write a Python program to remove duplicate elements from a list without using set().'''
'''L=[20,10,10,15,15,40]
L.sort()
new_list=[]
for i in range(len(L)):
    if L[i] not in  new_list:
        new_list.append(L[i])
print(new_list)'''  

'''Q.4 Write a Python program to count the frequency of each element in a list.'''
'''L=[10,20,10,20,30,40,50,50,60]
freq={}
for i in L:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq) '''


# Q.5 Given a list containing positive and negative numbers, move all negative numbers to the beginning and positive numbers to the end.
'''num=list(map(int,input().split(" ")))
l1=[]
l2=[]
for val in num:
    if val>=0:
        l2.append(val)
    else:
        l1.append(val)
final=l1+l2
print(final)'''


'''ls =[2,7,4,3,5,8]
target=10
for i in range (len(ls)):
    for j in range (i+1,len(ls)):
        if ls[i]+ls[j]==target:
            print((ls[i],ls[j]))'''



# DICTIONARY


#1.Given a dictionary containing student names and marks, find the student with the highest marks without using max().
'''students = {
    "Deepak": 70,
    "Rahul": 80,
    "Ashok": 110,
    "Kamlesh": 100
}
highest_marks=0
top_student=""
for name,marks in students.items():
    if marks>highest_marks:
        highest_marks=marks
        top_student=name
print(f"{highest_marks},{top_student}")'''


#2.Given a dictionary of numbers, calculate the sum of all values without using sum().
'''dict1={
    "num1":10,
    'num2':20,
    "num3":30,
    "num4":40
}
sum=0
for i in dict1.values():
    sum+=i
print(sum)'''


#3. Given a dictionary containing numbers as values, create a new dictionary containing only the **key-value pairs where the value is even**
'''dict1={
    "Num1":10,
    "Num2":15,
    "Num3":30,
    "Num4":25
}
dict2={}
for key,value in dict1.items():
    if value%2==0:
        dict2[key]=value
print(dict2)'''


#Q.4. Given a dictionary of student marks, count how many students **scored above 60**. 
'''dict1={
    "Rahul":40,
    "Deepak":50,
    "Ashish":60,
    "Mehak":100,
    "ashwin":80
}
count=0
for marks in dict1.values():
    if marks>=60:
        count+=1
print(count)'''


# 5. Given a dictionary, find the **key associated with the smallest value** without using `min()`.
'''dict1={
    "Num1":10,
    "Num2":5,
    "Num3":2,
    "Num4":3
}
min_key="Num1"
target=dict1["Num1"]

for key,value in dict1.items():
    if value < target:
        target=value
        min_key=key
print(min_key)'''


#7. Given a dictionary of employee names and salaries, calculate the **average salary** without using `sum()`
'''dict1={
    "A":100,
    "B":500,
    "C":200,
    "D":300
}
sum=0
for value in dict1.values():
    sum+=value
avg=sum/len(dict1)
print(avg)'''


#8.Given a dictionary, create a new dictionary by **swapping its keys and values**.
'''dict1={
    "A":100,
    "B":500,
    "C":200,
    "D":300
}
swapped={value:key for key,value in dict1.items()}
print(swapped)'''




