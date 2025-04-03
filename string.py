#   strings = is a datatype that stores a sequence of characteers
#  BASIC OPERATIONS ARE:
# Concatenate = "hello"+"world"
#  length of str =len(str)


str1 = "this is string . we \t are learning python \n hello world"
str2 ='this is string'
print(str1)
print(str2)
final_str = str1+str2
print(final_str)
print(len(final_str))

# indexing isdex  used to access a particular element in a string
# Slicing = Acessing part of a string
# syntax = str[starting_index : ending_index] and ending_index not included.
#  negative index slicing can be done in the python
print(str2[1:4])
print(str2[0:len(str2)])

str= "apple"
print(str[-1])
print(str[-3:-1]) 

#  string functions
# str.endswith("er") = returns true if string ends with substr 
# str.capitalize() = capitalize 1st character
# str.replace (old,new)  = replaces all occurences of old with new
# str.find(word) = returns 1st index of 1st occurrence
# str.count("am") = counts the occurence of substr in string

str_1 = "achyauta"
print(str_1.replace("a","o"))

#  it will the number of times a will apppear
print(str.count("a"))


name = input("enter your name")
print(len(name),"the length is")