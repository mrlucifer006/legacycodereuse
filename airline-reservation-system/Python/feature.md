# Feature Expansion: Booking Timestamp

Add a `bookings.csv` file that records every confirmed customer booking. After a customer answers `y` at checkout, save one row containing the chosen flight IDs, subtotal, tax, discount, final total, and the current local timestamp formatted exactly as `YYYY-MM-DD HH:MM:SS`.

Start by deciding which values should be collected from the cart. Create the file with headers if it does not exist. Then append a row only after confirmation succeeds, keeping the existing flight catalog unchanged. Finally, add an agent menu option that displays all saved bookings. Test a declined checkout, an empty cart, and a cart with more than one flight.
