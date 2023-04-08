'''
#Method 1
import threading
import time
print("Hello World :",threading.current_thread().getName())
def activate():
    for i in range(1,11):
        time.sleep(2)
        print("This is a child thread \n")

t=threading.Thread(target=activate)#creating thread obj
t.start() #call object
for i in range(1,11):
    time.sleep(2) 
    print("This is a main thread") 
'''
#----------------------------------------------------------------------    
'''      
# Method 2
from threading import *
import time
class MyThread(Thread):
    def run(self):
        for i in range(10):
            time.sleep(2)
            print('Child Thread-1')
obj_t=MyThread() 
obj_t.start()

for i in range(10):
    time.sleep(1)
    print('Main thread-1')
'''
#----------------------------------------------------------------------
'''
#Method-3         
from threading import *
class Mytest:
    def display(self):
        for i in range(10):
            print('Child Thread \n')
obj=Mytest()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread \n")            

'''