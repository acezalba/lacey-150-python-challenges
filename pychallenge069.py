import challenge_tools

countries = ("Belgium", "New Zealand", "Australia", "Switzerland", "Germany")
string_countries = challenge_tools.pretty_list_string(countries)
check_string = input(f"Enter one of these countries: {string_countries}\n>> ")
print(countries.index(check_string))
