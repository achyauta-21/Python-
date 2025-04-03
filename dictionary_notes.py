# Dictionary
# dictionary are used to store data values in key:value pairs
# They are unordered,mutable(changeable) & dont,allow duplicate keys
#  "key":value,
dict={
    "name": "achyauta",
    "cgpa":9.5,
    "marks":[97,98,95],
    "score":{                # NESTED DICTIONARY
        "chem":45,
        "math": 35,
    }
        
}
print("hi")
print (len(list(dict.keys())))



dict["name"] = "shradhakhapra"  # overwrite
dict["surname"] = "nand"
print(dict)
print(type(dict))

#  creating null dictionary
dict = {}
print(dict)

#  DICTIONARY METHODS
# myDict.keys()
#  myDict.values()
# myDict.items()
# myDict.get("key")
# myDict.update(newDict)

student = {
    "name": "rahul kumar",
    "subject" :{
        "physics":98,
        "chemistry" :54,
        "maths": 96
            }
}
student.update({"city":"delhi"})
print(student)


