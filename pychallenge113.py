import csv

file = list(csv.reader(open("Books.csv")))
entries = int(input("How many records do you want to add to the list?"))

for i in range(entries):
    print(f"Enter entry no. {i+1}")
    book = str(input("Enter new book: "))
    author = str(input(f"Enter author of {book}: "))
    year = int(input(f"Enter year {book} was published: "))
    temp = []
    temp.append(book)
    temp.append(author)
    temp.append(year)
    file.append(temp)

checkAuthor = str(input("Enter an author to show entries in their name: "))
checkAuthorIndex = 0

for row in file:
    if row[1] == checkAuthor:
        print(row)
        checkAuthorIndex = checkAuthorIndex + 1

if checkAuthorIndex == 0:
    print(f"No entries for {checkAuthor} available")
