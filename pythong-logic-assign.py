marks = 77

if marks >= 50:
    print("pass")
else:
    print("fail")


has_ID = True
age = int (input ("Age of user:"))
print(age)

if has_ID and age >= 18:
    print("entry allowed")
else:
    print("entry denied")




balance = int(input("Enter balance:"))
print(balance)
withdrawal = int(input("Enter withdrawal amount:"))
print(withdrawal) 

verification = True

if verification and withdrawal <= balance:
    print("withdrawal succesful")
else:
    print("withdrawal failed")