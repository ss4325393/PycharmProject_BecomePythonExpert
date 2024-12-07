"""
Indexing :if index is out of range : Then IndexError


Slicing: if bound is out of range : Then empty value

"""

# s="Welcome"   #index 0 to n-1 where n is no of elements: 0 to 6
# print(s)
# print(s[:])   #s[0:7:1] upper bond will be discorded
# print(s[::])  #s[0:7:1}
# print(s[0:])   #s[0:7:1}
# print(s[:10:])  #s[0:10:1} ie s[0:7:1]
# print(s[::1])    #s[0:7:1}

"""
+ve slicing: step size is +ve
if upper bond is bigger than lower bound then only we will get the output otherwise empty value,ie while slicing, if we moving from left to right then only we will get the output 

-ve slicing: step size is -ve
1.if upper bond is smaller than lower bound than only we will get the output otherwise empty value,ie while slicing,if we are moving from right to left than only we will get the output
2.Default lower bound =-1, Default upper bond =-n-1
in case of we have different signs of bounds. Then first thing first, change the signs of both the bonds to common sign, generally we make it +ve sign
"""
# #New program
# s="Welcome"
# print(s[10:2:1])

# #New program
# L=[10,20,30,40,50,60]
# print(L[2:2])          #upper should be bigger than lower bond should not equal

# #New Program
# s="Welcome"    #+ve slicing
# print(s[-2:-5:-1])  #s[-2],s[-3],s[-4]

# #New Program
# s="Welcome"  #-ve slicing
# print(s[-2:-5:1])


# #New Program
# s="Welcome"  #-ve slicing
# print(s[2:5:-1]) #upper bond is smaller than lower bound #empty output
#
# #New Program
# s="Welcome"  #-ve slicing
# print(s[-2:5:1])   #s[5:5:1]

# #New Program
# s="Welcome"
# print(s[2:-5:1])   #s[2:2:1]
#
# #New Program
# s="Welcome"
# print(s[1:-4:1])   #s[1:3:1] ie s[1],s[2]

#
# #New Program
# s="Welcome"
# print(s[-1:4:1])   #s[6:4:1] empty

# #New program
# s="Welcome" #-ve slicing
# print(s[:-4:-1])  #s[-1:-4:-1]

# #New program
# s="Welcome" #-ve slicing
# print(s[-2::-1])  #s[-2:-8:-1]

# #New program
# s="Welcome" #+ve slicing
# print(s[-2::])  #s[-2:7:1] s[5:7:1]



"""
convert a string to a reverse string without using any method 
"""
# s="Welcome"
# print(s[::-1])  #s[-1:-8:-1]

# #New Program
# L=[[1,2,3],[4,5,6],[7,8,9]]
# print(L)


# #New Program
# L=[[1,2,3],[4,5,6],[7,8,9]]
# print(L[0])
# print(type(L[0]))
# print(L[0][0])


# #New Program
# L=[[1,2,3],[4,5,6],[7,8,9]]
# print(L[0][4]) #Error


# #New Program #2-D Array:List in python is an indirect array
# L=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#    ]
# print(L[2][1])

# #New Program #2-D Array:List in python is an indirect array
# L=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#    ]
# print(L[2][0:2])
#
# #New Program #2-D Array:List in python is an indirect array
# L=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#    ]
# print(L[0:b2][0:2])
#
# #New Program
# a=[[1,2,3,],[4,5,6]]
# print(a[0:2])    #a[0]a[1]

"""
How to call a function : syntax 
function_name(arguments)
if function is made inside a class , then generally we call 
it a method pr few people call it function only.

how to call a method:
Firstly create the object of that class.For the time being,
we can call object as a variable.
how we create variable in python ? by assigning the value 
syntax to call a method:
object_name.method_name(Arguments)

String:
Every date type in python is a class,
class is a collection of variables and methods. 

"""
# s="Welcome"
# r=s.upper()
# print(r)

# #New Program
# s="Welcome"
# print(s.upper())
#
# #Nwe Program
# s="Welcome"
# n=len(s)
# print(n)
# print(len(s))


#New Program
# print(print("santosh"))

# #New Program
# a=print("CETPA")
# print(a)
#
# #New Program
# s="SANTOSH INFOCetpa123**$"
# print(s.lower())

#
# #New Program
# s="SANTOSH INFOCetpa123**$"
# print(s.title())

#
# #New Program
# s="Welcome to cetpa"
# r=(s.count("t"))
# print(r)

# #New Program
# s="Welcome to cetpa"
# r=(s.find("t"))
# print(r)

# #New Program
# s="Welcome to cetpa"
# r=(s.index("t"))  #will return +index of first matching element
# print(r)

"""
In find method, if element is missing than output will be -1
In index method, if element is missing then output will be Error 
"""

# #New Program
# s="Welcome to Cetpa"
# r=s.index("X")            #will return
# print(r)


# #New Program
# s="Welcome to Cetpa"
# r=s.find("X")            #will return -1
# print(r)

# #New Program :Remove c from string
# s="Welcome"
# s=s[:3]+s[4:]
# print(s)
#
# #New Program :replace c from string
# s="Welcome"
# s=s.replace("c","")
# print(s)

# #New Program :replace
# s="Welcome"
# s=s.replace("elco","****")
# print(s)

"""Any method having is in the starting then it will return bool value"""

# #New program
# s="Welcome"
# print(s.isalpha())    #Alphabet or not


# #New program
# s="123"
# print(s.isdecimal())    #Only Numbers or not

# #New program : WAP To check whether the mobile number input by user is of correct format or not
# m=input("Enter mobile no")
# if m.isdecimal():
#     if (len(m)==10):
#         print("the number is correct formate")
#
#     else:
#         print("enter the number in 10 digit only")
# else:
#     print("enter only number in mobile ")


# #New program
# s="Welcome"
# r=s.islower()
# print(r)
#
# #New program
# s="Welcome"
# r=s.join("***")
# print(r)


# #New program
# s="santosh kumar sahni"
# r=s.split()             #by default split on the basis of space
# print(r)
#
# #New Program
# num=input("Enter 5 numbers: ").split()
# print(num)
#
# #New program
# L=["santosh","kumar","sahni"]
# r=" ".join(L)
# print(L)

#
# #New program
# L=["santosh","kumar","sahni"]
# r="***".join(L)
# print(r)

# # #New program
# s=" welcome to CETPA    "
# print(len(s))
# r=s.strip()
# print(r,len(r))   #remove any trailing character

# #New program
# a=int(input("Enter First No :").strip())
# b=int(input("Enter second No :").strip())
# r=a+b
# print(r)
#
# #New program
# s="    welcome to CETPA..."
# r=s.replace(" ","")
# print(r)

# #New program
# s="SANTOSkumar"
# r=s.swapcase()
# print(r)















