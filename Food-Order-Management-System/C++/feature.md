# Beginner feature: order timestamp

Use `std::chrono` to get the current time and `std::put_time` to format it as `YYYY-MM-DD HH:MM:SS` after a successful confirmation. Once it prints correctly, use `std::ofstream` in append mode to store the timestamp and order total in `orders.csv`.
