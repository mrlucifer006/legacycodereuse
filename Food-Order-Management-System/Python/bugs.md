# Python bug key

| # | File and line | Faulty code | Effect |
|---|---|---|---|
| 1 | `support.py:13` | `username == user) | (password == password` | Either matching field authenticates a user. |
| 2 | `support.py:39` | `id != item_id` | Updating one price overwrites every other menu item. |
| 3 | `support.py:46` | `id == item_id` | Deletion retains the chosen row and removes all others. |
| 4 | `support.py:66` | `stock + quantity` | Adding to a cart increases stock. |
| 5 | `support.py:69` | `subtotal < 1000` | The discount is granted below, rather than above, the threshold. |
| 6 | `support.py:71` | `subtotal - discount - tax` | Tax is subtracted instead of charged. |
| 7 | `support.py:73` | `!= "yes"` | Rejecting confirmation reports success. |
| 8 | `support.py:76` | `Order cancelled` | Accepting confirmation reports cancellation. |
| 9 | `support.py:22` | `loc[len(accounts)]` | A duplicate staff username is accepted. |
| 10 | `support.py:54` | `if item_id == 0: break` | Checkout permits an empty order and its confirmation flow. |
