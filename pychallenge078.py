shows = ["Friends", "The Big Bang Theory", "Rick and Morty", "How I Met Your Mother"]

print(*shows, sep="\n")

new_show = str(input("What show do you want added on the list? "))
position = int(input("What position do you want it to be placed on?"))

shows.insert(position, new_show)
print(*shows, sep="\n")
