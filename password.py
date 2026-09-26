#simple log in tool
#can only  attempt three times
#password is poop
#if fails three times print "account locked"

password = "POOP"
attempts = 0

while attempts < 3:
    user_input = input("Please enter your password: ")

    if user_input == password:
        print("Welcome!")
        break
    else:
        attempts += 1

        if attempts == 3:
            print("ACCOUNT LOCKED")
        else:
            print("Please try again")
