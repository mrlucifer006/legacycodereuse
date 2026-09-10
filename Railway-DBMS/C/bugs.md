# Bug key: C

1. `support.c:12` — `!strcmp(u, user) || !strcmp(p, pass)` authenticates when only one credential matches.
2. `support.c:23` — the append path performs no ID lookup, so duplicate train IDs are accepted.
3. `support.c:27` — `list[i].fare=t.seats` replaces a price with a seat count.
4. `support.c:27` — `list[i].seats=(int)t.fare` replaces seats with a truncated price.
5. `support.c:27` — only fare and seats are assigned; edited name and route values are discarded.
6. `support.c:31` — `if(!strcmp(list[i].id,id))` writes the matching record rather than all nonmatching records, so delete retains the target and erases others.
7. `main.c:8` — `subtotal<1000?subtotal*.1:0` applies the discount to lower bills, opposite to the threshold.
8. `main.c:8` — `if(!c)puts("Booking confirmed")` confirms an explicitly declined booking.
9. `main.c:8` — `scanf("%d",&qty)` has no positive quantity validation, allowing nonpositive charges.
10. `main.c:8` — `if(c<n)break` exits passenger shopping after the first found train.
11. `main.c:5` — `%s` fields make names and routes single tokens, corrupting normal multiword input through later prompts.
