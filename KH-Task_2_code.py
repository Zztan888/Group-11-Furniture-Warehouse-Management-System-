# MECS1023 Advance DSA Group 11
# Student: Tee Kah Hock MEC245061
# Title : Furniture Inventory Control Module

import csv
import time

# 1. ABSTRACT DATA TYPE (ADT): The class for FurnitureItem holds all relevant details from csv file. 

class FurnitureItem:
    def __init__(self, sku, item_name, category, material, color, 
                 warehouse_location, quantity, supplier, last_updated, description):
        self.sku = sku.strip()  # The Unique Key
        self.item_name = item_name
        self.category = category
        self.material = material
        self.color = color
        self.warehouse_location = warehouse_location
        self.quantity = quantity
        self.supplier = supplier
        self.last_updated = last_updated
        self.description = description

     # This is the format structure to print all relevant details
    def __str__(self):
        return (f"SKU: {self.sku} | Name: {self.item_name} | Category: {self.category} | Material:{self.material} |Qty: {self.quantity} | Loc: {self.warehouse_location} | Supplier: {self.supplier}")


# 2. BST NODE: Create the node structure for the BST, the left and right pointers. 

class BSTNode:
    def __init__(self, furniture_item):
        self.data = furniture_item
        self.left = None
        self.right = None


# 3. BINARY SEARCH TREE IMPLEMENTATION

class FurnitureBST:
    def __init__(self):
        self.root = None

    # INSERT OPERATION
    def insert(self, furniture_item):
        if self.root is None:
            self.root = BSTNode(furniture_item)
        else:
            self._insert_operation(self.root, furniture_item)

    def _insert_operation(self, current_node, new_item):
        if new_item.sku < current_node.data.sku:
            if current_node.left is None:
                current_node.left = BSTNode(new_item)
            else:
                self._insert_operation(current_node.left, new_item)
        elif new_item.sku > current_node.data.sku:
            if current_node.right is None:
                current_node.right = BSTNode(new_item)
            else:
                self._insert_operation(current_node.right, new_item)
        else:
            print(f"Duplicate SKU found: {new_item.sku}. Item not added.")

    # SEARCH OPERATION
    def search(self, sku):
        return self._search_operation(self.root, sku)

    def _search_operation(self, current_node, sku):
        if current_node is None:
            return None
        if sku == current_node.data.sku:
            return current_node.data
        elif sku < current_node.data.sku:
            return self._search_operation(current_node.left, sku)
        else:
            return self._search_operation(current_node.right, sku)

    # DELETE OPERATION
    def delete(self, sku):
        self.root = self._delete_recursive(self.root, sku)

    def _delete_recursive(self, current_node, sku):
        if current_node is None:
            return current_node

        # Find the node to delete
        if sku < current_node.data.sku:
            current_node.left = self._delete_recursive(current_node.left, sku)
        elif sku > current_node.data.sku:
            current_node.right = self._delete_recursive(current_node.right, sku)
        else:
            # Node found. Handle 3 cases:
            
            # Case 1: Node has no children (Leaf)
            if current_node.left is None and current_node.right is None:
                return None
            
            # Case 2: Node has one child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            
            # Case 3: Node has two children
            # Find the in-order successor (smallest node in the right subtree)
            min_larger_node = self._get_min(current_node.right)
            # Copy that data to the current node
            current_node.data = min_larger_node.data
            # Delete the successor node from the right subtree
            current_node.right = self._delete_recursive(current_node.right, min_larger_node.data.sku)

        return current_node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


# 4. MAIN APPLICATION

def load_data_from_csv(filename, bst):
    print(f"Loading data from {filename}...")
    count = 0
    try:
        with open(filename, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = FurnitureItem(
                    row['SKU'], row['ItemName'], row['Category'], 
                    row['Material'], row['Color'], row['WarehouseLocation'], 
                    row['Quantity'], row['Supplier'], row['LastUpdated'], 
                    row['Description']
                )
                bst.insert(item)
                count += 1
        print(f"Successfully loaded {count} records into the BST.")
    except FileNotFoundError:
        print("Error: File not found. Make sure the CSV is in the same folder.")
    except Exception as e:
        print(f"Error loading data: {e}")

def main():
    # Initialize Tree
    inventory_tree = FurnitureBST()
    
    # Load Data
    csv_filename = 'Furniture Inventory.csv' 
    load_data_from_csv(csv_filename, inventory_tree)

    # Interactive Menu
    while True:
        print("\n" + "="*40)
        print(" FURNITURE INVENTORY CONTROL (BST) ")
        print("="*40)
        print("1. Search Item (by SKU)")
        print("2. Add New Item")
        print("3. Remove Item")
        print("4. Check Root Node (Verify Tree)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == '1':
            sku = input("Enter SKU to search: ").strip()

            start_time = time.perf_counter() # Start timer
            result = inventory_tree.search(sku)
            end_time = time.perf_counter()   # Stop timer
            processing_time = (end_time - start_time) * 1000 # Convert to milliseconds
            
            if result:
                print("\n--- ITEM FOUND ---")
                print(result)
            else:
                print("\n[!] Item not found.")
            print(f"[i] Search Operation Time: {processing_time:.6f} milliseconds")

        elif choice == '2':
            print("\n--- ADD NEW ITEM ---")
            sku = input("SKU: ").strip()
            if inventory_tree.search(sku):
                print("[!] SKU already exists. Cannot add duplicate.")
                continue
                
            # This is the input that require user to fill in for new added item. 
            name = input("Item Name: ")
            cat = input("Category: ")
            material = input("Material:")
            color = input("color:")
            Quantity = input("Quantity:")
            Location = input("Location:")
            Supplier = input ("Supplier:")
            item = FurnitureItem(sku, name, cat, material, color , Quantity, Location, Supplier, "2025-11-19", "New item")
            start_time = time.perf_counter() # Start timer
            inventory_tree.insert(item)
            end_time = time.perf_counter()   # Stop timer
            
            processing_time = (end_time - start_time) * 1000 # Convert to milliseconds
            print(f"\n[+] Item {sku} added successfully.")
            print(f"[i] Insertion Operation Time: {processing_time:.6f} milliseconds")

        elif choice == '3':
            sku = input("Enter SKU to delete: ").strip()
            if inventory_tree.search(sku):
                inventory_tree.delete(sku)
                print(f"\n[-] Item {sku} deleted successfully.")
            else:
                print("[!] Item not found, cannot delete.")

        elif choice == '4':
            if inventory_tree.root:
                print(f"Root Node SKU: {inventory_tree.root.data.sku}")
            else:
                print("Tree is empty.")

        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()