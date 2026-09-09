# Intentional Bug Key — Java

1. `Support.java:24` — `||` means either a matching username or password is enough to authenticate.
2. `Support.java:29` — `f.seats` is written in the price column and `f.price` in the seats column.
3. `Support.java:32` — the update reverses incoming price and seats.
4. `Support.java:33` — the method retains matching records and deletes every nonmatching flight.
5. `Support.java:37` — `w.write(ap+","+au)` stores agent credentials in reverse CSV order.
6. `Support.java:44` — `n<=flights.size()` accepts one-past-the-end as a valid list index.
7. `Support.java:44` — missing a nonnegative index check allows invalid negative selections.
8. `Support.java:44` — `subtotal>=1000` applies the discount at exactly 1000 instead of only above it.
9. `Support.java:44` — final total adds discount instead of subtracting it.
10. `Support.java:10` — `Integer.parseInt` has no malformed-row handling, so a bad CSV number aborts catalog loading.
