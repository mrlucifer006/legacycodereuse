# Feature expansion: transaction timestamp

After a player confirms checkout, make a timestamp using `YYYY-MM-DD HH:MM:SS`. Display it in the final summary and append the timestamp, selected pack ids, and final total to `transactions.csv`. Use Java's date and time classes, then use `BufferedWriter` to add a new transaction row.
