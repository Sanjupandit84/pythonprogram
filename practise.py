# i =101
# while i>1:  # stoping condition
#     i-=1
#     print(i)

# n=int(input("enter number"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while  i< len(nums):
# # while  i< len(nums)+1:
#     print( nums[i])
#     # print( i*i)
#     i+=1


# i=1
# while i<=10:
#     if (i%2 != 0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# list = ['ram', 'shyam','chandu', 'mohit']

# for name in list:
#     if (name=='chandu'):
#         print('chandu found')
#         break
#     print(name)
# else:
#     print(
#         'end of code'
#     )


# nums=[1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)



# nums=[1,4,9,16,25,36,49,64,81,100]
# x=25
# idx=0
# for i in nums:
#     if(i==25):
#         print("num found at indx", idx)

#     idx+=1  

# for i in range(1,101):
#     print(i)
    

# for i in range(100,0, -1):
#     print(i)
    
# n= int (input("enter number"))
# for i in range(1,11):
#     print(n*i)

# for i in range(10):
#     pass

# print("sanjay")

# n=int(input("enter number to find sum of natural number : "))
# sum=0
# for i in range(1, n+1):
#     sum+=i
# print('sum of n num is ', sum)

# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# n=5
# fact =1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
    
    
    
    # now we are using function 
    
# def clc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum


# clc_sum(3,2)


# without passing an input , parameter, output

# def print_hell():
#     print('helloWprld')


# print_hell()


# def avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

# avg(5,5,3)
# avg(99,66,77)


x=["ram", "shyam","rohan","mohabat"]
m=["ramm", "ashyam","mrohan"]

def print_len(list):
    print(len(list))
    return 0


# print_len(x)
# print_len(m)


list=["ram", "shyam","rohan","mohabat"]

def print_element(list):
    for item in list:
        print(item , end=" ")
        
        
# print_element(list)



def print_fact(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
        
    print(fact)
        
# print_fact(5)



# usd to ins convertion 


def converter( usd, inr=83):
    
    inr=usd*inr
    
    print( usd ,"usd","=" ,inr,"inr " )


# converter(5)
# converter(1)

# wpa to find odd or even 

def odd_even(num):

    if num%2==0:
        print("number is even ")
        
    else:
        print("number is odd")

# odd_even(9)


# wpa to find sum of n num with recursive function 



def print_sum(n):
    if n==0:
        return 0
    return print_sum(n-1)+n


sum=print_sum(5)
# print(sum)


# waf using recursion to find factorial 


def cal_fact(n):
    if n==1 or n==0:
        return 1
    return cal_fact(n-1)*n
     
    
fact=cal_fact(5)
# print(fact)




list =["ram ", "shyam ", "mohit", "rsuresh"]

def idx_element(list, idx=0):
    
    if idx==len(list):
        return 
    
    print(list[idx])
    idx_element(list, idx+1)


# idx_element(list)
    
    
# learnig file  in python 

# f=open("sample.txt", "w")
# f.write("\nhy i am learning java  ")
# f.write("\nhy i am learning python, java  ")
# f.close()

# with i method 

# word ="python"
# with open ("sample.txt" , "r") as f:
#     data=f.read()
#     if word in data:
#         print('found')
#     else:
#         print (-1)
        
        #  with string find method 
        
# word ="mpython"
# with open ("sample.txt" , "r") as f:
#     data=f.read()
#     if(data.find(word) !=-1):
#         print('found')
#     else:
#         print ('not found')



# with open ("sample.txt", "r") as f:
#     data = f.read()

# new_data=data.replace("java","javascript")
# print(new_data)

# with open ("sample.txt", "w") as f:
#     f.write(new_data)



# def check_line_no():
#     word= "learning"
#     data=True
#     line=1
    
#     with open ("sample.txt","r") as f:
#         while data:
#             data=f.readline()
#             if word in data:
#                 print(line)
#                 line+=1



# def check_line_no():
#     word= "learning"
#     data=True
#     line=1
    
#     with open ("sample.txt","r") as f:
#         while data:
#             data=f.readline()
#             # if (word in data):
#             if (data.find(word)!=1):
#                 print(line)
#             line+1


# count=0
# with open ("practice.txt", "r") as f:
#     data=f.read()
#     nums=data.split(",")
#     for val in nums:
#         if (int(val) %2==0):
#             print(val)
#             count+=1
# print( "number of even value", count)



# class in python  


# class student :
#     name = "sanju"

# s1=student()
# print(s1.name)


# s2= student()
# print(s2.name)


# class car:
#     car_mdl="po25s66"
#     car_clr="red"

# c1=car()
# print(c1.car_mdl)
# print(c1.car_clr)

# c2=car()


# print(c2.car_clr)
# print(c2.car_mdl)




# class student:
#     def __init__(self, name):
#         self.name=name
        
# s1=student("ram")
# print (s1.name)


# s2= student("mohabat")
# print(s2.name)
    
    
    
    
# writing a class to print studetn name , and marks

# class student:
#     def __init__(self, name, marks):
#         self.full_name=name
#         self.marks=marks
        
   
# s1=student("ravii yadav", [55,88,99])

# print("student name  ", s1.full_name , "and  student marks is ", s1.marks)


# s2=student("sanju pandit", [88,99,77])
# print("student name ", s2.full_name , "and student marks is " , s2.marks)



# class student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
        
#     def welcome(self):
#         print("welecome", self.name)

#     def getmarks(self):
#         # print("student marks is ", self.marks)
#         return self.marks
        
        
# s1=student("raghupati", [55, 77, 88])
# s1.welcome()
# print (s1.getmarks())
# print(type(s1.marks))



# class student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
        
#     @staticmethod
#     def wellcome():
#         print("wellcome")
    
    
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum=sum+val
#         print("hi  ", self.name, "your avg score is ", sum/len(self.marks) )


# s1=student("ramnand", [88,77,66])
# print(s1.name, "your marks is ", s1.marks)

# s1.wellcome()
# s1.get_avg()

# s1.name="ironman"
# s1.get_avg()


# abstraction

# class car:
#     def __init__(self):
#         self.clutch =False
#         self.acc=False
#         self.brk=False
        
#     def car_start(self):
#         self.clutch=True
#         self.acc=True
#         print("car statrted.....")

# car1=car()
# car1.car_start()
# # print(car1.car_start())



# encapsulation

# class Account:
#     def __init__(self, bal, acc):
#         self.balance=bal
#         self.account=acc
        
#     def Account_debited(self, amount):
#         self.balance -=amount
#         print("Rs. ", amount, "debited")
#         print("total balance = ", self.get_balance())
        
#     def Account_credited(self, amount):
#         self.balance+=amount
#         print("Rs. ", amount, "credited")
#         print("Total balance = ", self.get_balance() )
        
        
#     def get_balance(self):
#         return self.balance
    
    
# a1=Account(1000, "abcd")
# a1.Account_credited(500)
# a1.Account_debited(400)

# class Password:
#     def __init__(self, name, pas):
#         self.name=name
#         self.__password=pas
        
#     def reset_pas(self):
#         print(self.__password)        
    
# p1=Password("raj", "abcd")

# print (p1.name)
# print (p1.reset_pas())


#  inheritaance ..........

# single inheritance......


# class car:
#     color='blue'
#     @staticmethod
#     def start():
#         print("car started.....")
    
#     @staticmethod
#     def stop():
#         print("car stoped......")
        
        
# class toyota_car(car):
#     def __init__(self, type):
#         self.type=type
        

# c1=toyota_car("desel")

# c1.start()
# c1.stop()
# print(c1.color)


# multilevel inheritance..........


# class university:
    
#     @staticmethod
#     def greating():
#         print("good mornig dear student" )
    
#     @staticmethod
#     def university_name():
#         print("IIT")
    
# class departement(university):
#     def __init__(self,subj_name):
#         self.subj_name=subj_name
    
# class student(departement):
#     def __init__(self, s_name, subj_name):
#         self.s_name=s_name
#         super().__init__(subj_name)
    
 
# s1=student("sanju", "DSA")
# s1.greating()
# print(s1.s_name)
# s1.university_name()
# print(s1.subj_name)



    
# multiple inheritance ...........


# class carA:
#     @staticmethod
#     def fortuner():
#         print("base model")
    
# class carB:
#     @staticmethod
#     def thar():
#         print('top model')
        
# class tata(carA,carB):
#     print("tata buy bothe one")
    

# t1=tata()
# # print(t1.fortuner())
# # print(t1.thar())
# t1.thar()
# t1.fortuner()


# class method..


# class person:
#     name="anonymous"
#     @classmethod
#     def changename( cls, name):
#         cls.name=name
    
# p1=person()
# p1.changename('raju')
# print(p1.name)
# print(person.name)


# @property method.....


# class student:
#     def __init__(self, math, chem, phy):
#         self.math=math
#         self.chem=chem
#         self.phy=phy

   
    
#     @property
#     def percentage(self):
#         return str((self.math+self.chem+self.phy)/3)+"%"
                
# s1=student(88,55,77)
# print (s1.percentage)
# s1.math=99
# print(s1.percentage)



# class complex:
#     def __init__(self, real, img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print (self.real, "i +", self.img, "j" )
        
#     def __add__(num, num2):
#         newReal= num.real + num2.real
#         newImg= num.img+num2.img
#         return complex(newReal,newImg)
    
    
    
# n1=complex(3,4)
# n1.showNumber()

# n2=complex(6,7)
# n2.showNumber()
# n3=n1.__add__(n2)
# # c3=c1.add(c2)   now we use donder method to print comple number using __add__
# n3.showNumber()

# f string .........
 
# name='sanjay'
# print(f"hello my name is {name}")



# calculating the are and perameter of the circle ....

# class circle:
#     PI=22/7
#     def __init__(self, radius):
#         self.radius=radius

#     def calculate_Area(self):
#         return self.PI*self.radius**2
    
#     def claculate_perameter(self):
#         return 2*self.PI*self.radius

# c=circle(21)
# print (c.calculate_Area())
# print (c.claculate_perameter())



# class Employe:
#     def __init__(self, role, dept, salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showDetaile(self):
#         print(' employe role = ', self.role)
#         print("employe dept = ", self.dept)
#         print("employe salary = ", self.salary)

    
# class engineer(Employe):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer", "IT", 80000)
        
# emp1=engineer("sanjay", 21)
# emp1.showDetaile()



# class order:
#     def __init__(self, item, price):
#         self.item=item
#         self.price=price

#     def __gt__(self,odr2):
#         return self.price>odr2.price
    
# odr1=order("chips", 20)
# odr2=order("biskut", 10)

# print(odr1>odr2)