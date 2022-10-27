should_be_upper = str(input("Type something in uppercase: "))
while should_be_upper.isupper() == False:
    print("You typed something in lowercase. Do it again.")
    should_be_upper = str(input("Type something in uppercase: "))
print("Thank you.")
