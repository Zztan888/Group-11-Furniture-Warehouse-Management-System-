# Furniture Warehouse Management System (Group 11)

A comprehensive system for managing furniture inventory, supplier logistics, and sales orders. This project implements efficient data structures (Binary Search Trees) to handle large datasets of furniture stock and shipments.

📂 Project Structure
```
Group11-Furniture-System/
├── data/                        # Dataset storage
│   ├── generated/               # Generated datasets (Suppliers, Shipments)
│   └── inventory/               # Furniture inventory CSVs
│
├── docs/                        # Project documentation
│   └── Presentation_Slides.pptx # Task 2 Presentation
│
├── src/                         # Source Code Modules
│   ├── inventory_module/        # Inventory Management (KH)
│   │   └── inventory_task2.py
│   │
│   ├── sales_module/            # Sales & Order Processing (QH)
│   │   ├── bst_order.py         # BST Implementation for Orders
│   │   └── main_sales.py
│   │
│   └── supplier_module/         # Supplier & Shipment Tracking (ZY)
│       ├── bst_implementation.py # BST Logic for Suppliers
│       ├── generator.py         # Data Generation Script
│       └── main_app.py          # Supplier CLI Application
│
├── .gitignore                   # Files to ignore (pycache, etc.)
└── README.md                    # Project Documentation
```

## Key Features
1.  Furniture Inventory Control Module  
Main Feature: Manages physical stock levels of furniture items.

Functionality: extensive search and reporting on current inventory levels.

Input: Processes raw CSV data into structured objects.

2.Supplier & Shipment Tracking Module
Main Feature: Tracks supplier details and shipment statuses.

Data Structure: Binary Search Tree (BST) for efficient searching and insertion of supplier records (O(log n)).

Data: Handles 30000 generated supplier and 50000 generated shipment records.

Operations: Add Supplier, Search ID, Track Shipment Status.

3. Customer Order and Delivery Management Module
Main Feature: Processes customer orders and sales transactions.

Data Structure: Implements tree-based logic to sort and retrieve order history.


## Requirements
.Python 3.10 and above
.pandas (pip install pandas)

## Contributors (Group 11)
Tee Kah Hock MEC245061- Furniture Inventory Control Module 

Tan Zin You MEC245007 - Supplier & Shipment Tracking Module

Lee Qi Hui MEC255018 - Customer Order and Delivery Management Module
