#Lambda
'''square=(lambda x : x * x)
print(square(int(input("Enter number:"))))'''

#apply any operation to all elements we use map
'''numbers=[10,20,30,40,50,60]
result=map(lambda x : x*x,numbers)
print(list(result))'''

# apply filter based on condition
'''numbers=[1,2,3,4,5,6,7,8]
result=filter(lambda x: x%2==0,numbers)
print(list(result))'''

#apply reduce 

'''numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)'''


# File Handling 
'''with open("data.txt",'w')as f:
    f.write('Hello AGBE FAMILY')
    f.write('\nSql')
    f.write('\npython')
    f.write('\njava')'''


'''with open('AGBE/Day2/data.txt','r')as f:
    data=f.readlines()
print(data,len(data))'''


#Exception Handling
'''try:
    num1=int(input('enter:'))
    num2=int(input('enter:'))
    print(num1/num2)

except ZeroDivisionError :
    print('cant divide by zero')

finally:
    print('it will run either issue occured or not')'''


#Tuple


#Create a tuple using user input and print all its elements.
'''num=tuple(map(int,input().split(",")))
print (num)'''


#Write a program to unpack a tuple containing three values into three variables.
'''data=(10,20,30)
a,b,c=data
print(a)
print(b)
print(c)'''


#Given a tuple (10, 20, 30), change its second element to 50 by converting it to another data structure first.
'''tup=(10,20,30)
L1=list(tup)
L1[1]=50
tup=tuple(L1)
print(tup)'''

#Write a program to check whether two tuples are equal.
'''tup1=(10,20,30,40)
tup2=(10,20,40,40)

if tup1==tup2:
    print("equal")
else:
    print("not equal")'''


# Write a program to check whether all elements of one tuple are present in another tuple.
'''tup1=(10,40,50,30,20)
tup2=(10,20,50,30,20)
for i in range(0,5):
    if tup1[i]==tup2[i]:
        print("present")
    else:
        print("not present")'''


#Write a program to find the number of elements greater than a given value in a tuple.
'''tup1=[10,30,20,30,40,30,50,30]
target=int(input("Enter number:"))
count=0
for i in tup1:
    if i>target:
        count+=1
    
print(count)'''


#Write a program to find the number of unique elements in a list using a set.
'''num=[10,20,10,40,20,30]
unique=set(num)
print(unique)'''


#Given two sets, find the elements that are present in both sets without using a loop.
'''set1={1,2,3,4,5}
set2={3,4,5,6,7}
result=set1&set2
print(result)'''


#Given two sets, find all elements that are present in either set but not in both.
'''tup1=[10,20,30,5]
tup2=[50,6,30,5]
result=tup1 or tup2
print(result)'''


#Given a set of numbers, create a new set containing the squares of all elements
'''set1={1,2,3,4,5,6}
list1=list(set1)
sq=[i*i for i in set1]
set2=set(sq)
print(set2)'''





