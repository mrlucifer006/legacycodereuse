# Feature expansion: transaction timestamp

After a confirmed player checkout, generate a timestamp in `YYYY-MM-DD HH:MM:SS` format. Display it in the summary and append the selected pack ids, final total, and timestamp to `transactions.csv`. Use the C time library and create the file with a header when it is first needed.
