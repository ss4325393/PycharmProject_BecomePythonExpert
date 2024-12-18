
#Check Whether the first character and last character of a string are same ?
#BLL

# def check(s):
#     if(s[0]==s[-1]):
#         return "same"
#     else:
#         return "not same"
#
# #PL
# s=input("Enter Any String:")
# res=check(s)
# print("The first and last character are ",res)
"""
Loops: Are used to run the block of code repeatedly.
TO run the code again and again for finite no of times or infinite no of times.

Types of Loops in Python: Two types
1.for
2.while

Main Syntax for loop:
for element in iterator:
      set of statements

Another Syntax ie variant of main syntax for loop:
for index/var in range():
      set of statements

"""
#New program
# s="CETPA"
# for e in s:
#     print(e)
# print("End of Loop")

# #New Pmrogram
# s=[10,20,30,40,50,60,70]
# for e in s:
#     print(e,end="")
#     print("*")
# print("End of Loop")

"""
main syntax: 
for element in iterator:
       block of code to execute repeatedly 
       
       
Extended syntax:
for index/var in range (arguments):
    block of code to execute repeatedly 
    
range is a class which is also an interator 
Iterator : on which for loop will be executed which can be iterated 

range syntax:
range(lower_bond,upper_bond,step_size)

range(5,2,1):how many times loop will run:0 times ,same 
rules of slicing ie for +ve  step size ,upper bond should be bigger than lower bound.

range(a,b,s)
range(1,8,2)   #1,3,5,7

if we have 3 arguments in range: range (a,b,s):
a:lower bound 
b:upper bound 
s:step size

if we have 2 arguments in range: range (a,b):
a:lower bound 
b:upper bound 
Default step size=1

if we have 1 arguments in range: range (b):
Default step size=1
Default lower bound=0
b:upper bound 

remember: range(n) mens loop will run n times ie starting from 0 till n-1.  
This syntax will be used mainly in loop 

range is a data type ,multi element 


"""
# for i in 5:
    # print(i)   #TypeError: 'int' object is not iterable

# #New Program
# for i in range(1,7,2):
#     print(i)  #3times prent statement will be executed

#New Program
# for i in range(3,7):
#     print(i)

# #New Program
# for i in range(5):   #
#     print(i)

# # #New Program
# for i in range(5):   #n-1
#     print(i)
#
# #new program
# x=range(5)
# print(x)
# y=list(x)
# print(y)

# #New Program
# L=[0,1,2,3,4]
# for i in L:
#     print(i)

# #New Program
# L=range(5)
# for i in L:
#     print(i)

"""
loops Programs: Level 1: Print a Series ie elements ie Access element of an iterator: 
Ex1: Table of 2 print:
Stating element: Lower bound:2
Last element: 20,upper bound: 21
step size:2
"""
# for i in range(2,21,2):
#     print(i)

"""
Rule:All user interaction statement are written in PL,
If there is need of the program.or PL is big then we can even divide PL in functions.classes or modules.
if we have few simple logics than these logics may be implemented in Pl also.
"""
#print a table where number is input by user
"""
Lower bound:n
upper bound: (n*10+1)
step size: n
"""
# #new program
# #PL
# n=int(input("Enter the Number: "))    #n=7
# for i in range(n,(n*10+1),n):
#     print(i)

"""
series print: check how many times loop to run :10
for i range(10)
make a table of i and term, calculate the term and print
i_value      term(t)
0             5
1             10
2             15
3             20

9             50
now leave python and use maths,and find the relationship between input and output ie
how term is dependent on i 
t=(i+1)*5



"""
#New program
#Table of 5
# for i in range(10):
#     t=(i+1)*5
#     print(t)


#New program
#Table of n
# n=int(input("Enter the Number:"))
# for i in range(10):
#     t=(i+1)*n
#     print(t)


"""
2cube, 3cube, 4cube... 13cube
Number of element :12
a:2
b:14
s:1
i   term
2    2cube 
3    3cube
.
13   13cube
maths: Relation between term and i
t=i**3
"""
# #New program
# for i in range(2,14):
#     t=i**3
#     print(t)

#New program
# n=int(input("Enter the Number: "))
# for i in range(2,14):
#     t=i**n
#     print(t)

"""
negative value in range

"""
# for i in range(-5,-2,-1):
#     print(i)                 #loop won't run for a single time

"""
Level 1 of Loops:
how to print elements of a Series
    case a: Yesterday we discussed, how to create elements of the 
    loop using range class like how to print different integers or 
    combination of integers 
    case b: print the series but take the elements from a readymade 
    iterator like we have a list and to perform some task on that list
    and print the result  

range class only supports integer arguments 
"""
# L=[10,20,30,40,50]
# for e in L:
#     print(e*e)

#New Program
# for i in range(1,1.4,0.1)  #error
#     print(i)

#New program
#Access the elements of a string and convert them into capital letter without using string methods
#New Program
# s="ceTpA123"
# for e in s:
#     code=ord(e)                   #code =99
#     if (code>=97 and code<=122):
#         code=code-32              #code=67
#     ch=chr(code)                  #ch='C'
#     print(ch)


"""
To convert a capital letter to small latter,add 32 in ascii value of the code. 
To convert a small letter to capital latter,add -32 in ascii value of the code. 

"""
# #New program: Above program
# s="ceTpA123"
# for e in s:
#     code=ord(e)                   #code =99
#     if (e in "abcdefghijklmnopqrstuvwxyz"):
#         code=code-32              #code=67
#     ch=chr(code)                  #ch='C'
#     print(ch)

"""
Level 2 of the Loops:
perform some operation on the elements or selected elements of an iterator and display the final result. Iterator can be str, list or range or any other iterator.
 steps:
 1:run the loop/iterate the loop on iterator 
 2.create the table: find the relationship between term and index?element .calculate the term with table or without table 
 3.write the expression result= result operator term 
 4.Mention step 0: Initiate the result before the start of the loop in such a way that first time loop runs,result should get the value of first term 
 5.terminate the loop by coming out of indentation and print the result or use the result.
 vary important concept or program of loops ie to sum the elements of an iterator.
L=[10,20,30,40,50]
res=10+20+30...50
"""
#Find the sum of the elements of a list
# L=[10,20,30,40,50]
# res=0
# for e in L:
#     t=e       #calculate the term, t=10,t=20,t=30
#     res=res + t   #res = res +e,res=10...
# print(res)

# #New program
# #Business Logic Layer
# def myUpper(s):     #s="ceTpA123
#     res=""
#     for e in s:     #E="c"
#         e=ord(e)    #e=99  assi
#         if (e>=97 and e<=122):
#             e=e-32      #e=67
#         e=chr(e)    #e="C"
#         res=res + e
#     return res
#
# #Presentation Layer
# s=input("Enter Any String: ")
# res=myUpper(s)
# print("String in Upper case: ",res)

#
# #New Program
# #Sum the digits of a number input by user
#
# #Business Logic Layer
# def myLove(s):     #s=23456
#     res=0
#     for e in s:               #e="2" ,e="3", e="4"
#         t=int(e)              #t=2   ,t=3  , t=4
#         if (t%2==0):
#             res=res + t       #res=2  ,res=2+4
#     return res
#
# #presentation Layer
# s=input("Enter Any number: ")
# res=myLove(s)
# print("sum of only even number of total ",res)


















