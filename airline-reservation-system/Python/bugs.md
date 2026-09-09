# Intentional Bug Key — Python

1. `support.py:15` — `|` accepts a matching username *or* password. Authentication must require both credentials from the same row.
2. `support.py:19` — `[flight_id, destination, seats, price]` writes seat count under `price` and price under `seats`.
3. `support.py:25` — `"price"] = seats` assigns the wrong input to the price field.
4. `support.py:26` — `"seats"] = price` assigns the wrong input to the seat field.
5. `support.py:31` — retaining rows equal to the ID makes delete discard every other flight and preserve the requested one.
6. `support.py:45` — agent credentials are collected and stored in reverse CSV-column order.
7. `support.py:71` — `selected <= len(flights)` permits `len(flights)`, which is outside the final zero-based index.
8. `support.py:71` — no lower-bound test allows negative indexes, selecting from the end of the catalog.
9. `support.py:75` — the discount starts at 1000, although the stated threshold is strictly greater than 1000.
10. `support.py:76` — `subtotal + tax + discount` adds a discount instead of subtracting it.
