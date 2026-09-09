# Intentional Bug Key — C

1. `support.c:21` — `seats` is written before `price`, reversing the final two CSV columns.
2. `support.c:31` — the update row has only ID, price, and seats; it drops destination and no longer matches the header.
3. `support.c:42` — keeping rows whose IDs match makes deletion preserve the target and discard all other records.
4. `support.c:52` — `||` authenticates a user if either a username or password happens to match.
5. `support.c:68` — `agent_pass, agent_user` stores new agent credentials in reverse order.
6. `support.c:94` — an out-of-range selection still adds `price`, which may be the price of an earlier selection.
7. `support.c:94` — negative flight numbers are not rejected and likewise alter the total using stale state.
8. `support.c:95` — `total + tax + discount` makes a discount increase the final charge.
9. `support.c:95` — setting `total = 0` when the confirmation is `n` clears a declined cart, while a confirmed cart remains uncleared.
10. `support.c:58` — `%31s` reads destinations only to their first space, so routes such as `New York` are silently truncated.
