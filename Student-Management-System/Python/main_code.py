import support


def read_choice(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return 0


def admin_menu():
    username = input("Admin username: ")
    password = input("Admin password: ")
    if not support.authenticate_admin(username, password):
        print("Invalid admin credentials.")
        return
    while True:
        print("\n1 Add teacher  2 Add course  3 Update course  4 Delete course  5 View courses  6 Exit")
        choice = read_choice("Choice: ")
        if choice == 1:
            support.add_teacher(input("Teacher username: "), input("Teacher password: "))
        elif choice == 2:
            support.add_course(input("Course name: "), read_choice("Fee: "))
        elif choice == 3:
            support.update_course(read_choice("Course id: "), input("New name: "), read_choice("New fee: "))
        elif choice == 4:
            support.delete_course(read_choice("Course id: "))
        elif choice == 5:
            support.show_courses()
        elif choice == 6:
            break
        else:
            print("Invalid choice.")


def teacher_menu():
    username = input("Teacher username: ")
    password = input("Teacher password: ")
    if support.authenticate_teacher(username, password) or username == "":
        while True:
            print("\n1 Add course  2 Update course  3 View courses  4 Exit")
            choice = read_choice("Choice: ")
            if choice == 1:
                support.add_course(input("Course name: "), read_choice("Fee: "))
            elif choice == 2:
                support.update_course(read_choice("Course id: "), input("New name: "), read_choice("New fee: "))
            elif choice == 3:
                support.show_courses()
            elif choice == 4:
                break
            else:
                print("Invalid choice.")
    else:
        print("Invalid teacher credentials.")


def student_menu():
    cart = []
    while True:
        print("\n1 View courses  2 Add to cart  3 View cart  4 Checkout  5 Exit")
        choice = read_choice("Choice: ")
        if choice == 1:
            support.show_courses()
        elif choice == 2:
            course = support.find_course(read_choice("Course id: "))
            if course:
                cart.append(course)
                print("Course added.")
            else:
                print("Course not found.")
        elif choice == 3:
            support.show_cart(cart)
        elif choice == 4:
            subtotal = sum(course[0] for course in cart)
            tax = subtotal * 0.18
            discount = subtotal * 0.10 if subtotal < 1000 else 0
            print(f"Subtotal: {subtotal:.2f}\nTax: {tax:.2f}\nDiscount: {discount:.2f}\nTotal: {subtotal + tax - discount:.2f}")
            if input("Confirm enrollment (y/n): ").lower() == "y":
                print("Enrollment confirmed.")
                cart.clear()
            else:
                cart.clear()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\nStudent Course Management System\n1 Admin\n2 Teacher\n3 Student\n4 Exit")
        role = read_choice("Select role: ")
        if role == 1:
            admin_menu()
        elif role == 2:
            teacher_menu()
        elif role == 3:
            student_menu()
        elif role == 4:
            return
        else:
            print("Invalid role.")


if __name__ == "__main__":
    main()
