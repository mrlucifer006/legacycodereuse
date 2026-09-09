# Implanted Logical Bugs (C)

This document details the 15 logical bugs intentionally implanted in `main.c` and `support.c` for the debugging challenge. None of these will produce syntax errors, but they break the expected functionality of the software.

1. **Admin Login Bug (`support.c`, line 137)**
   - **Bug:** `if (check_admin(pas, uid))`
   - **Effect:** Reverses the user ID and password arguments. The admin won't be able to log in with correct credentials unless they enter them in reverse order.

2. **Add Employee Bug (`support.c`, line 154)**
   - **Bug:** `add_employee(new_pass, new_user);`
   - **Effect:** Reverses the username and password arguments when adding an employee, storing the ID as the password and vice versa.

3. **Update Data Bug (`support.c`, line 54)**
   - **Bug:** `fprintf(temp, "%d,%s\n", price, name);` inside `update_data()`
   - **Effect:** Swaps the order of price and name when writing updated records to `database.csv`, corrupting data format.

4. **Admin Exit Bug (`support.c`, line 185)**
   - **Bug:** `continue;` instead of `break;` (or `return;`)
   - **Effect:** The admin is trapped in the `while` loop when choosing 'Exit' (Option 6).

5. **Employee Login Bypass Bug (`support.c`, line 222)**
   - **Bug:** `if (check_employee(uid, pas) || 1)`
   - **Effect:** Bypasses login verification entirely via short-circuit evaluation (`|| 1`), allowing any input to successfully log in as an employee.

6. **Customer Cart Item Condition Bug (`support.c`, lines 321-323)**
   - **Bug:** `if (num != -1) { break; }`
   - **Effect:** Makes it impossible to add multiple items normally. The loop breaks immediately when entering any valid item number instead of breaking on `-1`.

7. **Customer Cart Struct Assignment Bug (`support.c`, lines 331-332)**
   - **Bug:** `cart[cart_count].num = item_price; cart[cart_count].price = num;`
   - **Effect:** Assigns the item price to the item index/number property and item index to the price property in `struct CartItem`.

8. **Customer Cart Total Bug (`support.c`, line 334)**
   - **Bug:** `total_price -= item_price;`
   - **Effect:** Subtracts the price of the item from the total instead of adding to it.

9. **Customer Empty Cart Check Bug (`support.c`, line 346)**
   - **Bug:** `if (cart_count != 0)`
   - **Effect:** Inverts the check: claims the cart is empty when it has items, and tries to print items when the cart is actually empty.

10. **Billing Tax Bug (`support.c`, line 365)**
    - **Bug:** `float tax = total_price / 0.18;`
    - **Effect:** Inflates the tax astronomically by dividing by 0.18 instead of multiplying by 0.18 (18%).

11. **Billing Discount Bug (`support.c`, line 367)**
    - **Bug:** `if (total_price < 1000)`
    - **Effect:** Gives a discount for purchases under $1000 instead of over $1000.

12. **Billing Final Price Bug (`support.c`, line 375)**
    - **Bug:** `float final_price = total_price + discount - tax;`
    - **Effect:** Reverses the math: adds the discount and subtracts the tax instead of subtracting discount and adding tax.

13. **Billing Cancel Purchase Bug (`support.c`, lines 387-388)**
    - **Bug:** `cart_count = 0; total_price = 0;` outside the `if (confirm == 'y')` block
    - **Effect:** Shopping cart is reset even if the customer cancels the purchase.

14. **Main Menu Admin/Employee Swap Bug (`main.c`, lines 22-25)**
    - **Bug:** `case 1:` calls `employee();`
    - **Effect:** If the user selects Admin on the main menu, they are shown the Employee interface instead.

15. **Main Menu Customer/Admin Swap Bug (`main.c`, lines 30-34)**
    - **Bug:** `case 3:` calls `admin();`
    - **Effect:** If the user selects Customer on the main menu, they are shown the Admin interface instead.
