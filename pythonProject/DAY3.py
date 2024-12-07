"""
Data Type: What kind of values we can pass to variables.
have predefined rules.
x=5 Actual value in binary
x="5"ASCII Value

ASCII : American Standard Code for Information interchange
Initially ASCII Code was of 7 bits: Total combinations: 2 power n(7):128
8 Bits: Min value 0,Max value:255 Total combinations: 2 power n(8):256
00000000
00000001
.
.
11111111
A ASCII Code:65    a ASCII Code :97
B           :66    b            :98
C           :69    c            :99
.
Z           :90    z            :122

0           :48
1           :49
.
5           :53
9           :57

python 3: Started supporting Unicodes

Variable: Data Storing Element: Whose value vary in the program
variables are Stored in RAM

"""
# print("santosh")
# print(25)

#new program
# x=25
# print(type(x))
# print(x)

# print(ord("5"))
# print(ord("क"))
# print(chr(2325))
# print(chr(65))

#new program
# print(ord("$"))

"""
input function :To take the data from the user 
syntax
var=input("message for user")
"""
# new program
# name= input("Enter Your Name: ")
# print(name)

#new program
# a=input("enter first No:")
# b=input("enter second No:")
# r=a+b
# print(r)    #57 why?

"""
Whenever we interact in python with outer world using print or input function ,data is transmitted in string format
"""
#new program
# a="5"
# b="7"
# r=a+b
# print(r) #concatenated
# #new program
# a="HELLO"
# b="WORLD"
# r=a+b
# print(r) #concatenated

"""
When we use + operator on numbers ,then data will be added 
when we use + operator on string, then data will be concatenated 

Type casting : Conversion of one data type to another data type 
Syntex : res_var=src_type(src_var)



"""
#new program
# a=5
# print(type(a))
# a=input("Enter your No: ")
# print(type(a))

#new program
# x=5
# print(x, type(x))
# x=float(x)
# print(x, type(x))
# x=str(x)
# print(x, type(x))
# print(len(x))

# #new program
# x="5"
# print(x,type(x))
# x=int(x)
# print(x,type(x))

# WPA to add 2 numbers, take inputs from user
# no1=input("Enter first No:")
# no1=int(no1)
# no2=int(input("Enter second No:"))
# res= no1+no2
# print("Result:",res)

"""
Data Type:
Single Element:
int 
float
complex
bool
NoneType
 
Multi Element: 
Str
list
tuple
dist
set
frozenset


str: collection of homogeneous data type ie characters or unicodes
list:collection of heterogeneous data types

Syntax
Var=[Comma separated values]
"""
# a=[22,55,"CETPA",[2,3,4]]
# print(a)
# print(type(a))
# print(len(a))

#New program
# L1=[11,22,33,44,55]
# print(L1)
# L2=[66,77,88]
# print(L2)
# L3=L1+L2  #both lists are concatenated
# print(L3)

"""
tuple : collection of heterogeneous data type 
syntax
var=(comma Separated values)
"""
# t=(11,22,"santosh",5.5)
# print(t)
# print(type(t))

#New program
# x=5
# print(len(x))  #Error :Work on Iterators

"""
Type casting : Conversion of one to another 
"""
s="SANTOSH"
L=tuple(s)
print(L)
