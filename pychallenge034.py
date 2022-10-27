choice = int(input("1) Square\n2) Triangle\n\nEnter a number: "))
if choice == 1:
    square_side = int(input("Give me the length of a side of a square: "))
    print("Area of the square is:", 4 * square_side)
elif choice == 2:
    triangle_base = float(input("Give me the base of the triangle: "))
    triangle_height = float(input("Give me the height of the triangle: "))
    print("Area of the triangle is:", (triangle_base * triangle_height) / 2)
else:
    print("Choice isn't available.")
