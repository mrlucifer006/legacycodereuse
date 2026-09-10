# Bug key

| # | Location | Faulty code | Behavioral flaw |
|---|---|---|---|
| 1 | `support.cpp:14` | `(u == user) || (p == pass)` | Either credential alone logs in. |
| 2 | `support.cpp:15` | `f << u << ',' << u` | New staff passwords become usernames. |
| 3 | `support.cpp:16` | `p.slots=(int)p.price` | Admin pack slots are replaced with price. |
| 4 | `support.cpp:17` | `p.id!=target` | Admin update alters all other records. |
| 5 | `support.cpp:18` | `p.id==target` | Delete preserves only the requested record. |
| 6 | `support.cpp:16` | `if(!found)` | Unique staff pack ids are rejected. |
| 7 | `support.cpp:17` | `p.title=value` | Staff category input overwrites title. |
| 8 | `support.cpp:21` | `subtotal+=p.price*2` | Each cart selection is doubled. |
| 9 | `support.cpp:21` | `subtotal*.08` | Tax is 8 percent. |
| 10 | `support.cpp:21` | `subtotal<=1000` | Discount condition is reversed. |
| 11 | `support.cpp:21` | `subtotal-tax-discount` | Tax is subtracted. |
| 12 | `support.cpp:21` | `!="Y"` | Refusing confirmation completes checkout. |
