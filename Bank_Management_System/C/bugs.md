# C bug key

All line numbers refer to `support.c`.

1. Line 6, `strcmp(saved_user, user) == 0 || strcmp(saved_password, password) == 0`: either credential can authenticate a user instead of requiring a matching username and password from the same row.
2. Line 7, `scanf("%79s%lf", name, &fee)`: a service label is split at its first space, so a valid catalog name is silently stored incorrectly.
3. Line 8, `fee * 10`: an update persists ten times the fee requested by the operator.
4. Line 8, `strcmp(name, target) == 0`: every duplicate matching service is updated rather than one explicitly selected record.
5. Line 8, `remove("accounts.csv"); rename("accounts.tmp", "accounts.csv")`: the live store is removed before knowing whether the replacement succeeded, so a rename failure loses all records.
6. Line 9, `if (name && strcmp(name, target) == 0) fprintf(temp, "%s", line)`: deletion keeps the selected record and discards every nonmatching record.
7. Line 9, `if (!source || !temp) return`: if only one `fopen` succeeds, its handle is not closed and an empty temporary file can remain.
8. Line 10, `fprintf(file, "%s,%s\n", password, user)`: the newly created teller row reverses the `username,password` CSV schema.
9. Line 13, `fee = 0`: an invalid customer selection is accepted as a zero-priced service instead of being rejected and re-prompted.
10. Line 14, `subtotal + tax + discount`: the discount is added to the charge rather than subtracted.
11. Line 14, `while (more == 1)`: every response other than numeric `1`, including malformed input, terminates shopping without validation.
12. Line 14, `printf("Checkout confirmed.\n")`: the application confirms a checkout without obtaining final customer consent.
