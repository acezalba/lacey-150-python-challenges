sales_table = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
}

for salesperson, sales in sales_table.items():
    print(salesperson, ":", sales)

salesperson = str(input("Whose record do you want to check: "))
region = str(input("In which region (N,S,E,W): "))
print(
    f"{salesperson}'s sales for region {region} is {sales_table[salesperson][region.upper()]}"
)
change = str(input("Do you want to change it? (yes or no): "))

if change.lower() == "yes":
    new_value = int(input("Enter the new sales record: "))
    sales_table[salesperson][region] = new_value
    print(
        f"{salesperson}'s new sales for region {region} is {sales_table[salesperson][region.upper()]}"
    )

if change.lower() == "no":
    print("Thank you.")
