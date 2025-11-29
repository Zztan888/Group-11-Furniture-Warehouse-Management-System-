import datetime

class OrderNode:
    def __init__(self, order_id, customer_id, item_details, delivery_address, order_date=None, status='Pending'):
        # Primary Key
        self.order_id = order_id

        # Essential Attribute
        self.customer_id = customer_id
        self.item_details = item_details # Simple item tracking, eg: [{'Earphone', 1}]
        self.delivery_address = delivery_address
        self.delivery_status = status # Field required for the update operation
        
        # auto set order_date when order is created
        if order_date is None:
            self.order_date = datetime.date.today()
        else:
            self.order_date = order_date
        
        # BST Pointers
        self.left = None
        self.right = None

    def __str__(self):
        return f"ID: {self.order_id} | Customer: {self.customer_id} | Status: {self.delivery_status} | Items: {self.item_details}"

class OrderBST:
    def __init__(self):
        self.root = None
        
    def add_order(self, order_id, customer_id, item_details, delivery_address):
        new_node = OrderNode(order_id, customer_id, item_details, delivery_address)
        if self.root is None:
            self.root = new_node
            print(f"Order {order_id} added successfully.")
            return True
        return self._insert_binary_tree(self.root, new_node)

    def _insert_binary_tree(self, current_node, new_node):
        #  Travel to left
        if new_node.order_id < current_node.order_id:
            if current_node.left is None:
                current_node.left = new_node
                print(f"Order {new_node.order_id} added left of {current_node.order_id}.")
                return True
            else:
                return self._insert_binary_tree(current_node.left, new_node)
        # Travel to right
        elif new_node.order_id > current_node.order_id:
            if current_node.right is None:
                current_node.right = new_node
                print(f"Order {new_node.order_id} added right of {current_node.order_id}.")
                return True
            else:
                return self._insert_binary_tree(current_node.right, new_node)
        print(f"Insertion failed: Order ID {new_node.order_id} already exists.")
        return False
    
    def display_all_sorted(self):
        print("--- Displaying All Orders Sorted by ID ---")
        if self.root is None:
            print("The order tree is currently empty.")
            return

        self._in_order_traversal(self.root)
        print("------------------------------------------")

    def _in_order_traversal(self, current_node):
        if current_node is not None:
            # Travel to left to find leftmost node
            self._in_order_traversal(current_node.left)
            
            print(current_node)

            # Travel to right to continue print
            self._in_order_traversal(current_node.right)
            
    def find_order(self, order_id):
        return self._find_binary_tree(self.root, order_id)
    
    def _find_binary_tree(self, current_node, order_id):
        if current_node is None: # Search failed (Node not found)
            return None

        if current_node.order_id == order_id:
            return current_node

        if order_id < current_node.order_id:
            return self._find_binary_tree(current_node.left, order_id)
        else:
            return self._find_binary_tree(current_node.right, order_id)

    def update_order_status(self, order_id, status):
        node_to_update = self.find_order(order_id)

        if node_to_update:
            node_to_update.delivery_status = status
            print(f"Status changed to '{status}' for order {order_id}.")
            return True
        else:
            print(f"Update failed: Order {order_id} not found for status update.")
            return False

    def delete_order(self, order_id):
        target_order = self.find_order(order_id)
        if target_order == None:
            print(f"Order {order_id} not found.")
            return False

        original_root = self.root
        self.root = self._delete_binary_tree(self.root, order_id)
        
        if self.root != original_root or self.find_order(order_id) is None:
            print(f"Order {order_id} deleted successfully.")
            return True
        else:
            print(f"Order {order_id} not found.")
            return False

    def _find_min_node(self, node):
        # Helper to find the smallest (leftmost) node in a given subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_binary_tree(self, current_node, order_id):
        if current_node is None: # Search failed (Node not found)
            return None

        if order_id < current_node.order_id:
            current_node.left = self._delete_binary_tree(current_node.left, order_id) # Continue to search left tree
        elif order_id > current_node.order_id:
            current_node.right = self._delete_binary_tree(current_node.right, order_id) # Continue to search right tree
        else:
            if current_node.left is None:
                return current_node.right #  Returns the right child
            if current_node.right is None:
                return current_node.left  #  Returns the left child

            successor = self._find_min_node(current_node.right)
            current_node.order_id = successor.order_id
            current_node.customer_id = successor.customer_id
            current_node.delivery_address = successor.delivery_address
            current_node.item_details = successor.item_details
            current_node.delivery_status = successor.delivery_status

            current_node.right = self._delete_binary_tree(current_node.right, successor.order_id)
            
        return current_node
        