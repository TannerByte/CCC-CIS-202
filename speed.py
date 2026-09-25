age = int(input("Enter your age: "))

if age < 3:
    print("Your ticket is free.")
elif age <= 12:
    print("Your ticket price is $10.")
elif age <= 22:
    print("Your ticket price is $15.")
elif age <= 64:
    print("Your ticket price is $20.")
else:
    print("Your ticket price is $12.")
