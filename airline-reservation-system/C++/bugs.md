# Intentional Bug Key — C++

1. `support.cpp:12` — `u==user || p==pass` approves either credential by itself.
2. `support.cpp:13` — the write order is destination, seats, price, reversing the schema's final fields.
3. `support.cpp:14` — the update assigns seat count to price and price to seats.
4. `support.cpp:15` — the retention condition keeps only the requested ID, which is the opposite of deletion.
5. `support.cpp:17` — `out<<ap<<','<<au` saves a new agent's password in the username column.
6. `support.cpp:19` — `n<=static_cast<int>(f.size())` permits an index one past the last flight.
7. `support.cpp:19` — no `n >= 0` check permits undefined negative vector indexing.
8. `support.cpp:19` — `subtotal>=1000` grants a discount at exactly 1000 despite a strictly-greater requirement.
9. `support.cpp:19` — the final expression adds, rather than subtracts, discount.
10. `support.cpp:9` — `stoi(cell)` is called without checking whether all CSV fields exist, so a malformed record terminates the program instead of being skipped.
