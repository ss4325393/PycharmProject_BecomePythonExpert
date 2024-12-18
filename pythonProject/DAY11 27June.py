"""
Write a python program to swap commas and dots in string.
sample string : "127.0.34,1"
Expected Output: "127,0,34.1"
"""
#new program
# s="127.0.34,1"
# s=s.replace(".","*")
# print(s)
# s=s.replace(",",".")
# print(s)
# s=s.replace("*",",")
# print(s)

#Cresate own count method
#New Program
# #business logic layer
# def myCount(L,d):             # L=[10,20,10,90,70,10,20,30]
#     count=0
#     for e in L:               #e=10, e=20
#         if (e==d):
#             count+=1          #count=count+1, count=1,count=2
#     return count
#
# #Presantation Layer
# L=[10,20,10,90,70,10,20,30]
# d=70
# n=myCount(L,d)
# print(n)
"""
Loops:

for loop syntax:
for element/index in iterator:
     set of statements 
     
iterator can be str ,list, .... range

we can directly access the elements of a str,list, tuple...in a loop or even 
we can access the elements using index (indexing) using range class 

"""
# #New program
# L=[10,20,30,40,50]
# for e in L:
#     print(e)

# # #New program
# L=[10,20,30,40,50]       #i=0,1,2,3,4
# for i in range(5):
#     print(i)
#
# #New Program
# L=[10,20,30,40,50]         #list index 0 to 4
# for i in range(len(L)):    #len(L):Range(5):i =0,1,2,3,4
#     print(i,L[i])          #i=0,L[0],i=1,L[1],i=2,L[2]


"""
To access elements in a loop 
s="CETPA"
Option a:
for e in s:
  print(e)
  
option b:
for i in range(len(s)):
   print(s[i])
"""
"""
you have a list and you want to sum every 2 elements consecutively
L=[10,20,30,40,50]
output:10+20=30
       20+30=50 
       
Loop to run 4 times, length is 5
i      element(e)
0      L[0]+L[1]
1      L[1]+L[2]
2      L[2]+L[3]
3      L[3]+L[4]
e=L[i]+L[i+1]
       
Length=5
loop to run: Length-1 
"""
# #New Program(you have a list and you want to sum every 2 elements consecutively)
# L=[10,20,30,40,50]
# for i in range(len(L)-1):
#     e=L[i]+L[i+1]
#     print(e)

"""
Nested loops: 
Outer loop n time run ,inner loop m times: Final statements inside inner loop will run:n*m times

"""
# #New Program
# for i in range(3): #i=0
#     for j in range(4):
#         print(i,j)     #This statement will run 3*4 ie 12 times
# print("End the both the loops")

# #New program
# L1=[1,2,3,4]
# L2=[6,7,8,9]
# for e1 in L1:
#     for e2 in L2:
#         print(e1,e2)

# #New Program
# def func1():
#     pass
# r=func1()
# print(r)

# #New Program
# print()
# print()
# print()
# print()
# print()


#New Program
# for i in range(3):
#     print()

"""
*
*
*
*
*
"""
# for i in range(5):
#     print("*")

"""
*****
"""
# for i in range(5):
#     print("*", end="")

"""
Pattern Printing :
*
**
***
****
*****
i    j
0    1
1    2
2    3
3    4
4    5
Find relationship between j_max and i ie j=i+1
"""

#New Program
# for i in range(5):   #i=0,1,2,3,4
#     for i in range(i+1):
#         print("*",end="")
#     print()
"""
pattern printing in loops 
n input: for no of lines 
*
**
***
****
*****
.
.

"""
# #New program
# a,b,c=[10,20,30]    #unpacking
# print(a,b,c)

# #New program
# L=[[10,20],[30,40],[50,60]]     #2-D List
# for a in L:
#     for b in a:
#         print(a,b)

#New program
# L=[[10,20],[30,40],[50,60]]     #2-D List, 3 element
# for a,b in L:
#     print(a,b)             #unpacking

#New Program
# L=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for a,b,c,d in L:
#     print(a,b,c,d)


"""
pattern printing in loops 
n input: for no of lines 
*
**
***
****
*****
.
.
range(0,n,1) means range(n)
"""
#New Program
# n=int(input("Enter No. of Lines: "))  #n=6
# for i in range(n):   #i=0 to 5,0 to n-1
#     for j in range(i+1):
#         print("*",end="")
#     print()

"""
*****
****
***
**
*
i loop :n
inner loop j
i      j
0      5
1      4
2      3
3      2
4      1

Now no python ,math only ,tell me the relationship between j,i and n ie how j is dependent on i and n
j=n-i 

"""
# #New program
# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print()

"""
    *
   **
  ***
 ****
*****

make a table
let n=5 
i    j   k
0    4   1
1    3   2
2    2   3
3    1   4
4    0   5

j relation with n and i:j=n-i-1 
k relation with n and i:k=i+1 

"""
# #New Program
# n=int(input("Enter No of Lines:"))   #n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()

"""
*        *
**      **
***    ***
****  ****
**********
create a table for this
i   j   k   l
0   1   8   1
1   2   6   2
2   3   4   3
3   4   2   4
4   5   0   5
formula
j=i+1
k=2*(n-i-1)
l=i+1

"""
# #New program
# n=int(input("Enter No of Lines: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(2*(n-i-1)):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()
"""
A
BB
CCC
DDDD
EEEEE

"""
# #New program
# code=65
# for i in range(5):
#     ch=chr(code)
#     for j in range(i+1):
#         print(ch,end="")
#     code+=1
#     print()


"""
while loop is exactly similar in functionality to for loop ,
while loop is used generally to develop infinite loop 

while loop will only run till the time, value inside while is a true value
false value
1. None 
2. 0
3. Empty
4. False

To exit from for or while loop on the some particular condition ,we can use break keyword 

To skip some particular iteration of a loop, we can use continue keyword 

"""
# while (-800):
#   print("santosh")

# #New Program
# L=[10,20,30,40,50]   #print:10sq,20sq,40sq,50sq don't want to print element of index 2
# for i in range(len(L)):   #range(5),i=0,1,2,3,4
#     if (i==2):
#         continue
#     print(L[i]**2)

# #New Program
# for i in range (5):
#     print(i)
#
#
# i=0   #lower bound
# while(i<5):   #while (i<upper bound)
#     print(i)
#     i+=1      # increment by step size

"""
steps to make a while loop 
1.Initialize the index/variable with lower bound
2.while (condition)  : index<upper bound 
                       index >upper bound any condition 
                       
3.inside loop, set of statements, which need to be executed repeatedly 
4.increment or decrement index by step size 
 
"""
#New Program
# for i in range (2,21,2):
#     print(i)

# #New program
# i=2             #lower bound
# while(i<21):    #while (i<upper bound)
#     print(i)
#     i+=2        #increment by step size

