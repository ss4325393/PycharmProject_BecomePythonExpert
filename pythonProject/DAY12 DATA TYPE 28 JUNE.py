"""
DATA TYPE :2
SINGLE ELEMENT:
int
float
complex
bool
NoneType
MULTI ELEMENT:
string
List
Tuple
dict
set
frozenset
range
"""

# #new Program
# def add(a,b):
#     return a+b
# print(type(add))


"""
str: Collection of homogeneous data type ie collection of characters 
how to create strings: using quotes
list:Collection of heterogeneous data type 
how to create list: keeping commas separated element in square brackets 
tuple:Collection of heterogeneous data type 
how to create tuple: keeping commas separated element in small brackets 

"""
# #New Program(list)
# L=[10,20,3.5,True,[1,2,6]]
# print(L)
# print(type(L))
# print(L[0])
# print(len(L))
# print(type(L[0]))

#New Program
# T=(10,20,3.5,True,[1,2,6])
# print(T)
# print(type(T))
# print(T[0])
# print(len(T))
# print(type(T[0]))

"""
Difference between List and tuple
list is mutable    :Means elements of list can be changed
If we change, increase or decrease or delete the element
of a list then base address of address of the list won't be changed 
tuple is immutable :Means elements of tuple can't be changed
if we change the elements than there will be error 
which data type is mutable in python 
list
dict
set

which data type is immutable in python 
rest all are immutable 
int
float
complex
bool
NoneType
str
tuple
frozenset 

First Thing first :variable means whose value will vary 
in the program and python is that powerful that even at the time of change of value,  
even you can change the data type.

so mutable means elements.
In python to support dynamic nature , every time ,we pass a new value to variable this new value is stored at a different location. 

Mutable: means changes at the same location 


"""
# #New Program
# L=[10,20,30]
# print(id(L))
# L[0]=50
# print(L)
# print(id(L))
#

# #New Program
# t=(20,30,40)    #tuple element can't be modified
# t[0]=500
# print(t)

# #New Program (string )
# s="santosh"       #str element can't be modified
# s[0]="t"
# print(s)

# #New Program
# s="CETPA"
# print(id(s))
# s="SANTOSH"
# print(id(s))

# #New Program
# L=[2,30,40]
# print(id(L),L)
# K=[210,50,30]
# print(id(K),K)

# #New Program
# i=5
# print(i,id(i))
# i=10
# print(i,id(i))


"""
change the first element of a string 
"""
# #New Program
# s=input("Enter the String:")
# w=input("Enter the New String: ")
# s=w+s[1:]
# print("New String is :",s)

# #New program
# t=(10,20,30)
# t[0]=(100)   #Error
# print(t)


#New Program
# t=(10,20,30)
# t=(30,50,60)
# print(t)

"""
how to access method of a class :
obj_name.,method_name(arguments)
"""
# s="SANtoSH"
# r=s.upper()
# print(r)

""" 
List method :
if we try to modify the list element using list method then same list is modified and new list is not created or new list in not returned ,
why? because list is mutable 
if we try to modify the string element using str method then same str is not modified and new str is created or a string is returned 
"""
# #New Program
# s="Cetpa"
# print(id(s))
# r=s.upper()
# print(r)
# print(id(r))

# #New Program
# L=[10,20,30]
# L.append(40)
# print(L)


# #New Program
# L=[10,20,30]
# r=L.append(40)
# print(L)
# print(r)         #None because list is mutable




