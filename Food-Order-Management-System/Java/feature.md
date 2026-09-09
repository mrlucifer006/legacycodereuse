# Beginner feature: order timestamp

After the user confirms an order, use `java.time.LocalDateTime.now()` and `DateTimeFormatter` to create a `YYYY-MM-DD HH:MM:SS` timestamp. Display it beside the receipt total. Next, append the timestamp and total to a new `orders.csv` using `BufferedWriter`.
