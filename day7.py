# Q.1) Write python program to print follwing output.
# 1 5
# 2 4
# 4 2
# 5 1
n = int(input("Enter a number."))
for i in range(1, n):
    if(i == 3):
        continue
    print(i,6-i)
       
#---------------------------------------------------------------------------------------
# Q.2) WAP to Print the number of pairs.
#      [2,2,3,4,4,4,5,6,7,2]

# list = [2,2,3,4,4,4,5,6,7,2]
# for i in range(2):
#     x = list.count(i)

# print(x)

#--------------------------------------------------------------------------------------
# Q.3) WAP to Print the index number of first occurence and last occurence of 2.
#      [1,5,3,2,2,3,4,2,3,5,6]
# list = [1,5,3,2,2,3,4,2,3,5,6]
# print(list.index(2, 3,7))
        

