string=str(input("Enter a email: "));
if string.count("@")==1 and string.count(".")==1 and string.index("@")<string.index(".") :

    print("The email is valid");
else:

    print("The email is invalid");