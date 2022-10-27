import challenge_tools

subjects = [
    "Math",
    "Science",
    "Geography",
    "Literature",
    "Physical Education",
    "Woodworking",
]
challenge_tools.pretty_print(subjects)
hated = str(input("Which of these subjects you don't like."))
subjects.remove(hated)
challenge_tools.pretty_print(subjects)
