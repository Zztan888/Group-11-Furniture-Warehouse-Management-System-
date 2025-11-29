# Furniture Warehouse Management System (Group 11)

## 👥 Contributors (Group 11 Members)
### - **Tee Kah Hock** (MEC245061)
### - **Tan Zin You** (MEC245007)
### - **Lee Qi Hui** (MEC255018)

A comprehensive system for managing furniture inventory, supplier logistics, and sales orders. This project implements efficient data structures (Binary Search Trees) to handle large datasets of furniture stock and shipments.

## 📂 Project Structure

```text
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
└── README.md                    # Project Documentation
```

## 🚀 Key Features

### 🔹 Furniture Inventory Control Module
- **Main Feature:** Manages physical stock levels of furniture items.
- **Functionality:** Extensive search and reporting on current inventory levels.
- **Input:** Processes raw CSV data into structured objects.

### 🔹 Supplier & Shipment Tracking Module
- **Main Feature:** Tracks supplier details and shipment statuses.
- **Data Structure:** **Binary Search Tree (BST)** for efficient searching and insertion (`O(log n)`).
- **Data:** Handles 30,000 generated supplier and 50,000 shipment records.
- **Operations:** Add Supplier, Search ID, Track Shipment Status.

### 🔹 Customer Order and Delivery Management Module
- **Main Feature:** Processes customer orders and sales transactions.
- **Data Structure:** Implements tree-based logic to sort and retrieve order history.

## Requirements
- Python 3.10 and above

## 🔗 Quick Access to Source Code
Click the links below to navigate directly to the module folders:

📦 Furniture Inventory Control Module -  **Tee Kah Hock** (MEC245061)
### [**./src/inventory_module**](./src/supplier_module)

🚚 Supplier & Shipment Tracking Module - **Tan Zin You** (MEC245007)
### [**./src/supplier_module**](./src/supplier_module)

🛒 Customer Order and Delivery Management Module - **Lee Qi Hui** (MEC255018)
### [**./src/sales_module**](./src/sales_module)

📊 Presentation Slides
### [./docs/Presentation_Slides.pptx](./docs/Presentation_Slides.pptx)

## Assignment Details

<table>
  <tr>
    <th>Group & Theme</th>
    <th>Name & Student ID</th>
    <th>Programming Language Initial Proposal Title</th>
    <th>Individual Tree Data Structure</th>
  </tr>
  <tr>
    <td rowspan="3"><b>Group 11</b><br>Furniture Warehouse Management System</td>
    <td><b>Tee Kah Hock</b><br>MEC245061</td>
    <td>Furniture Inventory Control Module</td>
    <td>AVL</td>
  </tr>
  <tr>
    <td><b>Tan Zin You</b><br>MEC245007</td>
    <td>Supplier & Shipment Tracking Module</td>
    <td>B-Tree</td>
  </tr>
  <tr>
    <td><b>Lee Qi Hui</b><br>MEC255018</td>
    <td>Customer Order and Delivery Management Module</td>
    <td>Splay</td>
  </tr>
</table>
