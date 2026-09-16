student={}
while True:
    press=int(input())
    if press==1:
        print('Add Student')
        Name=input('Enter name')
        marks=int(input('Enter marks'))
        student[Name]=marks
        print('submitted')

    elif press==2:
        print(f'student:{student}')

    elif press==3:
        Name=input('Enter name:').lower()
        if Name in student:
            print('Found')

        else:
            print('Not Found')

    elif press==4:
        Name=input('Enter name:')
        if Name in student:
            marks=int(input('Enter marks:'))
            student[Name]=marks
            print('updated marks')
        
    elif press==5:
        Name=input('Enter name:')
        del student[Name]
        print('deleted')

    elif press==6:
        total=0
        for Name,Marks in student.items():
            total+=Marks
        print(total)
    
    elif press==7:
        highest_marks=0
        topper=''
        for Name,marks in student.items():
            if marks>highest_marks:
                highest_marks=marks
                topper=Name
        print(f'Topper:{topper},{highest_marks}')
    
    elif press==8:
        total=0
        for Name,marks in student.items():
            total+=marks
            count = len(student)   
        print(f'total students:{count}')
        print(f'total marks:{total}')
        print(f'average:{total/len(student)}')
    
    elif press==9:
        break

    '''Project 2: Personal Expense & Budget Tracker
Create a console application to manage:

Income
Expenses
Categories
Budget
Balance
Expense analysis

===== PERSONAL EXPENSE TRACKER =====

1. Add Income
2. Add Expense
3. View Income
4. View Expenses
5. Calculate Balance
6. Search Expense
7. Category-wise Analysis
8. Set Budget
9. Check Budget
10. Show Statistics
11. Delete Expense
12. Exit'''



'''Income_list=[]
Expense_list=[]
while True:
    press=int(input())
    if press==1:
        print('Add Income')
        Income=[
        {
            'Source':input("Enter Source:"),
            'amount':int(input('Enter amount:'))
        }
    ]
        Income_list.append(Income)
        print('added')
        
    elif press==2:
        print('Add Expenses')
        Expenses=[
            {
                'categories':input("Enter Category:"),
                'amount':int(input('Enter spending:'))
            }
        ]
        Expense_list.append(Expenses)
        print('added')
    elif press==3:
        print(Income_list)
        

    elif press==4:
        print(Expense_list)

    elif press==5:
        Income_sum=0
        for i in range (len(Income_list)):
            Income_sum+=(Income_list[i][0]['amount'])
        print(Income_sum)
        Expense_sum=0
        for i in range (len(Expense_list)):
            Expense_sum+=(Expense_list[i][0]['amount'])
        print(Expense_sum)

        print(f'Balance amount:{Income_sum-Expense_sum}')
            

    elif press==6:
        category = input("Enter category: ")

        for i in range(len(Expense_list)):'''
    