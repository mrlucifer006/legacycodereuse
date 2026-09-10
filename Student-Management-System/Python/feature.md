# Feature expansion: transaction timestamp

Add a successful-enrollment receipt to the student checkout flow. After the student confirms with `y`, capture the current local time in `YYYY-MM-DD HH:MM:SS` format and append one CSV row to a new `enrollments.csv` file. Store the timestamp, each selected course ID, subtotal, tax, discount, and final total. Do not write a receipt when the student declines confirmation.

Start by making a small helper in `support.py` that accepts the cart and totals. Then call it only from the confirmed checkout branch in `main_code.py`. Test both confirmation choices and an empty cart.
