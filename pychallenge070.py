import challenge_tools

countries = ("Belgium", "New Zealand", "Australia", "Switzerland", "Germany")
string_countries = challenge_tools.pretty_list_string(countries)

while True:
    try:
        check_string = str(
            input(f"Enter one of these countries: {string_countries}\n>> ")
        )
        print(countries.index(check_string))
        break
    except ValueError:
        print("Error: Enter a string.")

while True:
    try:
        check_index = int(input("Enter an index to return a country from the list: "))
        print(countries[check_index])
        break
    except IndexError:
        print("Error: index not on list")
