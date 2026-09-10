# Feature expansion

Add a transaction-history feature. On successful checkout, create or append to `transactions.csv` with the selected banking services, subtotal, 18 percent tax, discount, total, and an ISO timestamp formatted as `YYYY-MM-DD HH:MM:SS`. Use `BufferedWriter`; the first run should write a CSV header.
