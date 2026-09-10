# Python bug key

All line numbers refer to `support.py`.

1. Line 6, `... | ...`: `|` lets either a matching username or password authenticate; both must match the same row.
2. Line 13, `fee * 1.1`: a new service is stored at 110 percent of the fee entered by staff.
3. Line 16, `fee / 10`: an update stores one tenth of the requested fee.
4. Line 16, `data["service"] == name`: every duplicate service name is changed instead of one chosen record.
5. Line 19, `data[data["service"] == name]`: deletion writes only the matching service, discarding every other record.
6. Line 22, `[password, user]`: teller credentials are persisted in reversed CSV columns.
7. Line 44, `data.iloc[selected]`: menu numbers start at one, but `iloc` starts at zero, selecting the next service.
8. Line 44, `cart.append(...)`: out-of-range and negative selections are not checked; negative values select from the end.
9. Line 46, `subtotal * 0.08`: tax is 8 percent rather than the required 18 percent.
10. Line 47, `subtotal + tax - discount`: the calculation never validates that the cart has at least one item, so an empty checkout is reported as confirmed.
11. Line 48, `Checkout confirmed`: confirmation is printed without asking the customer to accept the final amount.
12. Line 13, `to_csv(ACCOUNTS, index=False)`: the live catalog is overwritten directly; a write interruption can leave a partial store.
