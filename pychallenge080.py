user_fname = str(input("Enter your first name: "))
print(f"The length of your first name is: {len(user_fname)}")
user_lname = str(input("Enter your last name: "))
print(f"The length of your last name is: {len(user_lname)}")
full_name = user_fname + " " + user_lname
print(
    f"Your full name is {full_name}. The length of your full name is {len(full_name)}"
)
