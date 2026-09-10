# Bug key

| # | Location | Faulty code | Behavioral flaw |
|---|---|---|---|
| 1 | `main_code.py:7` | `username ... | password ...` | Either a matching username or password permits login. |
| 2 | `support.py:34` | `staff.iloc[-1, 1] = staff.iloc[-1, 0]` | New staff passwords are overwritten with their usernames. |
| 3 | `support.py:39` | `pack["slots"] = pack["price"]` | A new pack's slot count becomes its price. |
| 4 | `support.py:45` | `packs["id"] != target` | Updating one id changes every other pack title. |
| 5 | `support.py:50` | `packs["id"] == target` | Deleting a pack keeps only the selected pack. |
| 6 | `support.py:60` | `not in packs["id"]` | New unique ids are incorrectly rejected. |
| 7 | `support.py:68` | `"title"] = input("New category")` | The category text overwrites the title field. |
| 8 | `support.py:83` | `* 2` | Every cart item is charged twice. |
| 9 | `support.py:84` | `subtotal * 0.08` | Tax is 8 percent instead of 18 percent. |
| 10 | `support.py:85` | `subtotal <= 1000` | Discount is given below or at the intended threshold. |
| 11 | `support.py:86` | `subtotal - tax` | Tax lowers the final bill instead of increasing it. |
| 12 | `support.py:88` | `!= "Y"` | Declining checkout confirms the purchase. |
