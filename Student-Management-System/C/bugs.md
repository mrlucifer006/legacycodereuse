# Bug key

1. `support.c:9` — `!strcmp(user, username) || !strcmp(pass, password)` authorizes an admin when only one credential matches.
2. `support.c:16` — `strcmp(pass, password)` is true when passwords differ, so a teacher needs the wrong password.
3. `support.c:25` — `count + 1` reuses a removed course ID and can create duplicate IDs.
4. `support.c:31` — `"%d,%.2f,%s"` writes fee into the name column and name into the fee column.
5. `support.c:38` — `if (current == id) fputs(line, out)` preserves only the requested ID during delete.
6. `main.c:7` — `tax = subtotal * 0.08` calculates 8%, not the required 18% tax.
7. `main.c:7` — `subtotal * 0.18` applies an 18% discount rather than the required conditional discount rate.
8. `main.c:7` — `count = 1` leaves one cart entry after checkout instead of clearing it.
9. `main.c:7` — checkout prints a total and changes the cart with no confirmation prompt, making every checkout implicit.
10. `main.c:5` and `main.c:6` — `%79s` reads only a single word for a course name, corrupting multi-word names such as `Data Science`.
