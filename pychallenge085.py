vowels = "aeiou"
line = str(input("Enter your name: ")).lower()

count = {}

for i in "aeiou":
    exists = line.count(i)
    count[i] = exists

count_values = count.values()
total_vowels = sum(count_values)


print(f"You have this many vowels in your name: {total_vowels}")
