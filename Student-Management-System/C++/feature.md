# Feature expansion: transaction timestamp

Add a confirmation step and write a receipt row to `enrollments.csv` only after the student confirms. The row should contain a local timestamp formatted as `YYYY-MM-DD HH:MM:SS`, selected course IDs, subtotal, 18% tax, discount, and final total. Keep CSV operations in `support.cpp` and expose the helper from `support.hpp`.

Try an accepted checkout, a rejected checkout, and an empty cart.
