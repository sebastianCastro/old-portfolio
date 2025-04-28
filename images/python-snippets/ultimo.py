user = {"userName": "me", "password": "123"}
# opcional method
# user = {}
# user["userName"] = {"me"}
# user["password"] = {"123"}
attempts = 0
while attempts < 3:
    userInput = input("User Name")
    passwordInput = input("Password")
    if userInput.lower() in user["userName"] and passwordInput in user["password"]:
        print("Logged in")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Sorry but your username or password might be incorrect, please try again")
        else:
            print("Sorry you exceed the number times to log in, please try again later")
