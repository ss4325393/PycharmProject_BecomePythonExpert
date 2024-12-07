"""
Function: A block of code , designed to perform a specific task
why Function ?
1.TO Make the code reusable
2.Function are the basic Building blocks of modular approach of programing
3.Function are the basic building blocks of multi-Threading
4.Function are the basic building blocks of layered architect
The most popular layers are Presentation Layer (PL) and
Business logical layer  (BLL) one more important layer is
DLL (Data Link Layer ) OR DAL(Data Access Layer )
5. Function make the code scalable.

Syntax to call a Function:
Function_Name(Argument) # while calling a function, arguments passed are called actual parameters

Syntax to create a function : UDF: User Defined Function
def function_Name(arguments):
      block of code
      return argument #Return is optional

if a function doen't return  anything then in python automatically None type is None value is returned
# while creating a function, the argument mentioned inside function are called formal parameters.


kasam1.use as much comments as possible in your program,min 3 comment:#BLL,PL,What functionality going to import
Kasam:2.use logical names for identifiers (user defined names) ie variable or function names
Function name to Add a customer in crm:add_customer()
class name for customer: customer
kasm:3.whenever we will create even a very simple program ,you will divide at least in 2 layers ie
presentation Layer (PL) and
Business Logic Layer(BLL)
KASAM:4.you will use print and input functions only in PL
PL: is responsible for interaction with the user. for user interaction in console programming, we have two functions ie print and input,so we will write these function in PL.
BLL: Is responsible for writing the actual business logic

Nomenclature generally used by developers gives us some guidelines, these are not rules:
a: class name should start with capital letter and every new word should start with capital letter and every new word should start with capital letter.
b.Function name should start with small letter and stress on each word ie first word in function name complete small and then every word start with capital :
c.Variable Name: Complete small
cus_id variable name
try to add _under score in identifiers name


addCustomer() Function_Name
MyCustomer()   class_name



"""
#New program
# def add(a,b):
#     s=a+b
#     return s
# a,b=5,7
# r=add(a,b)
# print(r)

#WAP to check whether a number input by user ia a even no ot nat?
# def even(a):
#     if (a%2==0):
#         return "yes"
#     else:
#         return "no"
#
# no=int(input("Enter Any No: "))   #no=7
# res=even(no)
# print("The Entered No is Even ?: ",res)

#Business logic layer:BLL
# def add(a,b):                          #l1
#     return a+b                         #l2
#
# #presentation Layer :PL
# no1=int(input("Enter First no:"))      #l3
# no2=int(input("Enter Second no:"))     #l4
# res=no1+no2                            #l5
# print("The sum of number is:",res)     #l6


"""
how above program will be executed:
step1: Line 1 :L1,Firstly the definition of function will be created in the program, Function body never executes on its on,till the time, Function is called  
step2:L3
step3:L4
step4:L5 :Add Function
step5:L1,L2
step6:L5
step7:L6 Output will be printed on the screen 


"""
#New Program
#BLL
# def add()
#     r=a+b
#     return r
#
# #PL
# a,b=5,7          #eroor
# res=add(a,b)
# print(res)

"""
1.The variable which are defined inside function are called local variables.
2.The variable which are defined outside function are called global variables 
3.Global variable means, these variable can be accessed globally ie both outside functions as well as inside function .
4.Local variable means, these variable can be accessed only inside function not outside function.
"""
# #New program
# def func1():
#     print(a)
#
# a=5     #Global Variable
# func1()

#New program
# def func1():
#     a=5
#
# func1()        #local Variable
# print(a)       #error

#New Program
#BLL
# def add():
#     r=a+b
#     return r
#
# #PL
# a,b=5,7
# res=add()
# #print(r)  #error ,r is local variable
# print(res)
#
# #New Program  #Required Argument Function
# def add (a,b):
#     r=a+b
#     return r
# a,b=5,7
# print(add(a,b))

# #New Program :Approach 1,without passing arguments
# #BLL
# def add():
#     r=a+b
#     return r
# #PL
# a,b=5,7    #global variable
# res=add()
# print(res)
#
# #New program :Approach 2,by passing the arguments
# def add(a,b):
#     r=a+b
#     return r
# #PL
# a,b=5,7    #
# res=add(a,b)
# print(res)

"""
In above 2 approaches to write the same program, 2 approach is better because it makes the code reusable ie in 2nd approach same function can be used with different actual parameters   

"""
# def add (a,b):
#     r=a+b
#     return r
#
# a,b,c,d,e,f,=1,2,3,4,5,6
# r1=add(a,b)
# r2=add(c,d)
# r3=add(e,f)
# print(r1,r2,r3)

"""
if local and global variable are having same names.than inside function will be given to local variable and outside function ,
priority will be given to global variables 

"""
# def func1():
#     a=5          #local variable
#     print(a)
# a=6              #global variable
# print(a)
# func1()
# print(a)
"""
All Variable created inside functions are local variable.
when we try to change the value of global variable inside function,then new local variable are created,
why?
because in python,whenever we assign a value to a variable in function,then new local variable are created.

if we want to access and modify global variable inside function then we need to use global keywords 

"""
# #New Program
# def func1():
#     global a
#     a=5          #local variable
#     print(a)
# a=6              #global variable
# print(a)
# func1()
# print(a)

# #New Program
# def func1():
#     global a
#     a=5
#     print(a)
# func1()
# print(a)