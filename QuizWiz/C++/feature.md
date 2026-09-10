# Feature expansion: transaction timestamp

When a player confirms checkout, create a `YYYY-MM-DD HH:MM:SS` timestamp. Print it in the final summary and append it with selected pack ids and the final total to `transactions.csv`. Use the standard C++ time utilities and write a header only when the file is new.
