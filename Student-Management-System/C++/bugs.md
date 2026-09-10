# Bug key

1. `support.cpp:7` — `user==u || pass==p` accepts an admin if either value matches.
2. `support.cpp:8` — `pass!=p` authorizes a teacher only when the supplied password is different.
3. `support.cpp:10` — `rows+1` reuses IDs after deletion.
4. `support.cpp:11` — `id<<","<<fee<<","<<name` reverses the name and fee CSV columns.
5. `support.cpp:12` — the write occurs when `stoi(cell)==id`, retaining the target instead of all non-target records.
6. `main.cpp:7` — `subtotal*.08` applies 8% tax instead of 18%.
7. `main.cpp:7` — `subtotal*.18` makes the discount 18%, not the intended conditional discount.
8. `main.cpp:7` — `cart.erase(... 1 ...)` retains the first selected course after checkout.
9. `main.cpp:7` — checkout has no final confirmation, yet it modifies cart state.
10. `main.cpp:5` and `main.cpp:6` — `cin>>n` truncates a multi-word course name at its first space.
