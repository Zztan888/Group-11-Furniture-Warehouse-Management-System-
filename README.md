# Furniture Warehouse Management System (Group 11)

## 👥 Contributors (Group 11 Members)
-**Tee Kah Hock (MEC245061)
-**Tan Zin You (MEC245007)
-**Lee Qi Hui (MEC255018)

A comprehensive system for managing furniture inventory, supplier logistics, and sales orders. This project implements efficient data structures (Binary Search Trees) to handle large datasets of furniture stock and shipments.

## 📂 Project Structure

├── [**data**](./data)
│   ├── [generated](./data/generated)
│   └── [inventory](./data/inventory)
│
├── [**docs**](./docs)
│   └── [Presentation_Slides.pptx](./docs/Presentation_Slides.pptx)
│
├── [**src**](./src)
│   ├── [**inventory_module**](./src/inventory_module)
│   │   └── [inventory_task2.py](./src/inventory_module/inventory_task2.py)
│   │
│   ├── [**sales_module**](./src/sales_module)
│   │   ├── [bst_order.py](./src/sales_module/bst_order.py)
│   │   └── [main_sales.py](./src/sales_module/main_sales.py)
│   │
│   └── [**supplier_module**](./src/supplier_module)
│       ├── [bst_implementation.py](./src/supplier_module/bst_implementation.py)
│       ├── [generator.py](./src/supplier_module/generator.py)
│       └── [main_app.py](./src/supplier_module/main_app.py)
│
├── [.gitignore](./.gitignore)
└── [README.md](./README.md)

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

## 👥 Contributors (Group 11)

| Name | Student ID | Module Responsibility |
| :--- | :--- | :--- |
| **Tee Kah Hock** | MEC245061 | Furniture Inventory Control Module |
| **Tan Zin You** | MEC245007 | Supplier & Shipment Tracking Module |
| **Lee Qi Hui** | MEC255018 | Customer Order and Delivery Management Module |
