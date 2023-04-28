'''class Student:
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
'''
class Manipulation:
    Task: 1.simple interest
          2.factorial
          3.fibonacci series

    you have to create 3 diffrent functions
    create a constructor (declare all the datamembers here create a function to accept the value for data members getdata() 
    3.create a function to only display the results of simpleinterest factorial,fibonacci series 
    display data
'''
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
   
    # num = 3
    fact = 1
    def fact(self):  
         num = int(input("Enter the number to calculate factorial : "))
         if num < 0:
                print("Sorry, factorial does not exist for negative numbers")
         elif num == 0:
                print("The factorial of 0 is 1")
         else:
            for i in range(1,num + 1):
                factorial = factorial*i
                print("The factorial of", num ,"is",factorial)
        
obj = Manipulation() # creating a object of class and we always create 
obj.fact()    
