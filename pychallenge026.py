vowels = {"a", "e", "i", "o", "u"}

pig_word = str(input("Enter any given word: ").lower())
pig_length = int(len(pig_word))

if pig_word[0] in vowels:
    print(pig_word + "way")
else:
    print(pig_word[1:pig_length] + pig_word[0] + "ay")
