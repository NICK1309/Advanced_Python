'''
# Day 01
# Program No. 01 
class Student:
    roll_number = 101 # data members
    num1= 50    # data members
    num2 = 100   # data members

    def add(self):  #member function
        print(self.num1+self.num2) #150
        self.name = input("Enter name:")  
        print(self.name)
obj = Student() # creating a object of class and we always create 
obj.add()
print(obj.roll_number)
#------------------------------------------------------------------
# Program No. 02
class HOD:
    def __init__(self): #constructor
        self.name='Priyank Sharma'  # data member 2 byte
        self.age = 22  # 4 byte
        self.empid = 101 # 6 byte total = 12 byte

    def info(self):  # instance method
        print("My name is :",self.name)
        print("My age is : ",self.age)
        print("My emp id:", self.empid)

obj = HOD() # object create
obj.info()        
'''
#------------------------------------------------------------------
# Program No. 03
'''
class Manipulation:
    Task: 1.simple interest
          2.factorial
          3.fibonacci series

    you have to create 3 diffrent functions
    create a constructor (declare all the datamembers here create a function to accept the value for data members getdata() 
    3.create a function to only display the results of simpleinterest factorial,fibonacci series 
    display data

# class Manipulation:
#     principle = int(input("Enter the principle amount : "))
#     rate = int(input("Enter the rate :"))
#     time = int(input("Enter the time period : "))

#     def simpleinterest(self):  
#         print((self.principle*self.rate*self.time)/100) 
#         # self.name = input("Enter name:")  
#         # print(self.name)
    
# obj = Manipulation() # creating a object of class and we always create 
# obj.simpleinterest()
#----------------------------------------------------------------
class Manipulation:
    factorial = 1
    def fact(self):  
        num = int(input("Enter the number to calculate factorial : "))
        if num < 0:
                print("Factorial doesn't exists for -ve no.")
        elif num == 0:
                print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
                print("The factorial of", num ,"is",factorial)
        
obj = Manipulation() # creating a object of class and we always create 
obj.fact()    

#---------------------------------------------------------------------------------------------------
# Day 02:
# Program No. 01
class HOD:
    def __init__(self,name,age,roll): # parameterized constructors
        self.name = name
        self.age = age
        self.roll = roll

    def show(self):
        print('name = ',self.name) 
        print('age = ',self.age)  
        print('roll = ',self.roll)

obj = HOD('Sumit',45,101)
obj.show()        
   
# Program No.02 : declaring instance variable inside a constructor by using self variable.
class Student:
    def __init__(self):
        self.s_name = "Priyank"
        self.l_name = "Sharma" #instance varible
        self.roll = 12
        self.s_branch ="CS"
        self.s_mob = 00000000
        # every data member and its value stored in the form of {key:value} pair
obj = Student()
print(obj.__dict__)        

#Program No. 03
# declaring instance variable inside a method by using self variable.
class Student:
    def __init__(self): #constructor
        self.name = "Hazel"
        self.roll = 45
        self.branch = "IT"

    def getdata(self): # instance method
        self.s_mob =  9874895353 # instance variable
obj = Student()
#obj.getdata()
print(obj.__dict__)

#Program No 04
# Declaring instance variable outside a class by using object.
class Student:
    def __init__(self): #constructor
        self.name = "Shadab"
        self.roll = 23 # declaring instance variable inside a constructor

    def getdata(self):  
        self.mob = 893495345 # declaring instance var inside var inside instance method
obj = Student()
obj.getdata()
obj.branch="Civil"
print(obj.__dict__)     # adding instance variable by using object.      

# Program No.5 
# accessing and deleting instance variable from the class
class Student:
    def __init__(self):
        self.name = "Samar"
        self.roll = 34

    def getdata(self):
        self.mob = 34583453
       
obj = Student()
obj.getdata()
del obj.roll # deleting instance varible 
obj.branch = "Mech" # adding instance variable by using object
print(obj.name)  # accessing a variable outside a class
print(obj.__dict__)  

# Program no.06
class College:
    clgname = "SVKM IOT" # static variable

    def __init__(self):
        self.name = "Augustus " # instance variable

principle  = College() # object creation
teacher = College()
accountant = College()
print("principle = ",principle.clgname,"..",principle.name)
print("teacher = ",teacher.clgname,"..",teacher.name)
print("accountant = ",accountant.clgname,"..",accountant.name)

College.clgname = "HBD" # second way to add static variable
principle.name = "Augustus Cruise"

print("principle = ",principle.clgname,"|",principle.name)
print("teacher = ",teacher.clgname,"|",teacher.name)
print("accountant = ",accountant.clgname,"|",accountant.name)
'''
# Program No.07
# Task 01
# html page
# input = array
# input = enter the number to be searched
#  view.py Business Logic (linear search algo)
#-------------------------------------------------------------------------------
'''
# Day - 03
# Program No.01
#instance method example
class Student:
    def __init__(self,name,roll,mob):
        self.name = name #instance variables
        self.roll = roll
        self.mob = mob
    def display(self): #instance method
        print(self.name," ",self.roll," ",self.mob)
stud = Student("Nishant",101,8989898989)
stud.display()   
 #Program No.02      
#static method
class Student:
    # by using class name we can access static method
    @staticmethod #decorator
    def get_personal_detail(fname,lname):
        print("Your personal details = ",fname,lname)

    @staticmethod
    def contact_detail(mob,roll):
        print("Your personal details = ",mob,roll)
Student.get_personal_detail("Suhana","Khan")
Student.contact_detail(8989898989, 101)            

#Program No.02  
#implementing inner class concept
class BE_fy:
    def __init__(self):
        self.clgname = "SVKM IOT Dhule"
        self.br_name = "CSE"
        self.objsem = self.FirstSem() #inner class
    def display(self):
        print("College Name = ", self.clgname)
        print("Branch Name = ", self.br_name) #inner class
    class FirstSem:
        def __init__(self):
            self.sub1 = "DSA"
            self.sub2 = "DBMS"
            self.sub3 = "Python"
            self.sub4 = "CN"
            self.sub5 = "ML"
        def show(self):
            print("Subject 1 = ",self.sub1)
            print("Subject 2 = ",self.sub2)
            print("Subject 3 = ",self.sub3)
            print("Subject 4 = ",self.sub4)
            print("Subject 5 = ",self.sub5)    
obj = BE_fy()
obj.display()
objsem = obj.objsem
objsem.show()
'''
class Animal:
    legs = 4
    leg2 = 2
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))
    @classmethod    
    def wal(cls,name):
        print('{} walks with {} legs...'.format(name,cls.leg2))    
Animal.walk("Dog")
Animal.wal("Man")        
