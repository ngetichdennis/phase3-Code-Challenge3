from helper import (
    add_customer,
    add_restaurant,
    add_review,
    list_all_customers,
    list_all_reviews,
    list_all_restaurants
    )
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_restaurant()
        elif choice == "3":
            add_review()
        elif choice == "4":
            list_all_customers()
        elif choice == "5":
            list_all_restaurants()
        elif choice == "6":
            list_all_reviews()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
def display_menu():
    print("1. Add customer")
    print("2. Add restaurant")
    print("3. Add review")
    print("4. List all customers")
    print("5. List all restaurants")
    print("6. List all reviews")
    print("7. Exit")

if __name__ == "__main__":
    main()
