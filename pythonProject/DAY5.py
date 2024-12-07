"""
Which values are called False values?
1.0
2.None
3.False
4.Empty values

Operators:
1. Arithmetic operators
2.Comparison Operators
3.Logical Operators: 3type
Generally return True or False.Generally used to check multiple
conditions: Generally works on bool values
and : when both inputs are True ,Output will be true
or  :when one of the inputs is True, output is True
not :it will toggle the input. True will be converted to False


case 2: When we use logical Operator on non bool values
and operator: if first value is False output will be first value else output will be second value
or operator: if first value is True output will be first value else output will be second value

"""

#new program
# a=5
# b=7
# r=(a==5 and b==7)
# print(r)

# user_id=input("Enter user ID: ")
# pwd=input("Enter the pwd:")
# print(user_id=="Santosh" and pwd=="12345")


# new program
# a=5
# b=7
# r=not(a==5 and b==7)
# print(r)

# x=5
# y=7
# print(x and y)

# print(not(0))
# print(not(False))
# print(not(None))
# print(not([]))
# print(not(""))

# x=5
# y=7
# print(x or y)

# x=0
# y=7
# print(x or y)

"""
Bitwise Operators:6 is the lucky number
& Bitwise And :Both input bits 1 then output 1
| Bitwise Or :One of the input bit is 1 output 1
~ Bitwise Not:Toggle,Input 1 Output 0
^ Bitwise Xor :Both input are same than output is 1 else output is 0
<< Bitwise Shift Left (with G) :each bit is will be shifted to left and leftmost bil will be filled by 0and rightmost bit will be discarded
>> Bitwise shift Right (with Sign):MSB(Most significant bit) rightmost bit is sign bit :each bit is shifted to right and left most bit is kept the sane ie leftmost bit is filled with sign bit only and rightmost bit is discarded
r=a << b means a will be shifted to left b times
"""
# x=5     #00000101
# y=6     #00000110
# r=x & y #00000111
# print(r)           #4

#new program
# x=5     #00000101
# y=6     #00000110
# r=x | y #00000111  #7
# print(r)

# a=3
# b=2
# r=a << b
# print(r)

"""
Assignment Operators:There are 14 Assignment operator
a.Equal to 
b. Arithmetic Operator 
c.Bitwise operators other than not(~)
d.walrus

= Equal to
+= plus Equal to  a+=b means a = a +b
-=
*=
/=
%=
**=
//=
&= and Equal to
|=
^= 
<<= a*=b mean a = a ** b
>>= Shift right equal to 
:=  walrus Operator : Launched in Python 3.8 version 

In python ,all variables are of reference type.when we assign one variable to another then address of RHS variable is assigned to LHS Variable 
"""
#new program
# a=5    #say a address is 1000
# b=a    #b address will also become 1000
# print(a,b)
# print(id(a),id(b))

#New Program
# a=5
# b=7
# a+=b    #a=a+b
# print(a)
#
# a=5
# b=7
# a**=b    #a=a**b
# print(a)

# a=3
# b=2
# a<<=b    #a=a<<b
# print(a)

#New Program
# a=5
# a+=1
# print(a)
# a+=1
# print(a)

#new program
# print(a=5)  #Error

# print(a:=5)  #Expration operator


"""
Identity Operators:
is      Return True if same address else False
is not  Return False if same address else True

"""
#new program
# a=5
# b=a
# print(a is b)
# print(id(a),id(b))

# a=5
# b=7
# print(a is b)
# print(id(a),id(b))

# a=5
# b=7
# print(a is not b)
# print(id(a),id(b))


"""
Membership Operator: Check whether the element /sub data is part of the main data or main iterator
in       If member then True else False
not in   If  not member then False else True
"""
# L=[10,20,30,40,50,60,70,80,90,100]
# E=50
# print(E in L)
# print(E not in L)

#new program
# e= "abc"
# s="adhoifosoasbvcnkfhkjkkjdkgeig"
# print()