# n = 6
# m =1 
# for x in range (6,0,-1):
#     m=m*x
#     print(m)

# n=5
# m=25
# if n == n%10:
#     print('automorphic number')
# else:
#     print('not automorphic number')

# for x in range(5,8):
#     for y in range(1,11):
#         print (x,'x',y,'=',x*y)
#     print()

# for x in range (1,250):
#     f_c=0
#     for i in range(1,x+1):
#          if x%i==0:
#             f_c+=1
#     if f_c==2:
#                   print('prime',x)
#     else:
#                  print('not prime')

# 

# a=1
# while a<=100 :
#     if a%1==0:
#         print(a)
#         a+=2

# s =234
# revers_num=0
# while s>0:
#     d=0%10
#     s//=10
#     revers_num=revers_num * 10 + d
# print (revers_num)

# h=11
# sum =0
# temp=h
# while h>0:
#     d=h%10
#     h//=10
#     sum+=d  
# if temp%sum==0:
#         print('harshad number')
# else:
#         print('not harshad number')


# h=[10,20,30,40]
# print (h[2])
   
# next while loop
# a=2

# while a<=20:
#     b=1

#     while b<=10:
#         print(f'{a} x {b} = {a*b}')
#         b+= 1
#     print()
#     a+= 1





# d= {'a':10, 'b':20, 'c':30}
# max1=0
# for x in d.items():
#     if x > = max1:
#         max1=x

# print(max1)

# d= {'a':10, 'b':20, 'c':30}
# # .values()))print(max(d
# print(min(d.values()))

# print('hello world')

# res= {}
# for x in range(1,11):
#     res[x]=x*x
# print(res)  

# res= {}
# for x in range(1,6):
#     res[x]=x*x*x
# print(res)
        
# def table (a):
#     for x in range(1,11):
#         print(f'{a} x {x} = {a*x}')
# table(12)
    
# def fact(n):
#     for x in range (1,n):
#         if x%n==0:
#             print(n)
# fact(10)


#1/6/26

# def check_prime(n):
#     if n>1:
#         print('prime')
#     else:      
#          print('not prime')
            
# check_prime(11)
        
    
# def string(a):
#     s =""
#     for x in a:
#         if "a"<= x <= "z" or "A" <= x <= "Z":
#             s+= x
#     print(s)
# string('hello123world')

# def string(a):
#     n=""
#     b='1,2,3,4,5,6,7,8,9,0'
#     while a>0:
#         d=a%10
#         a//=10
#         for x in range(len(b)):
#             if str(d) == b[x]:
#                 n+=b[x]
#     return n               
# print(string(12345)) 
# string(12345)



# def int(s):
#     n=0
#     r='123456789'
#     for x in s:
#      for y in range(len(r)):
#         if x == r[y]:
#             digit = y+1
#         n=n*10+digit
#     print(n)
#     print(type(n))
# int('12345')


# num =371
# sum=0
# temp=num
# while temp>0:
#     sum=sum+(temp%10)
# temp//=10
# if num%sum==0:
#     print('amnstrong number')
# else:              
#     print('not amnstrong number')



# def prime(n):
#     cou=0
#     for x in range(1,n+1):
#         if n%x==0:
#             cou+=1
#     if cou==2:
#             print('prime')
#     else:        
#             print('not prime')

# prime(13)


# def prime(n):
#     for x in range(1,10):
#         cou=0
#         for y in range(1,x):
#             if x%y==0:
#                 cou+=1
#     if cou==1:
#             print('prime',x)
#     else:        
#             print('not prime',x)  
# prime(7)

# i=[]
# def create_account():
#     new_account = {}
#     new_account['holdername'] = input('enter account holder name: ')
#     new_account['balance'] = 0
#     i.append(new_account)       
#     return new_account
    
#     def deposit():
#         name = input('enter account holder name: ')
#         for x in i:
#             if x['holdername'] == name:
#                 amount = int(input('enter amount to deposit: '))
#                 x['balance'] += amount
#             else:
#                 print('account not found')
#                 while True:
#                     print('1. create account')
#                     print('2. deposit')
#                     print('3. exit')

#  bank account code
# class BankAccount:
#     def __init__(self):
#         self.name = None
#         self.balance = 0.0

#     def create(self, name="ravi"):
#         self.name = name
#         self.balance = 0.0
#         print(f"Account created for {self.name} with balance {self.balance:.2f}")

#     def deposit(self, amount):
#         try:
#             amt = float(amount)
#         except Exception:
#             print("Invalid amount. Please enter a number.")
#             return
#         if amt <= 0:
#             print("Enter an amount greater than 0.")
#             return
#         if self.name is None:
#             print("No account exists. Create an account first (press 1).")
#             return
#         self.balance += amt
#         print(f"Deposited {amt:.2f}. New balance: {self.balance:.2f}")

#     def check_balance(self):
#         if self.name is None:
#             print("No account exists. Create an account first (press 1).")
#             return
#         print(f"Current balance: {self.balance:.2f}")

#     def show_details(self):
#         if self.name is None:
#             print("No account exists. Create an account first (press 1).")
#             return
#         print(f"Account holder: {self.name}\nBalance: {self.balance:.2f}")


# def menu():
#     acc = BankAccount()
#     while True:
#         print("\n--- Bank Menu ---")
#         print("1 - Create account (get ravi)")
#         print("2 - Deposit")
#         print("3 - Check balance")
#         print("4 - Show account details")
#         print("5 - Exit")
#         choice = input("Choose an option: ").strip()

#         if choice == "1":
#             acc.create("ravi")
#         elif choice == "2":
#             amt = input("Enter deposit amount: ").strip()
#             acc.deposit(amt)
#         elif choice == "3":
#             acc.check_balance()
#         elif choice == "4":
#             acc.show_details()
#         elif choice == "5":
#             print("Goodbye")
#             break
#         else:
#             print("Invalid choice. Enter 1-5.")


# if __name__ == "__main__":
#     menu()


# l = []

# def create_Account():
    
#     new_Acc = {}
    
#     new_Acc['HolderName'] = input('Enter Holdername:')  # sai
#     new_Acc['Account_num'] = int(input('Enter Account number:'))
#     new_Acc['Balance'] = 0
#     l.append(new_Acc)
    
#     print(l)
    
# def Deposit():
#     acc_num = int(input('Enter Account number:'))
#     Account_F = 0   #  1
#     for x in l:
#         if x['Account_num']==acc_num:
#             Account_F = 1
#             D_Amount = int(input('Enter Deposit Amount:'))
#             x['Balance']+=D_Amount
            
#     if not Account_F:
#         print('invalid Account number')
  
#     print(l) 
        
            
    


# while True:
#     print('''
#           1) Create Account 
#           2) Deposit
#           3) Exit''')
    
#     n = int(input('select 1/2/3/4:'))
    
#     if n==1:
#         create_Account()
        
#     elif n ==2:
#         Deposit()
        
#     elif n==3:
#         break
#     elif n==4:
#         print()
#     else:
#         print('account not found')
#         print(1)
# def create_Account():
#     print('account created')    
#     account_num = int(input('enter account number:'))
#     account_holder = input('enter account holder name:')
#     account_phonenumber = int(input('enter account phonenumber:'))
#     balance = 10000
#     account = {
#         'account_num': account_num,
#         'account_holder': account_holder,
#         'account_phonenumber': account_phonenumber,
#         'balance': balance
#     }
#     accounts.append(account)
#     print('account created successfully')   



# import string


# def add(*a):
#     sum = 0
#     for x in a:
#         if type(x) == string:
#             sum += x
#     print(sum)
# add(1,10,20,30,2,3,4,5,a,b,c,d)


# def employee(**k):
#     for x in k.items():
#         print(x)
# employee(name='ravi',age=30,designation='developer') 


# def employee(emp_id, emp_name, emp_age=22, emp_salary=35000):
#     print(f'Employee ID: {emp_id}')
#     print(f'Employee Name: {emp_name}')
#     print(f'Employee Age: {emp_age}')
#     print(f'Employee Salary: {emp_salary}')
# employee(101, 'Ravi',emp_age=29,)

# n=12
# i=[x for x in range(1,n) if n%x==0]
# print(i) 


# a=[x for x in range(1,100) if (x>1) and all(x%y!=0 for y in range(2,x))]
# print(a)

# r=[10,11,12,13]
# res=['even' if x%2==0 else 'odd' for x in r]
# print(res)


# r=[10,12,8,11]
# res=[[x for x in range(1,y)if y%x==0] for y in r]
# print(res)



# res=[x, x in range(1,20) if x%3==0 or x%5==0]
# print(res)

# n=12
# res=[x for x in range(1,n+1) if n%x==0]
# print(res)
# for x in d:
# Res=[x,spilt('.')[-1]]
# print(res)


# res=[x+y for x,y in zip([1,2,3], [10,20,30])]
# print(res)

# n=12
# r=(x for x in range(1,n) if n%x==0)
# print(list(r)) 
 
# res=[x for x in range (10,20)if all (x%y!=0) for y in range(2,x)]
#  print(res) 


# a=[1,2,3,4]
# b=[2,3,1,4]
# res=[(x,y) for x in a for y in b if x!=y]
# print(res)


# RES=[x for x in range(10,100) if str(x)==str(x)[::-1]]
# print(RES) 

# res=(x for x in range(10,100))
# for x in res:
#     print(next(res)) 


# res= tuple (x for x in range(10))
# for x in res:
#     print(res) 

# res=tuple(x for x in range(10)if x%2==0)
# print(res)

# res=tuple(x for x in range(1,10) if x%2!=0)
# print(res) 

# res=tuple(x for x in range(1,100) if x%3==0 and x%5==0)
# print(res)

# a=[10,11,12]
# b=[1,2,3]
# res= tuple(x*y for x in a for y in b)
# print(res)


# r={'a':10, 'b':20, 'c':30}
# res={v:k for k,v in r.items()}
# print(res)

# res={y:y*2 for y in range(1,10)if y%2==0}
# print(res)  

# res={x:{'s':x**2,'c':x**3}for x in range(1,10)}
# print(res)
#   

# h=[10,11,12,13]
# res={x:'even' if x%2==0 else 'odd' for x in h}
# print(res). 

# k=['a','b','c','d']
# v=[1,2,3,4]
# res={x:y for x,y in zip(k,v)}
# print(res)

# res=[x for x in range(10,20) if all (x%y!=0 for y in range(1,x))]
# print(res)

# 

# res={x:'prime' if all(x%y!=0 for y in range(2,x)) else 'not prime' for x in range(80,90)}
# print(res)


# res={x:list('even') for x in range(1,10) if x%2==0} + [x:list('odd') for x in range(10) if x%2!=0]}
# print(res)  


# player1 = input('enter player 1 name:')
# player2 = input('enter player 2 name:')
# import random
# for x in range(6):
#     for y in range(1,6):
#          print(f'{player1} rolls the dice: {random.randint(1,6)}')
#          print(f'{player2} rolls the dice: {random.randint(1,6)}')
        


