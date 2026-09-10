# Bank Service Billing System

This is a command-line banking-service catalog and billing application. It keeps its small data set in CSV files so new programmers can inspect and modify the stored records without a database server.

Administrators sign in through `admin.csv`, create teller accounts, and create, edit, delete, or list banking-service records. Tellers sign in through `teller.csv` and can add, update, and view services. Customers do not need an account: they browse the service catalog, select one or more services into a cart, then receive a checkout summary with subtotal, 18 percent tax, an order-value discount, and confirmation.

Each language folder is an intentionally imperfect debugging exercise. Its implementation has one entry file and one support file, plus the three CSV stores. The source is designed to compile or run, while the accompanying bug key identifies the logical defects learners should repair.
