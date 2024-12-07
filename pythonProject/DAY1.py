"""GOOD MORNING
# What is Python?
**python is both compiled and interpreted,object-oriented,high level programing language with dynamic semantics.**

# What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

# Why Python:
- 1. Easy Syntax, More English Like Language
- 2. Open Source
- 3. Big Community
- 4. Platform Independent
- 5. Vast Library Set: 2.35 Lakes + Libraries/Packages: Billions of Predefined Functions
- 6. High Level Language
- 7. Python supports modular approach of programming: We can divide the project into modules and finally interface all modules
- 8. Python is used in versatile domains:
    Data Driven Domains: DA, ML, DL, IP, NLP, DS, AI....
    Other Domains: Web Applications, Mobile Applications, IOT, CyberSecurity, Network Security, ....
- 9. Interpreter Based Language: Code Line by Line Execute
- 10. Python supports Dynamic Data Type Definition: Data Type Definition at Run Time
- 11. Python supports Dynamic Memory Allocation: Memory Allocation at Run Time

**C Lang and Java supports compile time data type definition and compile time memory allocation**

Platform Independent:  If we write our code on one OS and if the same code, without any change can be
executed on any other OS also then we say our language or technology is platform independent: This is
the wrong definition. This is the definition of Portability
Portable: WORA: Write Once Run Anywhere

Platform Independent: CORA: Compile Once Run Anywhere: If we write our code on one OS and compile it,
After compilation if our compiled code can be executed on any OS then we say our langauge or technology
is platform independent.

If we open a C Lang, Java, Python file in Notepad or any text editor whether code will be human
understandable? Yes

If we open  the compiled file of C Lang, Java, Python in Notepad or any text editor whether code will be human
understandable? No

Compiled Code: Compiled Code is an intermediate code which is more close to hardware and runs at a fast
speed.

#### Why we compiled Code

Whether we can create a compiled file in Python: Yes
We have ready-made libraries in Python through which we can create compile code of Python. Extension
of Python Compiled Code file is .pyc (Python Compiled File)

Interpreter vs Compiler
Interpreter: Line by Line Code Execution. Means line by line errors are checked, Line by Line memory
is allocated and line by line program is executed
Compiler: Firstly completed code is compiled means errors are Checked in the code, memory is allocate
and code becomes in object code format.

#### Drawbacks:
- 1. Pythons consumes a lot of memory
- 2. Python is a slow processing language

Python interpreter based
C, Java: Compiler Based

Python supports dynamic data type definition: ie data type definition at run time: We can pass any type
of data in a variable in the same program
Dynamic Memory Allocation: ie Memory Allocation at run time.

How much memory is consumed by int in C Lang?  It depends on the compiler: 2 Bytes of 4 Bytes
1 Byte= 8 Bits
16 Bits Biggest Value in Binary: 1111111111111111: Signed and Unsigned
Say 2 bytes int, C Lang: Int range: -32768 to +32767

How much memory is consumed by int in python ?it depends on the value

"""
# print("hello world")
# print("Good morning sir,Thankyou for this opportunity , my name is santosh , I am pursuing MCA form Indira Gandhi national open university ,I am skilled in programing language and I have good knowledge of python mysql excel or power bi ")
# print("abc")
# print(abc)
# # print("i a the best")

# new program
# a=5
# a1=2.5

# new program
# a=5
# print(a)
# a=55555555555555555555555555555555555555555
# print(a)

"""
# Arithmetic operators

- Python provides **operators**, which are special symbols that represent computations like addition and multiplication.

- The operators +, -, and * perform addition, subtraction, and multiplication, as in the following examples:
"""
# #Addition
#  print("Addition of 12 & 34 is  ",12+34)
#
# #Subtraction
# print("Subtraction of 12 & 34 is ",34-12)
#
# #multiplication
# print("multiplication of 12 & 34 is ",12*34)
#
# #Division
# print("Division of 12 & 34 is ",34/12)
#
# #integer division
# print("Integer Division of 12 & 34 is  ",34//12)
#
# #Modulus
# print("Modulus of 12 & 34 is ",12%34)
#
# #power/Exponent
# print("Power/Exponent of 12 & 4",12**4 )
#
# #add
# print("Modulus of 12 & 34",48**8)
#
# **Things are calculated in the same order as in math. The parentheses(and) also work the same way.**
# 1+2+4/2*5
# (1+2+3)/2*5
#
# #PEMDAS
# (1+2)*5
# # Exception
# # Order of associativity
# # Exponentiation(**) & Assignment operator "=""
#
# # 2**3**2
# 2**3**2**2
# 2**4
# 2*8
# 2-3
# Comments
"""
- A comment is basically a text note that gives an explanation about the source code.
- They act as documentation in the source code.
- Comments increases the readability of the program.
- Comments make it easy for the programmer to remember the complex things added to the code.
- They describe what a function does, or explain the working of a particular block of code.

## Types of comments

**1. Line Comments**

These are basically the single-line comment.

**2. Block Comments**

These are the multi-line comment.

## Writing comments in Python

**In python, we use the # symbol for writing the comments**

The single-line comments use a single # symbol. For example:
#HELLO PYTHON
#ctrl+/
#in python,we use the

**The multi-line comments either use a single # symbol or string literal '''...'''/""" """. For example:**

# A comment is basically a text note that gives an 
# explanation about the source code.
# They act as documentation in the source code.
# Comments increases the readability of the program.
# Comments make it easy for the programmer to remember 
# the complex things added to the code.
# They describe what a function does, or explain the 
# working of a particular block of code.

print("example of a multiline comment")

'''
A comment is basically a text note that gives an 
explanation about the source code.
They act as documentation in the source code.
Comments increases the readability of the program.
Comments make it easy for the programmer to remember 
the complex things added to the code.
They describe what a function does, or explain the 
working of a particular block of code.
'''

print("another example of a multiline comment")

'''my name is santosh i am pursuing mca i am mature and bold i have talent of drawing i like to try new things right now i do job hunting i have fate for myself to achieve my job '''

"""
