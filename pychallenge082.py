line = "This is a line from my favorite poem."
print(line)

while True:
    try:
        init_index = int(input("Enter an initial index: "))
        fin_index = int(input("Enter a final index: "))
        print(line[init_index:fin_index])
        break
    except ValueError:
        print("Error: Needs an integer")
