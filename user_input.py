message= input("enter name:")
print(message)

#int() is used to accept numerical values

age= input("how old are you?")
age = int(age)
if age >= 18:
    print(f"you are {age}, that is old enough")
else:
    print("not old enough")
