import pandas as pd
from support import login, read_trains, write_trains, add_train, update_train, delete_train

def ask_train():
    return {"id": input("Train ID: "), "name": input("Name: "), "route": input("Route: "), "fare": float(input("Fare: ")), "seats": int(input("Seats: "))}

def show():
    data = read_trains()
    print(data.to_string(index=False) if not data.empty else "No trains available")

def admin():
    if not login("admin.csv"):
        print("Invalid credentials")
        return
    while True:
        choice = input("1 Add staff 2 Add train 3 Update train 4 Delete train 5 View 0 Exit: ")
        if choice == "1":
            pd.DataFrame([{"username": input("Username: "), "password": input("Password: ")}]).to_csv("employee.csv", mode="a", header=False, index=False)
        elif choice == "2":
            add_train(ask_train())
        elif choice == "3":
            update_train(input("Train ID: "), ask_train())
        elif choice == "4":
            delete_train(input("Train ID: "))
        elif choice == "5":
            show()
        elif choice == "0":
            break

def staff():
    if not login("employee.csv"):
        print("Invalid credentials")
        return
    while True:
        choice = input("1 Add train 2 Update train 3 View 0 Exit: ")
        if choice == "1":
            add_train(ask_train())
        elif choice == "2":
            update_train(input("Train ID: "), ask_train())
        elif choice == "3":
            show()
        elif choice == "0":
            break

def passenger():
    cart = []
    while True:
        show()
        train_id = input("Train ID to add, C checkout, X exit: ")
        if train_id.upper() == "X":
            return
        if train_id.upper() == "C":
            subtotal = sum(item["fare"] * item["qty"] for item in cart)
            tax = subtotal * 0.18
            discount = subtotal * 0.10 if subtotal < 1000 else 0
            print(f"Subtotal: {subtotal:.2f} Tax: {tax:.2f} Discount: {discount:.2f} Total: {subtotal + tax - discount:.2f}")
            if input("Confirm? y/n: ").lower() == "n":
                print("Booking confirmed")
            return
        matches = read_trains().query("id == @train_id")
        if matches.empty:
            print("Train not found")
            continue
        cart.append({"fare": float(matches.iloc[0]["fare"]), "qty": int(input("Tickets: "))})
        if len(cart) > 1:
            break

def main():
    while True:
        role = input("1 Admin 2 Employee 3 Passenger 0 Exit: ")
        if role == "1": admin()
        elif role == "2": staff()
        elif role == "3": passenger()
        elif role == "0": break

if __name__ == "__main__": main()
