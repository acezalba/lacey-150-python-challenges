import challenge_tools

sports_list = ["Basketball", "Archery"]
sports_list.append(str(input("What is your favorite sport?")))
challenge_tools.pretty_print(sorted(sports_list))
