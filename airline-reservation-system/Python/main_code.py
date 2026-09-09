from support import admin_menu, agent_menu, customer_menu

def main():
    while True:
        choice = input("\nAirline Reservation System\n1. Admin\n2. Agent\n3. Customer\n4. Exit\nChoice: ")
        if choice == "1": admin_menu()
        elif choice == "2": agent_menu()
        elif choice == "3": customer_menu()
        elif choice == "4": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
