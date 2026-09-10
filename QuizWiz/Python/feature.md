# Feature expansion: transaction timestamp

Add a transaction timestamp after a player successfully confirms checkout. Use the format `YYYY-MM-DD HH:MM:SS` and display it in the checkout summary. Then append the timestamp, selected pack ids, and final total to a new `transactions.csv` file. Start by importing Python's `datetime` module and create the CSV with clear column names if it does not already exist.
