
"""Nested conditions : Condition inside Condition"""

#New Program
# a,b,c,d=1,4,3,4
# if(a==1):
#     if(b==4):
#         if(c==5):
#             print("Inside a,b,c")
#         else:
#             print("hello")
#     elif(c==6):
#         print("CETPA")
#     else:
#         print("ABCD")
#
# else:
#     print("how are you?")
# print("Program is complete")

# id=input("Enter the id :,")
# if (id =="bond"):
#       pwd=input("Enter the Pwd")
#       if(pwd=="007"):
#           print("id and pwd are correct")
#           print("you are Welcome")
#       else:
#           print("Incorrect Pwd")
# else:
#     print("the id is incorrect")

"""find the biggest of 3 number using nested condition"""
#
# num1=input("Enter first number: ")
# num2=input("Enter second number: ")
# num3=input("Enter third number: ")
#
# if (num1>num2):
#     if(num1>num3):
#         print("the biggest No is",num1)
#     else:
#         print("The biggest No is ",num3)
# else:
#     if(num2>num3):
#         print("The biggest no is",num2)
#     else:
#         print("The biggest no is",num3)


# #New Program
# a,b,c=5,7,9
# print(max(a,b,c))

"""
indexing anf slicing

string: Collection of homogeneous data type ie character

list:Collection of heterogeneous data type 
L=[10,"ABCD",True,2.35,[2,5,6]]


Tuple:Collection of heterogeneous data type 
t=(10,"ABCD",True,2.35,[2,5,6])


"""
# L=[10,"ABCD",True,2.35,[2,5,6]]
# print(L)
# print(type(L))
# print(len(L))

#New Program
# t=(10,"ABCD",True,2.35,[2,5,6])
# print(t)
# print(type(t))
# print(len(t))

"""
indexing : To access a particular single element of an iterator
s="CETPA" #5 Element indices : 0 to 4 or -5 to -1
Left most element index=0  +ve indexing 
Right Most element index=-1 -ve indexing
python supports negative indexing
if n elements
+ve index:0 to n-1
-ve index:-n to -1

Syntax of indexing 
Iterator_name[index]


indexing :IndexError :if index goes out of range
"""


# s="CETPA"
# print(s[-5])
# print(s[-4])
# print(s[-1])

# #New Program
# L=[10,20,30,40,50,60]
# print(L[2])
# print(L[-4])

#New Program
# L=[10,20,30,40,50,60]
# print(L[10])


"""
Slicing: To access group of elements in a sequence 
Syntax:
iterator[Lower_bond:Upper_bond:stepsize]
1.step size is optional, default step size is 1
2.upper Bond is discarded in case of slicing or at most of the places in python 
3.in case of slicing if bounds are out of range then we get empty values 
4.In +ve step size,default lower bound:0, default upper bond: n


"""
# s="welcome"
# print(s[1:6:2])  #s[1],[3],[5]      #s[1],s[3],s[5]

# s="welcome"
# print(s[1:5:2])  #s[1],s[3]:valid elements in s[1] to s[4]

# #New Program
# s="welcome"    #index 0 to 6
# print(s[10:20:2])  #s[1],s[3]:valid elements in s[1] to s[4]

# #New Program
# L=[10,20,30,40,50,60,70,80] #index 0 to 7
# print(L[4:20:2])

# New Program
# L=[10,20,30,40,40,40,40,80] #index 0 to 7
# print(L[4:20:2])

#new program
# s="Welcome"         #index 0 to 6
# print(s[1:8:1])     #s[1] ,s[2]...s[6]
# print(s[1:20:1])

#New Program
# s="Welcome"    #index 0 to 6
# print(s[1:5])  #s[1],s[2],s[3],s[4], default step size 1


#New Program
# s="Welcome"    #index 0 to 6
# print(s[1::2])  #s[1],s[3],s[5]


# #New Program
# s="Welcome"    #index 0 to 6
# print(s[0::2])  #s[0],s[2],s[4],s[6] ,upper bond =7



