# Implanted Logical Bugs (Java)

This document details the 15 logical bugs intentionally implanted in `Main.java` and `Support.java` for the debugging challenge. None of these will produce syntax errors, but they break the expected functionality of the software.

1. **Admin Login Bug (`Support.java`, line 132)**
   - **Bug:** `if (checkAdmin(pas, uid))`
   - **Effect:** Reverses the user ID and password arguments. The admin won't be able to log in with correct credentials unless they enter them in reverse order.

2. **Add Employee Bug (`Support.java`, line 150)**
   - **Bug:** `addEmployee(newPass, newUser);`
   - **Effect:** Reverses the username and password arguments when adding an employee, storing the ID as the password and vice versa.

3. **Update Data Bug (`Support.java`, line 54)**
   - **Bug:** `bw.write(price + "," + name + "\n");` inside `updateData()`
   - **Effect:** Swaps the order of price and name when writing updated records to `database.csv`, corrupting data format.

4. **Admin Exit Bug (`Support.java`, line 184)**
   - **Bug:** `continue;` instead of `return;`
   - **Effect:** The admin is trapped in the `while` loop when choosing 'Exit' (Option 6).

5. **Employee Login Bypass Bug (`Support.java`, line 219)**
   - **Bug:** `if (checkEmployee(uid, pas) || true)`
   - **Effect:** Bypasses login verification entirely via short-circuit evaluation (`|| true`), allowing any input to successfully log in as an employee.

6. **Customer Cart Item Condition Bug (`Support.java`, lines 326-328)**
   - **Bug:** `if (num != -1) { break; }`
   - **Effect:** Makes it impossible to add multiple items normally. The loop breaks immediately when entering any valid item number instead of breaking on `-1`.

7. **Customer Cart Object Assignment Bug (`Support.java`, lines 335-336)**
   - **Bug:** `item.num = fetched.price; item.price = num;`
   - **Effect:** Assigns the item price to `num` and item index to `price` in `CartItem`.

8. **Customer Cart Total Bug (`Support.java`, line 339)**
   - **Bug:** `totalPrice -= fetched.price;`
   - **Effect:** Subtracts the price of the item from the total instead of adding to it.

9. **Customer Empty Cart Check Bug (`Support.java`, line 350)**
   - **Bug:** `if (!cart.isEmpty())`
   - **Effect:** Inverts the check: claims the cart is empty when `cart` contains items, and tries to print items when `cart` is empty.

10. **Billing Tax Bug (`Support.java`, line 369)**
    - **Bug:** `float tax = totalPrice / 0.18f;`
    - **Effect:** Inflates the tax astronomically by dividing by 0.18 instead of multiplying by 0.18 (18%).

11. **Billing Discount Bug (`Support.java`, line 371)**
    - **Bug:** `if (totalPrice < 1000)`
    - **Effect:** Gives a discount for purchases under $1000 instead of over $1000.

12. **Billing Final Price Bug (`Support.java`, line 379)**
    - **Bug:** `float finalPrice = totalPrice + discount - tax;`
    - **Effect:** Reverses the math: adds the discount and subtracts the tax instead of subtracting discount and adding tax.

13. **Billing Cancel Purchase Bug (`Support.java`, lines 390-391)**
    - **Bug:** `cart.clear(); totalPrice = 0;` outside the confirmation block
    - **Effect:** Shopping cart is reset even if the customer cancels the purchase.

14. **Main Menu Admin/Employee Swap Bug (`Main.java`, lines 25-28)**
    - **Bug:** `case 1:` calls `support.employee();`
    - **Effect:** If the user selects Admin on the main menu, they are shown the Employee interface instead.

15. **Main Menu Customer/Admin Swap Bug (`Main.java`, lines 33-37)**
    - **Bug:** `case 3:` calls `support.admin();`
    - **Effect:** If the user selects Customer on the main menu, they are shown the Admin interface instead.
