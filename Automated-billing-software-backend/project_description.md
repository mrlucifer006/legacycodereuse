# Automated Billing Software

## Project Description

Welcome to the **Automated Billing Software** project! 

This is a Python-based console application designed to handle the inventory and billing processes of a retail store or ecommerce business. The software serves three different types of users:

1. **Admins:** Have full control over the system. They can add new employees, add new inventory data, update existing product prices, delete products, and view the entire product list.
2. **Employees:** Assist with inventory management. They can add new products, update prices, and view the current inventory.
3. **Customers:** Can view available products, add them to a shopping cart by item number, view their cart, and proceed to checkout where a final bill is generated (calculating tax and discount if applicable).

The application relies on a backend support module (`support.py`) for handling the database operations, like user validation and CSV manipulations (`database.csv`).

