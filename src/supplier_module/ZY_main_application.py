"""
main_application.py
Interactive menu-driven application for Furniture Supplier Management System
Supports both BST and B-Tree implementations with full CRUD operations
"""

import sys
import os
import pandas as pd
import time
import datetime
from solution1_BST import BST, Supplier, Shipment, SupplierManagementBST # pyright: ignore[reportMissingImports]

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause and wait for user input"""
    input("\nPress Enter to continue...")

###############################################################################
# MENU DISPLAYS
###############################################################################
def display_home_menu():
    """Display main home menu"""
    print("\n" + "="*60)
    print("      FURNITURE SUPPLIER MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Use Binary Search Tree (BST)")
    print("2. Use B-Tree(Not done yet)")
    print("3. Exit")
    print("="*60)

def display_main_menu(system_type, total_suppliers, total_shipments):
    """Display main menu after selecting tree type"""
    print("\n" + "="*60)
    print(f"    MAIN MENU - Using {system_type}")
    print(f"    Total Suppliers: {total_suppliers} | Total Shipments: {total_shipments}")
    print("="*60)
    print("1. Supplier Management")
    print("2. Shipment Management")
    print("3. Load Supplier Data from CSV")
    print("4. Load Shipment Data from CSV")
    print("5. View All Suppliers")
    print("6. View All Shipments")
    print("7. System Statistics")
    print("8. Switch Tree Type")
    print("9. Exit")
    print("="*60)

def display_supplier_menu():
    """Display supplier management submenu"""
    print("\n" + "="*60)
    print("      SUPPLIER MANAGEMENT")
    print("="*60)
    print("1. Add Supplier")
    print("2. Search Supplier")
    print("3. Delete Supplier")
    print("4. Back to Main Menu")
    print("="*60)

def display_shipment_menu():
    """Display shipment management submenu"""
    print("\n" + "="*60)
    print("      SHIPMENT MANAGEMENT")
    print("="*60)
    print("1. Add Shipment")
    print("2. Search Shipment")
    print("3. Delete Shipment")
    print("4. Track Shipment by Status")
    print("5. Back to Main Menu")
    print("="*60)

###############################################################################
# SUPPLIER OPERATIONS
###############################################################################

def handle_add_supplier(manager):
    """Handle adding a new supplier"""
    print("\n" + "-"*60)
    print("ADD NEW SUPPLIER")
    print("-"*60)
    
    supplier_id = input("Supplier ID (e.g., SPL-00001): ").strip()
    
    # Check if supplier already exists
    if manager.search_supplier(supplier_id):
        print("X Error: Supplier ID already exists!")
        pause()
        return
    
    company = input("Company Name (e.g., Company Name.Sdn Bhd/Ltd./LLC): ").strip()
    contact_person = input("Contact Person (e.g., First Name,Last Name): ").strip()
    company_location = input("Company Location (e.g., KL,JB etc.,): ").strip()
    category = input("Category (e.g., table,benches,sofas,bookcase,chairs...): ").strip()
    
    try:
        rating = float(input("Rating (1.0-5.0): ").strip())
        if rating < 1.0 or rating > 5.0:
            print("!  Invalid rating. Using default 3.0")
            rating = 3.0
    except ValueError:
        print("! Invalid input. Using default rating 3.0")
        rating = 3.0
    
    # Create supplier object
    supplier = Supplier(supplier_id, company, contact_person, company_location, category, rating)
    
    # Add to system
    start_time = time.time()
    manager.add_supplier(supplier)
    elapsed = time.time() - start_time
    
    print(f"\n Supplier added successfully!")
    print(f" Time taken: {elapsed:.6f} seconds")
    pause()

def handle_search_supplier(manager):
    """Handle searching for a supplier"""
    print("\n" + "-"*60)
    print("SEARCH SUPPLIER")
    print("-"*60)
    
    supplier_id = input("Enter Supplier ID to search: ").strip()
    
    start_time = time.time()
    supplier = manager.search_supplier(supplier_id)
    elapsed = time.time() - start_time
    
    print(f"\nSearch completed in {elapsed:.6f} seconds")
    
    if supplier:
        print("\n✓ SUPPLIER FOUND")
        print("-"*60)
        print(f"ID:               {supplier.supplier_id}")
        print(f"Company:          {supplier.company}")
        print(f"Contact:          {supplier.contact_person}")
        print(f"Company Location: {supplier.company_location}")
        print(f"Category:         {supplier.category}")
        print(f"Rating:           {supplier.rating}")
        print("-"*60)
    else:
        print("\nX Supplier not found!")
    
    pause()

def handle_delete_supplier(manager):
    """Handle deleting a supplier"""
    print("\n" + "-"*60)
    print("DELETE SUPPLIER")
    print("-"*60)
    
    supplier_id = input("Enter Supplier ID to delete: ").strip()
    
    # First check if supplier exists
    supplier = manager.search_supplier(supplier_id)
    if not supplier:
        print("\nX Error: Supplier not found!")
        pause()
        return
    
    # Show supplier details
    print("\nSupplier to be deleted:")
    print(f"  {supplier}")
    
    confirm = input("\nAre you sure you want to delete? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        start_time = time.time()
        success = manager.delete_supplier(supplier_id)
        elapsed = time.time() - start_time
        
        if success:
            print(f"\n Supplier deleted successfully!")
            print(f" Time taken: {elapsed:.6f} seconds")
        else:
            print("\nX Error: Could not delete supplier!")
    else:
        print("\nX Deletion cancelled")
    
    pause()

def handle_print_all_suppliers(manager):
    """Handle printing all suppliers"""
    print("\n" + "-"*60)
    print("ALL SUPPLIERS")
    print("-"*60)
    
    stats = manager.get_statistics()
    total = stats.get('total_suppliers', 0)
    
    if total == 0:
        print("\n!  No suppliers in the system.")
        pause()
        return
    
    print(f"Total suppliers: {total}")
    display_all = input("Display all suppliers? (yes/no): ").strip().lower()
    
    if display_all not in ['yes', 'y']:
        display_count = input(f"How many to display? (max {total}): ").strip()
        try:
            display_count = min(int(display_count), total)
        except ValueError:
            display_count = 20
    else:
        display_count = total
    
    print(f"\nFetching suppliers... Please wait...")
    start_time = time.time()
    all_suppliers = manager.get_all_suppliers()
    elapsed = time.time() - start_time
    
    print(f"\n{'='*60}")
    print(f"SHOWING {min(display_count, len(all_suppliers))} OF {len(all_suppliers)} SUPPLIERS")
    print(f"{'='*60}")
    
    for i, (supplier_id, supplier) in enumerate(all_suppliers[:display_count], 1):
        print(f"{i:3d}. {supplier}")
    
    if len(all_suppliers) > display_count:
        print(f"\n... and {len(all_suppliers) - display_count} more suppliers")
    
    print(f"\nTraversal time: {elapsed:.4f} seconds")
    pause()

def handle_load_supplier_csv(manager):
    """Handle loading supplier data from CSV"""
    print("\n" + "-"*60)
    print("LOAD SUPPLIER DATA FROM CSV")
    print("-"*60)
    
    csv_file = "D:/UTM/SEM 3/Advance Data Structure/Assignment/Dataset & Output/supplier_dataset.csv"
    
    if not os.path.exists(csv_file):
        print(f"\nX Error: '{csv_file}' not found!")
        print("Please run dataset_generator.py first to create the dataset.")
        pause()
        return
    
    try:
        df = pd.read_csv(csv_file)
        print(f"\n Dataset loaded: {len(df)} suppliers available")
        
        print("\nHow many suppliers to load?")
        print(f" Available: {len(df)}")
        n = input(" Enter number (or 'all'): ").strip()
        
        if n.lower() == 'all':
            n = len(df)
        else:
            try:
                n = int(n)
                if n <= 0 or n > len(df):
                    print("X Invalid number!")
                    pause()
                    return
            except ValueError:
                print("X Invalid input!")
                pause()
                return
        
        # Sample data
        sample_df = df.sample(n, random_state=42)
        
        print(f"\nLoading {n} suppliers...")
        start_time = time.time()
        
        count = 0
        for _, row in sample_df.iterrows():
            supplier = Supplier(
                row['SupplierID'],
                row['Company Name'],
                row['Contact'],
                row['Company Location'],
                row['Category'],
                row['Rating']
            )
            manager.add_supplier(supplier)
            count += 1
            
            # Show progress every 1000 records
            if count % 1000 == 0:
                print(f"  Loaded {count}/{n}...")
        
        elapsed = time.time() - start_time
        
        print(f"\n Successfully loaded {n} suppliers")
        print(f" Time taken: {elapsed:.4f} seconds")
        print(f" Average insert time: {elapsed/n:.6f} seconds per supplier")
        
    except Exception as e:
        print(f"\nX Error loading data: {e}")
    
    pause()

###############################################################################
# SHIPMENT OPERATIONS
###############################################################################

def handle_add_shipment(manager):
    """Handle adding a new shipment"""
    print("\n" + "-"*60)
    print("ADD NEW SHIPMENT")
    print("-"*60)
    
    shipment_id = input("Shipment ID (e.g., SHP-00001): ").strip()
    
    # Check if shipment already exists
    if manager.search_shipment(shipment_id):
        print("X Error: Shipment ID already exists!")
        pause()
        return
    
    supplier_id = input("Supplier ID (e.g., SPL-00001): ").strip()
    product_type = input("Product Type(e.g., Wooden Chairs,Bookshelves,Coffee Tables,Leather Sofas etc.,): ").strip()
    
    try:
        quantity = int(input("Quantity: ").strip())
    except ValueError:
        print("!  Invalid input. Using default quantity 100")
        quantity = 100
    
    origin = input("Origin(e.g., Shanghai Port,Shenzhen Warehouse,Vietnam Factory,Port of Hong Kong):  ").strip()
    destination = input("Destination(e.g., Port Klang,Johor Port,Penang Port):  ").strip()
    status = input("Status (Preparing/In Transit/Delivered/Delayed): ").strip()
    
    # Create shipment object
    shipment = Shipment(
        shipment_id, supplier_id, product_type, quantity,
        origin, destination, status,
        datetime.datetime.now(),
        datetime.datetime.now() + datetime.timedelta(days=30)
    )
    
    # Add to system
    start_time = time.time()
    manager.add_shipment(shipment)
    elapsed = time.time() - start_time
    
    print(f"\n Shipment added successfully!")
    print(f" Time taken: {elapsed:.6f} seconds")
    pause()

def handle_search_shipment(manager):
    """Handle searching for a shipment"""
    print("\n" + "-"*60)
    print("SEARCH SHIPMENT")
    print("-"*60)
    
    shipment_id = input("Enter Shipment ID to search: ").strip()
    
    start_time = time.time()
    shipment = manager.search_shipment(shipment_id)
    elapsed = time.time() - start_time
    
    print(f"\nSearch completed in {elapsed:.6f} seconds")
    
    if shipment:
        print("\n SHIPMENT FOUND")
        print("-"*60)
        print(f"Shipment ID:      {shipment.shipment_id}")
        print(f"Supplier ID:      {shipment.supplier_id}")
        print(f"Product Type:     {shipment.product_type}")
        print(f"Quantity:         {shipment.quantity}")
        print(f"Origin:           {shipment.origin}")
        print(f"Destination:      {shipment.destination}")
        print(f"Status:           {shipment.status}")
        print("-"*60)
    else:
        print("\nX Shipment not found!")
    
    pause()

def handle_delete_shipment(manager):
    """Handle deleting a shipment"""
    print("\n" + "-"*60)
    print("DELETE SHIPMENT")
    print("-"*60)
    
    shipment_id = input("Enter Shipment ID to delete: ").strip()
    
    # First check if shipment exists
    shipment = manager.search_shipment(shipment_id)
    if not shipment:
        print("\nX Error: Shipment not found!")
        pause()
        return
    
    # Show shipment details
    print("\nShipment to be deleted:")
    print(f"  {shipment.shipment_id}: {shipment.product_type} - {shipment.status}")
    
    confirm = input("\nAre you sure you want to delete? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        start_time = time.time()
        success = manager.delete_shipment(shipment_id)
        elapsed = time.time() - start_time
        
        if success:
            print(f"\n Shipment deleted successfully!")
            print(f"  Time taken: {elapsed:.6f} seconds")
        else:
            print("\nX Error: Could not delete shipment!")
    else:
        print("\nX Deletion cancelled")
    
    pause()

def handle_track_by_status(manager):
    """Track shipments by status"""
    print("\n" + "-"*60)
    print("TRACK SHIPMENTS BY STATUS")
    print("-"*60)
    
    status = input("Enter status to search (Preparing/In Transit/Delivered/Delayed): ").strip()
    
    print(f"\nFetching all shipments...")
    all_shipments = manager.get_all_shipments()
    
    matching = [s for sid, s in all_shipments if s.status.lower() == status.lower()]
    
    if matching:
        print(f"\n Found {len(matching)} shipment(s) with status '{status}'")
        print("="*60)
        for i, shipment in enumerate(matching[:20], 1):
            print(f"{i}. {shipment.shipment_id}: {shipment.product_type} ({shipment.quantity} units)")
        if len(matching) > 20:
            print(f"... and {len(matching) - 20} more")
    else:
        print(f"\nX No shipments found with status '{status}'")
    
    pause()

def handle_print_all_shipments(manager):
    """Handle printing all shipments"""
    print("\n" + "-"*60)
    print("ALL SHIPMENTS")
    print("-"*60)
    
    stats = manager.get_statistics()
    total = stats.get('total_shipments', 0)
    
    if total == 0:
        print("\n! No shipments in the system.")
        pause()
        return
    
    print(f"Total shipments: {total}")
    display_all = input("Display all shipments? (yes/no): ").strip().lower()
    
    if display_all not in ['yes', 'y']:
        display_count = input(f"How many to display? (max {total}): ").strip()
        try:
            display_count = min(int(display_count), total)
        except ValueError:
            display_count = 20
    else:
        display_count = total
    
    print(f"\nFetching shipments... Please wait...")
    start_time = time.time()
    all_shipments = manager.get_all_shipments()
    elapsed = time.time() - start_time
    
    print(f"\n{'='*60}")
    print(f"SHOWING {min(display_count, len(all_shipments))} OF {len(all_shipments)} SHIPMENTS")
    print(f"{'='*60}")
    
    for i, (shipment_id, shipment) in enumerate(all_shipments[:display_count], 1):
        print(f"{i:3d}. {shipment.shipment_id}: {shipment.product_type} - {shipment.status}")
    
    if len(all_shipments) > display_count:
        print(f"\n... and {len(all_shipments) - display_count} more shipments")
    print(f"\nTraversal time: {elapsed:.4f} seconds")
    pause()

def handle_load_shipment_csv(manager):
    """Handle loading shipment data from CSV"""
    print("\n" + "-"*60)
    print("LOAD SHIPMENT DATA FROM CSV")
    print("-"*60)
    
    csv_file = "D:/UTM/SEM 3/Advance Data Structure/Assignment/Dataset & Output/shipment_dataset.csv"
    
    if not os.path.exists(csv_file):
        print(f"\nX Error: '{csv_file}' not found!")
        print("Please run dataset_generator.py first to create the dataset.")
        pause()
        return
    
    try:
        df = pd.read_csv(csv_file)
        print(f"\n✓ Dataset loaded: {len(df)} shipments available")
        
        print("\nHow many shipments to load?")
        print(f"  Available: {len(df)}")
        n = input("  Enter number (or 'all'): ").strip()
        
        if n.lower() == 'all':
            n = len(df)
        else:
            try:
                n = int(n)
                if n <= 0 or n > len(df):
                    print("X Invalid number!")
                    pause()
                    return
            except ValueError:
                print("X Invalid input!")
                pause()
                return
        
        # Sample data
        sample_df = df.sample(n, random_state=42)
        
        print(f"\nLoading {n} shipments...")
        start_time = time.time()
        
        count = 0
        for _, row in sample_df.iterrows():
            # Parse dates
            departure_date = datetime.datetime.strptime(row['DepartureDate'], "%Y-%m-%d")
            estimated_arrival = datetime.datetime.strptime(row['EstimatedArrival'], "%Y-%m-%d")
            actual_arrival = None
            if pd.notna(row['ActualArrival']) and row['ActualArrival']:
                actual_arrival = datetime.datetime.strptime(row['ActualArrival'], "%Y-%m-%d")
            
            shipment = Shipment(
                row['ShipmentID'],
                row['SupplierID'],
                row['ProductType'],
                row['Quantity'],
                row['Origin'],
                row['Destination'],
                row['Status'],
                departure_date,
                estimated_arrival
            )
            shipment.actual_arrival = actual_arrival
            
            manager.add_shipment(shipment)
            count += 1
            
            # Show progress every 1000 records
            if count % 1000 == 0:
                print(f"  Loaded {count}/{n}...")
        
        elapsed = time.time() - start_time
        
        print(f"\n Successfully loaded {n} shipments")
        print(f" Time taken: {elapsed:.4f} seconds")
        print(f" Average insert time: {elapsed/n:.6f} seconds per shipment")
        
    except Exception as e:
        print(f"\nX Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    pause()

def handle_system_statistics(manager):
    """Display system statistics"""
    print("\n" + "="*60)
    print("SYSTEM STATISTICS")
    print("="*60)
    
    stats = manager.get_statistics()
    
    for key, value in stats.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"{formatted_key:.<40} {value}")
    
    print("="*60)
    pause()

###############################################################################
# MENU LOOPS
###############################################################################
def supplier_management_loop(manager):
    """Supplier management menu loop"""
    while True:
        display_supplier_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            handle_add_supplier(manager)
        elif choice == '2':
            handle_search_supplier(manager)
        elif choice == '3':
            handle_delete_supplier(manager)
        elif choice == '4':
            break
        else:
            print("X Invalid choice! Please enter 1-4.")
            pause()

def shipment_management_loop(manager):
    """Shipment management menu loop"""
    while True:
        display_shipment_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            handle_add_shipment(manager)
        elif choice == '2':
            handle_search_shipment(manager)
        elif choice == '3':
            handle_delete_shipment(manager)
        elif choice == '4':
            handle_track_by_status(manager)
        elif choice == '5':
            break
        else:
            print("X Invalid choice! Please enter 1-5.")
            pause()

def main_menu_loop(manager, system_type):
    """Main menu loop"""
    while True:
        stats = manager.get_statistics()
        total_suppliers = stats.get('total_suppliers', 0)
        total_shipments = stats.get('total_shipments', 0)
        
        display_main_menu(system_type, total_suppliers, total_shipments)
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            supplier_management_loop(manager)
        elif choice == '2':
            shipment_management_loop(manager)
        elif choice == '3':
            handle_load_supplier_csv(manager)
        elif choice == '4':
            handle_load_shipment_csv(manager)
        elif choice == '5':
            handle_print_all_suppliers(manager)
        elif choice == '6':
            handle_print_all_shipments(manager)
        elif choice == '7':
            handle_system_statistics(manager)
        elif choice == '8':
            print("\nSwitching tree type...")
            break
        elif choice == '9':
            print("\n" + "="*60)
            print("Thank you for using the Furniture Supplier Management System!")
            print("="*60)
            sys.exit(0)
        else:
            print("X Invalid choice! Please enter 1-9.")
            pause()

###############################################################################
# MAIN APPLICATION
###############################################################################

def main():
    """Main application entry point"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  FURNITURE SUPPLIER MANAGEMENT SYSTEM  ".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    
    while True:
        display_home_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            # Initialize BST
            print("\n✓ Initializing Binary Search Tree (BST)...")
            manager = SupplierManagementBST()
            system_type = "Binary Search Tree (BST)"
            time.sleep(0.5)
            main_menu_loop(manager, system_type)
            
        elif choice == '2':
            # Initialize B-Tree
            print("Not done yet")

        elif choice == '3':
            print("\n" + "="*60)
            print("Thank you for using the Furniture Supplier Management System!")
            print("Goodbye!")
            print("="*60)
            break
            
        else:
            print("X Invalid choice! Please enter 1-3.")
            pause()

if __name__ == "__main__":
    try:
        sys.setrecursionlimit(50000)
        main()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("Program interrupted by user. Exiting...")
        print("="*60)
        sys.exit(0)