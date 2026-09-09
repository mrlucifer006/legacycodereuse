# Implanted Logical Bugs (C++)

This document details the 15 logical bugs intentionally implanted in `main.cpp` and `support.cpp` for the debugging challenge. None of these will produce syntax errors, but they break the expected functionality of the software.

1. **Admin Login Bug (`support.cpp`, line 132)**
   - **Bug:** `if (check_admin(pas, uid))`
   - **Effect:** Reverses the user ID and password arguments. The admin won't be able to log in with correct credentials unless they enter them in reverse order.

2. **Add Employee Bug (`support.cpp`, line 149)**
   - **Bug:** `add_employee(new_pass, new_user);`
   - **Effect:** Reverses the username and password arguments when adding an employee, storing the ID as the password and vice versa.

3. **Update Data Bug (`support.cpp`, line 53)**
   - **Bug:** `temp << price << "," << name << "\n";` inside `update_data()`
   - **Effect:** Swaps the order of price and name when writing modified records to `database.csv`, corrupting data format.

4. **Admin Exit Bug (`support.cpp`, line 180)**
   - **Bug:** `continue;` instead of `break;` (or `return;`)
   - **Effect:** The admin is trapped in the `while` loop when choosing 'Exit' (Option 6).

5. **Employee Login Bypass Bug (`support.cpp`, line 217)**
   - **Bug:** `if (check_employee(uid, pas) || 1)`
   - **Effect:** Bypasses login verification entirely via short-circuit evaluation (`|| 1`), allowing any input to successfully log in as an employee.

6. **Customer Cart Item Condition Bug (`support.cpp`, lines 315-317)**
   - **Bug:** `if (num != -1) { break; }`
   - **Effect:** Makes it impossible to add multiple items normally. The loop breaks immediately when entering any valid item number instead of breaking on `-1`.

7. **Customer Cart Struct Assignment Bug (`support.cpp`, lines 326-327)**
   - **Bug:** `item.num = item_price; item.price = num;`
   - **Effect:** Assigns the item price to `num` and item index to `price` in `CartItem`.

8. **Customer Cart Total Bug (`support.cpp`, line 330)**
   - **Bug:** `total_price -= item_price;`
   - **Effect:** Subtracts the price of the item from the total instead of adding to it.

9. **Customer Empty Cart Check Bug (`support.cpp`, line 342)**
   - **Bug:** `if (!cart.empty())`
   - **Effect:** Inverts the check: claims the cart is empty when `cart` contains items, and tries to print items when `cart` is empty.

10. **Billing Tax Bug (`support.cpp`, line 360)**
    - **Bug:** `float tax = total_price / 0.18;`
    - **Effect:** Inflates the tax astronomically by dividing by 0.18 instead of multiplying by 0.18 (18%).

11. **Billing Discount Bug (`support.cpp`, line 362)**
    - **Bug:** `if (total_price < 1000)`
    - **Effect:** Gives a discount for purchases under $1000 instead of over $1000.

12. **Billing Final Price Bug (`support.cpp`, line 370)**
    - **Bug:** `float final_price = total_price + discount - tax;`
    - **Effect:** Reverses the math: adds the discount and subtracts the tax instead of subtracting discount and adding tax.

13. **Billing Cancel Purchase Bug (`support.cpp`, lines 382-383)**
    - **Bug:** `cart.clear(); total_price = 0;` outside the `if (confirm == 'y' || confirm == 'Y')` block
    - **Effect:** Shopping cart is reset even if the customer cancels the purchase.

14. **Main Menu Admin/Employee Swap Bug (`main.cpp`, lines 25-28)**
    - **Bug:** `case 1:` calls `support.employee();`
    - **Effect:** If the user selects Admin on the main menu, they are shown the Employee interface instead.

15. **Main Menu Customer/Admin Swap Bug (`main.cpp`, lines 33-37)**
    - **Bug:** `case 3:` calls `support.admin();`
    - **Effect:** If the user selects Customer on the main menu, they are shown the Admin interface instead.
