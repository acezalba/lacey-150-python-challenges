# /usr/bin/env python3

import string

"""
Shift Code

Constraints:
- Spacing and punctuation is preserved
- Case is preserved
"""

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)


def shifter(line, offset):
    """
    The shift cipher
    Args:
    line - line to shift
    offset - distance from character position

    Returns the encoded string
    """
    string_to_encode = list(line)
    encoded_string = ""
    for x in string_to_encode:
        if x in uppercase:
            encoded_string = (
                encoded_string + uppercase[(uppercase.index(x) + offset) % 26]
            )
        elif x in lowercase:
            encoded_string = (
                encoded_string + lowercase[(lowercase.index(x) + offset) % 26]
            )
        else:
            encoded_string = encoded_string + x

    return encoded_string


def encode():
    """
    Encodes the message
    """
    # Ask for string
    string = str(input("Enter string to encode: "))
    # Ask for a number to shift the message
    shift = int(input("Enter number of places to shift: "))
    # Output the encoded string
    print(f"This is the coded string: \n\n>> {shifter(string, shift)}")


def decode():
    """Decode the message"""
    # Ask for the string
    string = str(input("Enter string to decode: "))

    # Ask for a number to unshift a message
    unshift = -(int(input("Enter number of places to unshift: ")))

    # Output the decoded string
    print(f"This is the decoded string: \n\n>> {shifter(string, unshift)}")


def menu():
    """Define the menu loop

    Args:
        None
    """

    # Display the choices
    print(
        "\nShift Code:\n \
  1) Make a code\n \
  2) Decode a message\n \
  3) Quit\n "
    )
    choice = input("What do you want to do? ")

    if choice == "1":
        encode()
        return True
    elif choice == "2":
        decode()
        return True
    elif choice == "3":
        return False  # Terminate the loop
    else:
        print("Choice not recognized.\n")
        return True


# Define the main loop
def main():
    while menu():
        continue
    print("Exiting")
    exit()


# Run main
main()
