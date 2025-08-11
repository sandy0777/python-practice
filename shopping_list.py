# shopping_list.py

def show_menu():
    print("\nShopping List Menu:")
    print("1. Show List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Quit")

def main():
    shopping_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if shopping_list:
                print("\nYour shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == "2":
            item = input("Enter an item to add: ")
            shopping_list.append(item)
            print(f'"{item}" added to your list.')

        elif choice == "3":
            item = input("Enter an item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed from your list.')
            else:
                print(f'"{item}" not found in your list.')

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
