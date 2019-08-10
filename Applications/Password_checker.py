crrt_psswd = "Password"
name = input("Enter your Name: ").capitalize()
sur_name = input("Enter your Last name: ").capitalize()
message = "Hello %s %s,Please enter password to proceed" %(name,sur_name)
print(message)
password = input("Password: ")
while password != crrt_psswd:
    password = input("Wrong Password. Enter again! ")
print("\nWelcome, User Logged in")