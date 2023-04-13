'''
import re 
a = input("Enter string to perform match operation")
mtch = re.fullmatch(a,"pythonisvery")
print(mtch)
if mtch != None:
    print("match found at begining level")
    print(mtch.start(), " ",mtch.end())
else:
    print("there is no matching at begining level")
#----------------------------------------------------------------------------------------------------------------
import re 
a = input("Enter string to perform match operation")
mtch = re.search(a,"pythonisssdynamicclann")
print(mtch)
if mtch != None:
    print(mtch.start(), " ",mtch.end())
else:
    print("there is no matching at begining level")
#--------------------------------------------------------------------------------------------------------------    
    
import re
mtch = re.findall('[A-Za-z0-9]',"abc8asd1j3j4")
print(mtch)
'''
#--------------------------------------------------------------------------------------------------------------
'''
import re 
mo=input("Enter Mobile Number.")
obj=re.fullmatch("[0-9]\d{9}",mo)
if obj != None:
    print("Valid Mobile number")
else:
    print("Invalid Mobile number")   
  '''  
#---------------------------------------------------------------------------------------------------------------
 #Task 01 :- #WAP to accept pw of pw contains uppercase lowercase digit special symbols then print pw is weak or strong.
import re
pw = input("Enter a Password.")
obj = re.search("[A-Z]",pw)
obj2 = re.search("[a-z]",pw)
obj3 = re.search("[0-9]", pw)
obj4 = re.search("W/",pw)
if obj != None and obj2 != None and obj3 != None and obj4 != None :
    print("Password is strong.")
else:
    print("Password is weak.")  

#--------------------------------------------------------------------------------------------------------------- 
'''import re
obj = re.sub("[0-9]","#","asda78asda8ad")
print(obj)
'''
#---------------------------------------------------------
# stack implementation (Last in first out)
'''
import time
stack = []
size = int(input("Enter the size of the stack :"))
for i in range(size):
    a = int(input("Push the element in stack:"))
    stack.append(a)
else:
    print("Stack is full")
    print(stack)    

print("Pop operation starts:")
for i in range(size):
    time.sleep(2)
    print(stack.pop()," Pop element from stack. ")
else:
    print("Stack is empty")
    print(stack)   
    '''
#---------------------------------------------------------------------------------------------------------     
# Queue implementation (First in first out)
'''
import time
queue = []
size = int(input("Enter the size of the queue :"))
if(size <= 10):
    for i in range(size):
        a = int(input("Insert the element in queue:"))
        queue.append(a)
    else:
        print("queue is full")
        print(queue)    

    print("Removal operation starts:")
    for i in range(size):
        time.sleep(2)
        print(queue.pop(0)," Delete element from Queue. ")
    else:
        print("Queue is empty")
        print(queue)   
'''
#---------------------------------------------------------------------------------------------------------------- 
       