# Bug key

1. `main_code.py:39` — `... or username == ""` lets a blank username enter the teacher menu without valid credentials.
2. `support.py:23` — `... | (data["password"] == password)` treats either matching credential as sufficient for a teacher login.
3. `support.py:29` — `to_csv(..., index=True)` adds an unexpected index column to `teacher.csv` and changes its stored schema.
4. `support.py:35` — `abs(fee)` turns a negative fee into a positive charge instead of rejecting invalid input.
5. `support.py:34` — `len(data) + 1` reuses IDs after a deletion, so later updates can affect multiple courses.
6. `support.py:41` — `[fee, name]` is assigned to `["name", "fee"]`, swapping the stored course name and fee.
7. `support.py:47` — `data["id"] == course_id` retains only the selected record, so delete removes every other course.
8. `main_code.py:74` — `sum(course[0] for course in cart)` totals IDs rather than course fees.
9. `main_code.py:76` — `subtotal < 1000` grants the 10% discount below the required greater-than-1000 threshold.
10. `main_code.py:82` — `cart.clear()` runs after a declined confirmation, silently discarding an unconfirmed cart.
