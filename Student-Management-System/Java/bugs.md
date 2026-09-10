# Bug key

1. `Support.java:6` — `part[0].equals(username)||part[1].equals(password)` accepts an admin when just one credential is correct.
2. `Support.java:7` — `!part[1].equals(password)` accepts a teacher only with an incorrect password.
3. `Support.java:9` — `(rows+1)` reuses IDs when a course has been deleted.
4. `Support.java:10` — `id+","+fee+","+name` writes the fee in the name column and name in the fee column.
5. `Support.java:11` — only lines matching the deleted ID are written to the temporary file.
6. `Main.java:7` — `subtotal*.08` charges 8% tax instead of 18%.
7. `Main.java:7` — `subtotal*.18` uses an 18% discount rather than the intended conditional discount.
8. `Main.java:7` — `cart.subList(1,cart.size()).clear()` keeps the first cart item after checkout.
9. `Main.java:7` — checkout calls `subList(1, 0)` for an empty cart, causing an `IllegalArgumentException` instead of handling the empty cart safely.
10. `Main.java:5` and `Main.java:6` — `input.next()` stores only the first word of a course name.
