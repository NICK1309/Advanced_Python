'''# Synchronnization using semaphore 
from threading import *
import time
l=Semaphore(4)
def come_in(name):
    l.acquire()
    for i in range(5):
        print("yes sir: ",name)
        print("------------------")
        time.sleep(1)

    l.release()
obj=Thread(target=come_in,args=("Priyank ",))
obj2=Thread(target=come_in,args=("Hazel ",)) 
obj3=Thread(target=come_in,args=("Daisy ",)) 
obj4=Thread(target=come_in,args=("Maria ",))         
obj.start()
obj2.start()
obj3.start()
obj4.start()
'''
#--------------------------------------------------------------------------------------------------------------------------------------------
'''
import re
count = 0
pattern = re.compile("python")
#print(pattern)
matcher = pattern.finditer("The python is easy language and python has many inbuilt libraries so the python is very interesting language.I love python.")
#print(matcher)
for i in matcher:
 count += 1
 print(i.start(),"...",i.end(),"...",i.group())
 print("The number of occurances:  ",count)
 
#----------------------------------------------------------------------------------------------------------------------------------------------
# find out data in text file and change it accordingly ...
# Task - 01
import re
# f = open("myfile.txt", "x")
with open("myfile.txt",'r') as f:
    data = f.readline()
pattern = re.compile("python")
match = pattern.finditer(data)    
for i in match:
    count += 1
print(count)
'''
#------------------------------------------------------------------------------------------------------------------------------------------
'''
import re
count = 0
matcher = re.finditer("Hi","HiaHiHiaHi")
for i in matcher:
    count +=1
    print(i.start(),"...",i.end(),"...",i.group())
print("The number of occurances :",count)

#-------------------------------------------------------------------------------------------------------------------------------------------
import re
obj = input("Enter any character.")
matchobj = re.finditer(obj,"a7sd sd878 sdfsd")
print(matchobj)
for match in matchobj: 
    print(match.start(),"...",match.end(),"...",match.group())
#print("The number of occurances :",count)
'''
#-------------------------------------------
import re
a = input("Enter any string to perform operations.")
ntch = re.match(a,"python is very imp")
print(ntch)
if ntch != None:
    print("match is found at begining level.")
    print(ntch.start(), " ",ntch.end())
else:
    print("There is no matching at begining level") 