shoe_customers = {}

for i in range(4):
    customer_record = {}
    customer_name = str(input(f"Enter name of customer {i+1}: "))
    customer_age = int(input(f"Enter age of customer {i+1}, {customer_name}: "))
    customer_shoesize = str(input(f"Enter the shoe size: "))
    shoe_customers[customer_name] = {"age": customer_age, "shoesize": customer_shoesize}

for customer, record in shoe_customers.items():
    print("Age of", customer, ":", record["age"])
