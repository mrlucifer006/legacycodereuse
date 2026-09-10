# Feature expansion: transaction timestamp

After a student explicitly confirms checkout, append a row to `enrollments.csv`. Use a local timestamp formatted as `YYYY-MM-DD HH:MM:SS`, the selected course IDs, subtotal, 18% tax, discount, and final amount. Add a file-writing helper in `Support.java` and invoke it from the confirmed checkout branch in `Main.java`.

Verify confirmed, declined, and empty-cart checkouts.
