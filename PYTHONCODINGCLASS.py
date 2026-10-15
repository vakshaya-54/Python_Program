# file=input("enter the extention")
# match file:
#     case'py':print("python file") 
#     case'c':print("c file")
#     case'c++':print("c++ file")
#     case'html':print("html file")
#     case'jpg':print("jpeg file")
   
# for i in range(10):
#     print("Hello Ram")

# num=int(input("Enter number"))
# total=0
# for i in range(1,num+1):20
#     total=total+i
# print(total) 

# num1=int(input("Enter Fnumber:"))
# num2=int(input("Enter Snumber:"))
# totals=0
# for i in range(num1,num2+1:)
#     if i%2==0;
#        totals+=i
#     print(totals)

# num=5
# totals=0
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# number=int(input())
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
#     print(i,end="")
#     if i<number:
#         print("*",end="")
# print("=",fact) 

# n=int(input())
# digits=0
# total=0
# while n!=0:
#     rem=n%10
#     digits+=1
#     total=total+rem
#     n=n//10
# print("no of digits:",digits)
# print("sum of digits:",total)

# num=int(input())
# while not (num>=0 and num<=9):
#     sums=0
#     while num!=0:
#         rem=num%10
#         sums=sums+rem
#         num=num//10
#     num=sums
# else:
#     print(num)
#AMSTRONG NUMBER
# num=int(input())
# digits=0
# temp=num
# temp1=num
# while num!=0:
#     digits+=1
#     num//=10
# sums=0
# while temp!=0:
#     rem=temp%10
#     sums=sums+rem**digits
#     temp=temp//10
# if temp1==sums:
#     print("amstrong number")
# else:
#     print("not a amstrong number")
     
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#      print("not a prime number ")


# for i in range(1,11):
#     if i==6:
#         break
#     print(i,end=" ")
# print()
# for i in range(1,11):
#     if i==6:
#         continue
#     print(i,end=" ")

# if True and False:
#     pass
# else:
#     print("javascript")

# n=int(input())
# a=n-1
# b=1
# for i in range(1,n*2):
#     for j in range(1,a+1):
#         print(" ",end=" ")
#     for k in range(1,b+1):
#         print("*",end=" ")
#     print()
#     if i>=5:
#         a+=1
#         b-=2
#     else:
#         a-=1
#         b+=2

# for i in range(5,0,-1):
#     print("*" * i)

# for i in range(2,6):
#     print("*" * i)   

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(2,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#List ordered mutable allow duplicate
# list_1=[24,56,78,9,0,23,23]
# list_2=["Jagan","Kumar","Navin","Praveen"]
# list_3=["Naveen",18,"M",9.8,"RGCET",True]
# print(list_1)
# print(list_2)
# print(list_3)
# print(type(list_1))
# list_4=[10,20,30,40]
# list_4[2]=300
# print(list_4)

# numbers=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     numbers.append(data)
# print(numbers)
 
# list_5=[1,2,3,4,5]
# print(list_5)

# for data in list_5:
#     print(data,end=" ")
# print()
# i=0 #1<5
# while i<len(list_5):
#     print(list_5[i],end=" ")
#     i+=1
# print()
# list_6=[1,2,3,4,5]
# list_6.append(6)
# list_6.append(7)
# print(list_6)
# list_6.insert(0,1000)
# print(list_6)

# list_7=[10,20,30,40,20,30]
# list_7.remove(30)
# print(list_7)
# list_7.pop()
# print(list_7)
# list_7.clear()
# print(list_7)

# print("index")
# list_7=[10,20,30,40,20,30]
# print(list_7[4])
# print(list_7[-4])

# list slicing
# nums=[10,20,30,40,50,60]

# print(nums[1:4])
# print(nums[:3])
# print(nums[3:])
# print(nums[::2])
# print(nums[-3:])
# print(nums[::-1])
# print(nums[:])

# nums_1=[10,30,40,10]
# print(10 in nums_1)
# print(nums_1.count(10))
# print(nums_1.index(30))

# nums_2=[32,78,12,0,-9]
# nums_2.sort()
# print(nums_2)
# nums_2.sort(reverse=true)
# print(nums_2)

# nums_3=[4,3,2,1]
# nums_3.reverse()
# print(nums_3)

# nums_4=[56,78,2,3,6,9,4,5,1,2,90,45,23,78,90,345,12]
# print(len(nums_4))
# print(sum(nums_4))
# print(min(nums_4))
# print(max(nums_4))

# two sum
# nums=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     nums.append(data)
# target=int(input())
# found=False
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             print(f"{i} , {j}")
#             found=True
#             break
#         if found:
#             break
# if not found:
#     print("-1 , -1")

#ordered immutable allow duplicate
# tuple_1=(34,67,89,23)
# print(tuple_1)
# print(type(tuple_1))

# tuple_2=(5,)
# print(type(tuple_2))

# tuple_3=(12,45,67,89,23)
# for data in tuple_3:
#     print(data,end=" ")
# print()
# i=0
# while i<len(tuple_3):
#     print(tuple_3[i],end=" ")
#     i+=1
# print()
# tuple_4=(1,2,3,2,3,1)
# print(tuple_4.count(3))
# print(tuple_4.index(3))

# print(len(tuple_4))
#  print(sum(tuple_4))
#  print(min(tuple_4))
#  print(max(tuple_4))

#  tuple_1 = (10, 20, 10, 30, 20, 40)
#  for num in set(tuple_1):
#      if tuple_1.count(num) > 1:
#         print(num)

# student1={
#     "name":"naveen",
#     "age":20,
#     "mark":459,
#     "dept":"ece"
# }
# print(student1)
# print(student1["name"])
# print(student1["age"])
# print(student1.get("mark"))
# print(student1.get("city","Not applicable"))
# student1["mark"]=499
# print(student1)
# student1["city"]="pondy"
# print(student1)
# student1.pop("age")
# print(student1)

# for a,b in student1.items():
#     print(a," :",b)

# name="naveen"
# dept='python'
# print(name)
# print(dept)
# print(dept[0])
# print(dept[1])
# print(dept[-1])
# #pyt
# print(dept[:3])
# #thon
# print(dept[2:6])
# #pyth
# print(dept[0:4])
# #nohtyp
# print(dept[::-1])

# a="Python" #1000
# a="J"+a[1:]
# print(a)
# print(len(a))
# for ch in a:
#     print(ch,end=" ")
# print()
# text="Java Programming"
# print(text.upper())
# print(text.upper())
# print(text.lower())
# print(text.replace("Java","Python"))
# print(text.count('a'))
# print(text.find("Programming"))
# print(text.find("C"))
# print(text.startswith("Java"))
# print(text.endswith("Programming"))

# text1="                 Java Programming               "
# print(text1.strip())
# text2="java python nodejs"
# courses=text2.split()
# print(courses)

# text3=["python","java","c++"]
# text4=",".join(text3)
# print(text4)

# def greet(): #function def
#     print("hi jagan")
# greet() #function calling 
# greet()


# def addition(a,b):
#     print(a+b)

# addition(5,6)
# addition(100,200)
# addition(200,300)

# def multiplication(a,b,c):
#     return a*b*c

# result=multiplication(5,5,5)
# print(result)
 
# #global variable and local variable

# def college():
#     text="message" #local variable
#     print(text)
# college()

# message="Hello" #Global variable
# def google():
#     print(message)
# google()
# print(message)

# def greet(n):
#     if n==0:
#         return
#     print(num,end=" ")
#     counts(num+1)
# counts(1)
# print()
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input())
# result=factorial(n)
# print(result)


# a=0
# b=1
# print(a," ",b,end=" ")
# for i in range(3,11):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
# print()
# def fib(num):
#     if num==0 or num==1:
#         return num
#     return fib(num-1)+fib(num-2)

# num=int(input())
# print(fib(num))

#lambda function
#lambda arguments:expression
# import math 
# from math import sqrt
# import Calculator
# addition=lambda a,b:a+b 
# print(addition(4,3))
# square=lambda a:a*a 
# print(square(5))

# modules and packages
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pi)

# print(Calculator.multi(5,5,5))

# Exception handling
# try:
#     a=int(input())
#     b=int(input())
#     c=a/b
#     print(c)
# except zerodivitionerror:
#     print("please enter positive number")
# except valueError:
#     print("entert integer only")
# except 

# class studenttwo:
#     name="unknown"
#     mark=0
#     def display(self):
#         print(self.name," ",self.mark)

# class studentone:
#     name="Aravindkumar"
#     age=20
#     dept="cse"
#     def marks(self):
#         print("Maths:90, English=78")

# class studentthree:
#     name="unknown"
#     mark=0
#     def__init__(self,name,mark)
#         self.name=name 
#         self.mark=mark 

# def setdetails(self,name,mark):
#    self.name=name
#   self.mark=mark
# def printdetails(self)
#     print(self.name," ",self.mark) 


# s1=studentone()
# print(s1.name)
# print(s1.age)
# s1.marks()

# s2=studenttwo()
# s2.name="deetshana"
# s2.mark=345
# s2.display()
# s3=studenttwo()
# s3.name="Akshaya"
# s3.mark=456
# s3.display()

# s4=studentthree("kumar",34)
# s4.setdetails("santhosh",500)
# s4.printdetails()

# class device:
#     def power_on(self):
#         print("Device swithched on")
# class Phone(Device):
#     def call(self):
#         print("Making a phone call")
# samsung=Phone()
# samsung.power_on()
# samsung.call()
# print()
# #multilevel inheritance -> Grandparent ->parent-> son
# class Device:
#     def power_on(self):
#         print("Device switched on")
# class computer(Device):
#     def run_Program(self):
#         print("Running a python program")
# class Laptop (Computer):
#     def charge(self):
#         print("Laptop battery charging")
# asus=Laptop 
# asus.power_on()
# asus.run_Program()
# asus.charge()
# print()
# #Multiple Inheritance one child class multiple parent class
# class camera:
#     def take_photo(self):
#         print("Taking a photo")
# class Musicplayer:
#     def play_music(self):
#         print("Playing music")
# class Smartphone(Camera,Musicplayer):
#     def call(self):
#         print("making a phone call")
# mi=Smartphone()
# mi.call()
# mi.take_photo()
# mi.play_music()

# class Device:
#     def power_on(self):
#         print("device switched on")
# class phone(Device):
#     def call(self):
#         print("making a phone call")
# samsung=phone()
# samsung.power_on()
# samsung.call()
# print()
# #multilevel inheritance -> grandparents ->parents->son

# class Device:
#     def power_on(self):
#         print("device is switched on")
# class computer:
#     def run_program(self)
#         print("running a python program")
# class laptop(computer):
#     def charge(self):
#         print("laptop battery charging")
# asus=laptop()
# asus.power_on()
# asus.run_program()
# asus.charge()
# print()
# # multiple inheritance one child class multiple parent class

# class camera:
#     def take_photo(self)
#         print("taking a photo")
# class MusicPlayer:
#     def play_music(self):
#         print("playing music")
# class SmartPhone(Camera,MusicPlayer):
#     def call(self):
#         print("making a phone call")
# mi=Smartphone()
# mi=call()
# mi=take_photo()
# mi=play_music()

# class Phone:
#     def camera(self):
#         print("taking a normal photo"):
# class smartphone(Phone):
#     def camera(self):
#         print("taking a potrait photo")
# samsung=samsung()
# samsung.camera()
# nokia=phone()
# nokia.camera()
# #encapsulation

# class bank:
#     __amount=800
#     def printamount(self):
#         retuen self.__amount
# hdfc=bank()
# print(hdfc.printamount())
# #Abstraction - hiding the internal details and showing only essential
# #features
# from abc import ABC,abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(payment):
#     def pay(self):
#         print("payment done using phonepe")
#         payment=UPI()
#         payment.pay()
#         payment=phonepe()
#         payment.pay()

