            #    PYTHON 

#  print in the different lines
print("hello")
print("world")

#  print int the same line
print("hello","world")

#  print digits
print(23)
print(45)

#  add two number
print(2+3)

#  declaring variables
name = "achyauta"
age = 23
price = 25.99
a = None
old= False
print("my name is",name)
print("my age is",age)
print(a)
print(old)

#  assigning variables value to new variable
age2 = age
print(age2)

#  type keyword define the type of value .like  int,string,none, float, boolean
print(type(age))
print(type(name))
print(type(price))
print(type(a))
print(type(old))

#  keywords are the reserved keywords
# False,none,True,lambda
#  python are case sensitive language
#  python is implicit.

# PRINT SUM OF TWO NUMBER
a= 10
b = 3
sum = a+b
print(sum)  


# Types of Tokens
#  1) punctuators = are the symbols to organise the sentence structure in programming  (),[],{},#,@ etc.

#  EXPRESSION EXECUTION

#  String & numeric values can operate together with * .
A,B = 2,3
txt = "@"
print(2*txt*3)
#   String & String can operate with + .
a,b = "2",3
txt = "@"
print((a+txt)*b) 

#  Numeric values can operate with all arithmetic oprators
a,b  =2,3
c =4
print("the value is",a+b*c)
 
#  Arithmetic expression with integer and float will result in float
a,b = 10,5.0
c = a*b
print(c)

# result of division with two integer will be float
a,b = 1,2
c = a/b
print(c)

#  Integer division with float and int will give int displayed as float
a,b = 1.5,3
c = a//b
print(c)
print(type(c))
#  Result of  (a//b) is same as floor(a/b)
#  floor gives closest integerich is lesse ,which is lesser than or equal to the float value
#  remainder is negative when denominator is negative

#  Comments 
# 1) single line code

# inputs in python
# input() statement is used to accept values (using keyboard) from users
# 1) string input   ex = 
name = input("name : ")
print(name)

# integer input
age = int(input("age : "))
print(age)

#  float input
price = float(input("price : "))
print(price)    

#  Conditional statement

# if(condition):
#     Statement1
# elif(condition):
#     Statement2
# else:
#     Statement3

light = input("light :")
if(light == "red"):
    print("stop")
elif(light =="yellow"):
    print("ready")
elif(light =="green"):
    print("go")
else:
    print("light is broken")
    
    #  Single line if / Ternary operator
    # <var> = <val1> if <condition> else <val2>
    food = input("food :")
    eat ="yes" if food == "cake" else "no"
    print(eat)
    
    #  stt1> if <condition> else <stt2>
    food =input("food : ")
    print("sweet") if food == "cake" or food =="jalebi" else print("not sweet")    
    
    # type conversion
    a= 4
    b = 2.153
    sum = a+b
    print(" the sum is",sum)
    
    # type casting
    a = 1
    c = int("2")
    print(type(c))
    print(a+c)
    
    # input in python
    name  = str(input("enter your name"))
    print("welcome",name)
    
    