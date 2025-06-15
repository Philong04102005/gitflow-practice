userName = input("Enter your username: ")
passWord = input("Enter your password: ")

if userName == "admin" and passWord == "password123":
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")
    exit()