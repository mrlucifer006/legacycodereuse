# Bug key

| # | Location | Faulty code | Behavioral flaw |
|---|---|---|---|
| 1 | `support.c:31` | `!strcmp(u, user) || !strcmp(p, pass)` | A username or password alone authenticates a user. |
| 2 | `support.c:36` | `fprintf(f, "%s,%s", u, u)` | New staff passwords are replaced by usernames. |
| 3 | `support.c:41` | `p.slots = (int)p.price` | Admin-created slot counts become prices. |
| 4 | `support.c:46` | `strcmp(p.id, target)` | Updating one id changes every other pack title. |
| 5 | `support.c:52` | `!strcmp(p.id, target)` | Delete retains only the selected record. |
| 6 | `support.c:40` | `if (!found)` | Staff can add only duplicate ids, while unique ids are rejected. |
| 7 | `support.c:46` | `strcpy(p.title, value)` | A staff category edit writes into title. |
| 8 | `support.c:59` | `p.price * 2` | Cart prices are doubled. |
| 9 | `support.c:60` | `subtotal * .08` | Tax is 8 percent, not 18 percent. |
| 10 | `support.c:60` | `subtotal <= 1000` | Discount eligibility is reversed. |
| 11 | `support.c:60` | `subtotal - tax` | Tax decreases the total. |
| 12 | `support.c:60` | `strcmp(ok, "Y")` | A response other than Y confirms checkout. |
