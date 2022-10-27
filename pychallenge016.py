response = str.lower(input("Is it raining today? Yes or no? "))
if response == "yes":
    response2 = str.lower(input("Is it windy today? Yes or no? "))
    if response2 == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")
