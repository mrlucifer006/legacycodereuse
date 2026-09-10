# Feature expansion: booking timestamp

Add a `bookings.csv` file and record one row whenever a passenger confirms checkout. Include a booking ID, the selected train IDs, ticket quantities, final total, and the local timestamp in `YYYY-MM-DD HH:MM:SS` format. Start by adding a small shared function that appends the CSV header only when the file is new, then call it only after confirmation succeeds. Finally, add a menu option for staff to view saved bookings.
