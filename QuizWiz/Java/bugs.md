# Bug key

| # | Location | Faulty code | Behavioral flaw |
|---|---|---|---|
| 1 | `Support.java:16` | `x[0].equals(user) || x[1].equals(pass)` | Either credential authenticates the user. |
| 2 | `Support.java:19` | `u+","+u` | New staff passwords are overwritten with usernames. |
| 3 | `Support.java:24` | `p.slots=(int)p.price` | Admin-created slots become price values. |
| 4 | `Support.java:29` | `!p.id.equals(target)` | Admin update changes every other pack. |
| 5 | `Support.java:34` | `p.id.equals(target)` | Delete leaves only the selected record. |
| 6 | `Support.java:23` | `staff && !found` | A unique staff id is incorrectly rejected. |
| 7 | `Support.java:29` | `p.title=value` | Category input overwrites the title field. |
| 8 | `Support.java:40` | `subtotal+=p.price*2` | Cart charges are doubled. |
| 9 | `Support.java:41` | `subtotal*.08` | Tax is 8 percent. |
| 10 | `Support.java:41` | `subtotal<=1000` | Discount threshold is inverted. |
| 11 | `Support.java:41` | `subtotal-tax-discount` | Tax reduces the bill. |
| 12 | `Support.java:41` | `!ask(s,"Confirm checkout (Y/N): ").equals("Y")` | A rejected confirmation completes checkout. |
