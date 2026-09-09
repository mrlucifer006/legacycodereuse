# Airline Reservation System

This command-line airline reservation system manages a small catalog of flights using CSV files. It is designed as a multi-language debugging exercise: each implementation offers the same workflows and stores equivalent data, while containing intentional logical defects for learners to locate and repair.

Administrators sign in to create agent accounts and create, edit, delete, or view flight records. Agents sign in to add, update, and view flight records. Customers do not need an account: they browse the flight catalog, select one or more flights into a booking cart, and review a checkout summary with tax, a conditional discount, and confirmation.

The application uses three simple CSV files in each language folder. `admin.csv` stores administrator credentials, `agent.csv` stores agent credentials, and `flights.csv` stores flight ID, destination, ticket price, and available seats. Run an implementation from its own language folder so it reads the adjacent CSV files.
