'''
#with multithreading we can see same program
from threading import*
import time
def add(num):
    for n in num:
        time.sleep(1)
        print("Add=:",2*n)
        print()
def mul(num):
    for n in num:
        time.sleep(1)
        print("Mul=:",n*n)
        print()
def sub(num):
    for n in num:
        time.sleep(1)
        print("Sub=:",n-n)
        print()     
num=[2,4,6,8,9]
starttime=time.time()
t1=Thread(target=add,args=(num,))
t2=Thread(target=mul,args=(num,))
t3=Thread(target=sub,args=(num,))   
t1.start() 
t2.start()  
t3.start()  
t1.join()
t2.join() 
t3.join()                
print("The total time:= ",time.time()-starttime) '''
#-----------------------------------------------------------------
'''
#ident(thread identification number)
# every thread internally having UID number, and that can be get by implicit variable ident.
from threading import *
def show():
    print("Child thread \n")
child=Thread(target=show)
child.start()
print("main thread ID",current_thread().ident)
print("child thread ID",child.ident) '''
#------------------------------------------------------------------
'''
#without synchronization
from threading import *
import time
def conferenceCall(myname):
    print("Hi i am=")
    time.sleep(1)
    print(myname)
obj = Thread(target=conferenceCall, args=('Prashant ' ,))
obj2 = Thread(target=conferenceCall, args=('Ashish',))   
#here two objects (obj,obj2) are going to access same method at same time
obj.start() 
obj2.start()
 '''