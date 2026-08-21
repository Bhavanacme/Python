password=str(input("Enter a password: "));
if len(password)>=8 and password.isalnum() :
    print("The password is valid");
else:
    print("The password is invalid");    