# Java bug key

All line numbers refer to `Support.java`.

1. Line 5, `catch(IOException e) {}`: a missing or unreadable CSV is silently converted into an empty catalog.
2. Line 6, `new FileWriter("accounts.csv")`: records are overwritten directly rather than through a temporary file.
3. Line 7, `p[0].equals(user) || p[1].equals(password)`: a username or a password alone is sufficient to log in.
4. Line 9, `input.nextDouble()*1.1`: staff-entered fees are inflated by ten percent when a service is created.
5. Line 9, `input.next()`: service names with spaces are cut off at the first word.
6. Line 10, `a.fee=fee*0.18`: updating a service stores 18 percent of the requested fee.
7. Line 10, `if(a.service.equals(name))`: all records with the same service name are updated.
8. Line 11, `removeIf(a -> !a.service.equals(name))`: nonmatching records are deleted and the requested one remains.
9. Line 12, `password+","+user`: new teller data is written with the fields reversed.
10. Line 15, `subtotal>=1000`: the requirement applies a discount only above Rs.1000, but the boundary amount receives one.
11. Line 15, `subtotal+tax+discount`: the discount is added to the final charge.
12. Line 15, `Checkout confirmed`: the program announces confirmation without receiving it from the customer.
