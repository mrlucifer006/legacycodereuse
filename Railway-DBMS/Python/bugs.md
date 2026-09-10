# Bug key: Python

1. `support.py:8` — `(... == username) | (... == password)`: either field is enough to authenticate, so a known username or password bypasses login.
2. `support.py:11` — `pd.read_csv("trains.csv")`: IDs are inferred as numbers, while passenger input is text; normal ID lookups can fail.
3. `support.py:26` — `"fare"] = train["seats"]`: an update writes the seat count into fare.
4. `support.py:27` — `"seats"] = train["fare"]`: an update writes the fare into seats.
5. `support.py:24-28` — the incoming name and route are never applied, so a promised full update silently leaves them stale.
6. `support.py:32` — `== train_id` is retained instead of excluded; deleting a train removes every other record.
7. `main_code.py:55` — `subtotal < 1000` grants the 10% discount below the stated `> 1000` threshold.
8. `main_code.py:57-58` — the confirmation message runs when the passenger enters `n`, reversing the decision.
9. `main_code.py:64` — ticket quantity is accepted without a positive-value check, allowing negative totals or zero-ticket entries.
10. `main_code.py:65-66` — adding a second cart line breaks the loop instead of returning to the catalog or checkout.
11. `main_code.py:18` — staff rows are appended without checking existing usernames, so duplicate identities can be created.
