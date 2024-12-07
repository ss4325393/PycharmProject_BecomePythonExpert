"""
Conditional Statements:
if,elif ,else

Till now we were using assignment operator then data was being transferred.But now we want that statements should be executed only if some particulars are True .

In python, the statement having some sub - statements inside it are called headings. At the end of the headings, we use : colon character
And this one group of statements is called Block.( Block of code ). All the statements inside a block or inside a heading are indented statements ie they are separated by fixed space with respect to heading.

if and elif need boolean type of data inside it or any True/False value

if (condition)
   Statement 1
   Statement 2
   .
   Statement n

elif (condition)
   Statement 1
   Statement 2
   .
   Statement n

else (condition)
   Statement 1
   Statement 2
   .
   Statement n

i can use single if.
i can use single if and elif
i can use single if and elif and else
i can use single if and else
i can"t use ony elif or else without if

if we have one if and multiple elif and else with this if then condition will be checked started from if then elif once a condition is True,rest of the condition against that if won't be checked

In c lang, block of code is separated by {}
In python, block of code is separated by indentation
indentation mean, all the statements inside a heading
ie inside a block of code is written at fixed space with respect to heading

"""
 # print("CETPA")  #Ereer



# a=5
# if(a==5):
#     print("Welcome to CETPA")
#     print("cepta is no1 company")
# else:
#     print("you are not welcomed ")
#     print("please try later ")

#New Program
# if(5):
#     print("CETPA")
# else:
#     print("Hello")


#New Program
# id=input("Enter your id:")
# pwd=input("Enter your pwd:")
#
# if id=="vikas" and pwd=="abc123" :
#     print("Id and Pwd are correct")
#     print("You are welcome")
# else:
#     print("incorrect Id or pwd")


# day=input(" Enter the day:")
# if day=="sunday":
#     print("Go to Movie")
# elif day=="saturday" :
#     print("Go to Market")
# elif day=="friday" :
#     print("take rest")
# else:
#     print("Go to Cetpa")
#
# print("program is complete")

"""
small project: Scientific calculator 
libraries /package/...Framework 
python is having  2.35 Lakhs+ libraries
Library is a collection of predefined variable, function class and Methods.
1. When we install python , some libraries are automatically installed.
2. When we create a python file , few libraries are automatically added in the program but not all the libraries which are already installed in the computer 
3. Rest of the libraries, We need to manually install in our computer .To download these libraries,open dos prompt:
 a.pip install package_name
 b.pytharm: File menu: Setting : Project: Interpreter  
   click on + ,Search Package_name and install

The libraries which are installed in our computer, to access these libraries in our program, We have multiple 
syntax:
import package_name
  
Feature of library use: Syntax 
package_name.feature_name
"""
#New Program
# import math
# r=math.log(1000,10)
# r=round(r)   #round (r,2)
# print(r)

# #New Program
# import random
# x=random.random()  #Random Value Between 0 to 1
# print(x)

"""
Randint: Will return the random value within given range including lower and upper bounds 

"""
# import random
# d1=random.randint(1,6)
# print(d1)

"""Scientific Calculator"""
# import operator
# import math
# no1=int(input("Enter First No: "))
# no2=int(input("Enter Second No: "))
# ch=input("Enter Choice +,-,*,/,pow,log: ")
# if(ch=="+"):
#     res=no1+no2
#     print("Result:,",res)
# elif(ch=="-"):
#     res = no1 - no2
#     print("Result:,", res)
# elif(ch=="*"):
#     res =operator.mul(no1,no2)    #res=no1*no2
#     print("Result:,", res)
# elif(ch=="/"):
#     res = no1 / no2
#     print("Result:,", res)
# elif(ch=="pow"):
#     res = no1**no2
#     print("Result:,", res)
# elif(ch=="log"):
#     res =math.log(no1,no2)
#     print("Result:,", res)
#
# else:
#     print("incorrect choice")




