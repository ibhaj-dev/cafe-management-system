def show_menu():
    print("\n☕ ---- CAFE MENU ----")
    print("1. Coffee  - ₹80")
    print("2. Tea     - ₹30")
    print("3. Burger  - ₹120")
    print("4. Pizza   - ₹200")


def take_order():
    total = 0

    while True:
        choice = input("\nEnter item number (or 'done' to finish): ")

        if choice == "done":
            break

        if choice == "1":
            qty = int(input("Quantity: "))
            total += 80 * qty

        elif choice == "2":
            qty = int(input("Quantity: "))
            total += 30 * qty

        elif choice == "3":
            qty = int(input("Quantity: "))
            total += 120 * qty

        elif choice == "4":
            qty = int(input("Quantity: "))
            total += 200 * qty

        else:
            print("Invalid choice ❌")

    return total


def calculate_bill(total):
    print("\n🧾 ----- BILL -----")
    print(f"Total Amount: ₹{total}")

    if total > 300:
        discount = total * 0.1
        print(f"Discount Applied: ₹{discount}")
        total -= discount

    print(f"Final Amount: ₹{total}")
    print("-------------------")


def main():
    print("🔥 WELCOME TO CAFE MANAGEMENT SYSTEM 🔥")

    show_menu()
    total = take_order()
    calculate_bill(total)

    print("\nThank you for visiting ☕❤️")


if __name__ == "__main__":
    main()