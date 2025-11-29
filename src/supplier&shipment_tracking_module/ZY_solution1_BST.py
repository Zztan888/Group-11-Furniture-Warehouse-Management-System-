"""
solution1_BST.py
Furniture Supplier and Shipment Tracking System using Binary Search Tree (BST)
Implements insert, search and delete operations.
"""

import datetime
import time

# DATA CLASSES
class Supplier:
    def __init__(self, supplier_id, company, contact_person, company_location, category, rating):
        self.supplier_id = supplier_id
        self.company = company
        self.contact_person = contact_person
        self.company_location = company_location
        self.category = category
        self.rating = rating
    
    def __str__(self):
        return f"{self.supplier_id} : {self.company} ( {self.company_location} ) {self.contact_person} | {self.category} - Rating: {self.rating}"

class Shipment:
    def __init__(self, shipment_id, supplier_id, product_type, quantity, 
                 origin, destination, status, departure_date, estimated_arrival):
        self.shipment_id = shipment_id
        self.supplier_id = supplier_id
        self.product_type = product_type
        self.quantity = quantity
        self.origin = origin
        self.destination = destination
        self.status = status
        self.departure_date = departure_date
        self.estimated_arrival = estimated_arrival
        self.tracking_updates = []
    
    def add_tracking_update(self, update_text, location=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        update = f"[{timestamp}] {update_text}"
        if location:
            update += f" at {location}"
        self.tracking_updates.append(update)


# BST Implementation
class BSTNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    # Insert operation
    def insert(self, key, data):
        """Insert a key-value pair into the BST"""
        if self.root is None:
            self.root = BSTNode(key, data)
            self.size += 1
            return True
        
        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    current.left = BSTNode(key, data)
                    self.size += 1
                    return True
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = BSTNode(key, data)
                    self.size += 1
                    return True
                current = current.right
            else:
                current.data = data
                return False
    
    # Search Operation
    def search(self, key):
        """Search for a key in the BST and return the node"""
        current = self.root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    
    # Delete Operation
    def delete(self, key):
        """Delete a key from the BST - Iterative implementation"""
        parent = None
        current = self.root
        
        # Find the node and its parent
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        if not current:
            return False  
        
        # Case 1: Node has no children or only one child
        if not current.left or not current.right:
            new_child = current.left if current.left else current.right
            
            if not parent:
                self.root = new_child
            elif parent.left == current:
                parent.left = new_child
            else:
                parent.right = new_child
        
        # Case 2: Node has two children
        else:
            # Find inorder successor (minimum in right subtree)
            successor_parent = current
            successor = current.right
            
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # Replace current node's data with successor's data
            current.key = successor.key
            current.data = successor.data
            
            # Delete successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        self.size -= 1
        return True

    # Inorder traversal (sort ascending)
    def in_order_traversal(self):
        """Return all key-value pairs in sorted order"""
        result = []
        self._in_order_helper(self.root, result)
        return result
    
    def _in_order_helper(self, node, result):
        if node:
            self._in_order_helper(node.left, result)
            result.append((node.key, node.data))
            self._in_order_helper(node.right, result)

# Supplier & Shipment System
class SupplierManagementBST:
    def __init__(self):
        self.supplier_tree = BST()
        self.shipment_tree = BST()
    
    def add_supplier(self, supplier):
        """Add a supplier to the system"""
        return self.supplier_tree.insert(supplier.supplier_id, supplier)
    
    def search_supplier(self, supplier_id):
        """Search for a supplier by ID"""
        node = self.supplier_tree.search(supplier_id)
        return node.data if node else None
    
    def delete_supplier(self, supplier_id):
        """Delete a supplier from the system"""
        return self.supplier_tree.delete(supplier_id)
    
    def add_shipment(self, shipment):
        """Add a shipment to the system"""
        return self.shipment_tree.insert(shipment.shipment_id, shipment)
    
    def search_shipment(self, shipment_id):
        """Search for a shipment by ID"""
        node = self.shipment_tree.search(shipment_id)
        return node.data if node else None
    
    def delete_shipment(self, shipment_id):
        """Delete a shipment from the system"""
        return self.shipment_tree.delete(shipment_id)
    
    def get_all_suppliers(self):
        """Get all suppliers in sorted order"""
        return self.supplier_tree.in_order_traversal()
    
    def get_all_shipments(self):
        """Get all shipments in sorted order"""
        return self.shipment_tree.in_order_traversal()
    
    def get_statistics(self):
        """Get system statistics"""
        return {
            'total_suppliers': self.supplier_tree.size,
            'total_shipments': self.shipment_tree.size
        }