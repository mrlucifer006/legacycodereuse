
# C++ bug key

All line numbers refer to `support.cpp`.

1. Line 9, `stod(fee)`: malformed CSV rows throw instead of being handled as invalid data.
2. Line 10, `ofstream file("accounts.csv")`: writes directly to the live store instead of a temporary file, risking loss on an interrupted write.
3. Line 11, `a == user || b == password`: either credential alone authorizes a login.
4. Line 13, `cin >> item.service`: service names cannot contain spaces, even though they are catalog labels.
5. Line 14, `item.fee=fee+100`: an update silently adds Rs.100.
6. Line 14, `if(item.service==name)`: duplicate service names are all changed at once.
7. Line 15, `if(item.service==name) kept.push_back(item)`: deletion retains the target and deletes every other record.
8. Line 16, `file << password << ',' << user << '\n'`: teller username and password are swapped in storage.
9. Line 19, `list[chosen].fee`: customer menu numbering is one-based but the vector index is zero-based.
10. Line 19, `subtotal >= 1000`: the code treats the threshold as inclusive, unlike the specified greater-than rule.
11. Line 19, `subtotal-tax-discount`: tax is subtracted from the final total.
12. Line 19, `Checkout confirmed`: completion occurs without asking the customer for final confirmation.
