import csv

books = [
    ["To Kill a Mockingbird", "Harper Lee", "1960"],
    ["A Brief History of Time", "Stephen Hawking", "1988"],
    ["The Great Gatsy", "F. Scott Fitzgerald", "1922"],
    ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"],
    ["Pride and Prejudice", "Jane Austen", "1813"],
]

with open("Books.csv", "w", newline="") as file:
    csvWriter = csv.writer(file)
    for row in books:
        csvWriter.writerow(row)
