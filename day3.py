'''
Synchronization
In case of multi threading when we are executing multiple thread there might be chance that at the same time multiple 
thread are going to exe same method or same statement so there will be the.
# ways to achieve synchronization :
1.lock
2.Rlock
3.semaphore
CTO, Risk Analyst 

# without synchronization how to implement the thread   

from threading import *
import time
def conferenceCall(myname):
    print('Hi I am :')
    time.sleep(2)
    print(myname)
    
obj = Thread(target=conferenceCall, args=("Prashant",))
obj2 = Thread(target=conferenceCall, args=("Priyank",))
obj.start()
obj2.start()

# Solution for synchronization is Lock:
from threading import *
import time
l=Lock() # lock objct created 
def come_in(name):
    l.acquire()
    for i in range(10):
        print(name)
        print("Yes sir : ", end='')
        time.sleep(1)
    l.release()   
obj = Thread(target=come_in, args=("Prashant",))
obj2 = Thread(target=come_in, args=("Priyank",))
obj.start()
obj2.start()    

#================================================================================================================
#problem in the thread lock 
#then it will be blocked
from threading import *
obj=Lock()
print("first time acquire lock")
obj.acquire()
print("second time acquire lock")
obj.acquire() # This will block the terminal 

from threading import *
obj=RLock()
print("first time acquire lock")
obj.acquire()
print("second time acquire lock")
obj.acquire() 


# WAP to import CSV file & perform actions
import csv
f = open("student.csv","a",newline="")
a= csv.writer(f) #here it will  return csv writer object.
a.writerow(["studentid","rollno","name","mobileno"]) #column creation a column name.
studentId=int(input("Enter student id:"))
rollno=int(input("Enter rollno:"))
name=input("Enter student name:")
mobileno=int(input("Enter mobileno:"))
a.writerow([studentId,rollno,name,mobileno])
print("student record has been saved.")
'''
# homework question 01 :
import csv
f = open("student1.csv","a",newline="")
a= csv.writer(f) #here it will  return csv writer object.
a.writerow(["rollno","name","email","address","mobileno","p1","p2","p3","p4","p5","total","percentage","Result"]) #column creation a column name.
rollno=int(input("Enter student id:"))
name=input("Enter student name:")
email=input("Enter EmailId:")
address=input("Enter Address:")
mobileno=int(input("Enter Mobile no:"))
p1=int(input("Enter marks for subject 1:"))
p2=int(input("Enter marks for subject 2:"))
p3=int(input("Enter marks for subject 3:"))
p4=int(input("Enter marks for subject 4:"))
p5=int(input("Enter marks for subject 5:"))
total = p1+p2+p3+p4+p5
percentage = total/5
if(percentage >= 40):
    print("You are Passed")
else:
    print("You are Failed")
a.writerow([rollno,name,email,address,mobileno,p1,p2,p3,p4,p5,total,percentage,Result])
