goods = [
    {"name": "Nivea men", "price": 2500, "category": "Deodorant", "quantity": 20, "date_of_arrival": "25/1/2023"},
    {"name": "Bracelets", "price": 4000, "category": "accessories", "quantity": 45, "date_of_arrival": "17/2/2023"},
    {"name": "Toilet cleaner", "price": 3000, "category": "Toiletries", "quantity": 23, "date_of_arrival": "19/4/2023"},
    {"name": "Hotwheels Complete set", "price": 20000, "category": "Toys", "quantity": 29, "date_of_arrival": "30/5/2023"},
    {"name": "Strawberry jam", "price": 5500, "category": "food", "quantity": 80, "date_of_arrival": "10/7/2023"},
]


def add_goods():
    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()
    price = int(input("Enter price: "))
    date_of_arrival = input("Enter date_of_arrival (dd-mm-yyyy): ")
    quantity = int(input("Enter quantity: "))


    goods.append({
        "name": name,
        "price": price,
        "category": category,
        "date_of_arrival": date_of_arrival,
        "quantity": quantity,
    }) 


    print("name" + " added successfully!\n")

def display_goods():
    print(f"{"==" * 20}\n Market Seller Inventory.\n{"==" * 20}")
    for good in goods:
        print("name:", good["name"],
              "  price: ",  good["price"],
              "  category:", good["category"],
              "  date_of_arrival:", good["date_of_arrival"],
              "  quantity:", good["quantity"])


def calculate_goods():
    total = sum(good["quantity"] for good in goods)
    print("Total number of good in inventory", total)


def search_goods():
    keyword = input("Enter name or category to search: ").strip().lower
    print(f"{"==" * 10}\nSearch Result\n{"==" * 10}")

    found = False
    for good in goods:
        if keyword in goods[{"name"}].lower() or keyword in goods[{"category"}].lower():
            print("name:", goods["category"],
                  "  nategory:", goods["category"],
                  "  price: $" + str(goods["price"]),
                  "  pate:", goods["date_of_arrival"],
                  "  quantity:", goods["quantity"])
            found = True

            if not found:
                print("No matching goods found.")

def main():
    print(f"{"==" * 12}\nMarket Seller Inventory.\n{"==" * 12}")
    while True:
        print(f"1. Add Goods \n2. View Inventory\n3. Calculate Total Number of Goods\n4. Search by Name or Category \n5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_goods()
        elif choice == "2":
            display_goods()
        elif choice == "3":
            calculate_goods()
        elif choice == "4":
            search_goods()
        elif choice == "5":
            print("Existing... Goodbye!\n")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")


main()                                





