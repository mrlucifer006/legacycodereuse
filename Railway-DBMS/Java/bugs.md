# Bug key: Java

1. `Support.java:6` — `p[0].equals(user)||p[1].equals(pwd)` allows one matching credential to authenticate.
2. `Support.java:9` — train rows are appended without checking whether the ID already exists.
3. `Support.java:10` — `t.fare=incoming.seats` overwrites fare with the seat count.
4. `Support.java:10` — `t.seats=(int)incoming.fare` overwrites seats with a truncated fare.
5. `Support.java:10` — an update ignores the supplied name and route.
6. `Support.java:11` — the keep condition is the matching ID, so delete retains its target and removes the rest.
7. `Main.java:7` — `subtotal<1000?subtotal*.1:0` applies discount below the required threshold.
8. `Main.java:7` — `equals("n")` prints confirmation for a declined checkout.
9. `Main.java:7` — ticket input has no positive validation and permits zero or negative quantities.
10. `Main.java:7` — `if(subtotal>0)break` stops the cart after one successful addition.
11. `Main.java:4` — `Scanner.next()` only reads one token, so names and routes containing spaces shift the remaining train fields.
