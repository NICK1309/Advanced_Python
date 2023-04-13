# Question asked in TCS digital for 7LPA package 
#Create CSV file and read data from CSV file & sort them as per bubble sort.
'''AGE     SALARY
20   20000
23   34000
24   34443
34   20000
23   23433
29   23433
30   54455

import csv
def CSV2List(csvFilename: str):
    f = open(csvFilename)
    q = list(f)
    return q.sort()
'''
import csv
f = open("student1.csv","a",newline="")
a= csv.writer(f) #here it will  return csv writer object.
a.writerow(["studentid","rollno","name","mobileno"]) #column creation a column name.
studentId=int(input("Enter student id:"))
rollno=int(input("Enter rollno:"))
name=input("Enter student name:")
mobileno=int(input("Enter mobileno:"))
a.writerow([studentId,rollno,name,mobileno])
print("student record has been saved.")