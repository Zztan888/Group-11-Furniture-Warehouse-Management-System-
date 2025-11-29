from src.order_bst import OrderBST 

def demonstrate_bst_operations():
    
    # Initialize the BST 
    order_tree = OrderBST()
    print("=" * 60)
    print("Customer Order & Delivery Management Module BST Demonstration")
    print("=" * 60)
    
    # Demonstration
    # --- 1. Insert ---
    print("--- 1. Insert ---")

    # Initializa dataset by inserting a sample set of orders to build the tree structure
    order_tree.add_order(30, 101, ('Laptop', 3), "123 Main Street")
    order_tree.add_order(60, 102, ('Monitor', 2), "456 Queenstown")
    order_tree.add_order(90, 103, ('Keyboard', 6), "789 Taman Durian")
    order_tree.add_order(45, 104, ('Mouse', 12), "111, First Town")
    order_tree.add_order(75, 105, ('Webcam', 8), "222, Dorian Street")
    order_tree.add_order(15, 106, ('Earphone', 30), "333, Taman Garden")
    
    # Attempt to insert duplcate
    order_tree.add_order(30, 101, ('Laptop', 6), "123 Main Street")

    print("------------------------------------------")

    # --- 2. Display ---
    print("--- 2. Display ---")

    order_tree.display_all_sorted()

    print("------------------------------------------")
    
    # --- 3. Search ---
    print("--- 3. Search ---")

    # Success Case
    search_id_1 = 30
    found_order_1 = order_tree.find_order(search_id_1)
    if found_order_1:
        print(f"FOUND Order {search_id_1}: {found_order_1}")
    
    # Failure Case
    search_id_2 = 99
    found_order_2 = order_tree.find_order(search_id_2)
    if not found_order_2:
        print(f"Order {search_id_2} not found in the BST.")

    print("------------------------------------------")

    # --- 4. Update ---
    print("--- 4. Update ---")

    # Update an existing order
    order_tree.update_order_status(30, "In Transit")
    found_order_update = order_tree.find_order(30)
    if found_order_update:
        print(f"Order 30: {found_order_update}")
    
    # Attempt to update a non-existent order
    order_tree.update_order_status(99, "Delivered")
    print("------------------------------------------")
    
    # --- 5. Delete ---
    print("--- 5. Delete ---")

    # Case 1
    order_tree.delete_order(90)
    found_order_delete_1 = order_tree.find_order(90)
    if found_order_delete_1 is None:
        print(f"--- Order 90 is deleted or not found. ---")
    
    # Case 2
    order_tree.delete_order(30)
    found_order_delete_2 = order_tree.find_order(30)
    if found_order_delete_2 is None:
        print(f"--- Order 30 is deleted or not found. ---")
    
    # Final verification display
    order_tree.display_all_sorted()
    
    # Attempt to delete a non-existent order
    order_tree.delete_order(150)

    print("------------------------------------------")

if __name__ == "__main__":
    demonstrate_bst_operations()