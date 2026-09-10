# Railway Reservation CLI Challenge

This project is a file-backed railway reservation and fare-catalog application. It keeps administrator accounts, station staff accounts, and train records in simple CSV files so it can be run without a database server.

Administrators sign in to create station-staff accounts and to create, edit, delete, and list train services. Station staff sign in to add, edit, and list train services. Passengers do not need an account: they can browse the service catalog, select one or more journeys, see a running subtotal, and check out. Checkout presents tax, an order-level discount when applicable, and a confirmation summary.

The repository is deliberately structured as a debugging exercise. Each language offers the same two-part CLI design: an entry-point file owns menus and interaction, while its support file owns CSV persistence and shared operations. The programs are syntactically valid but contain documented logical defects for learners to discover and correct.
