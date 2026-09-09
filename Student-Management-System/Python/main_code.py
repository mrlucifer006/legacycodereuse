import support

def main():
    print("Welcome to Student Management System")
    print("1. Admin\n2. Teacher\n3. Student\n4. Exit")
    try:
        choice = int(input("Choose role: "))
        if choice == 1:
            support.admin_menu()
        elif choice == 2:
            support.teacher_menu()
        elif choice == 3:
            support.student_menu()
        elif choice == 4:
            return
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
