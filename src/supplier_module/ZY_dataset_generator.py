"""
dataset_generator.py
Generates fixed random datasets of furniture suppliers and shipments, saving as CSV files.
Run this once to create supplier_dataset.csv and shipment_dataset.csv for consistent testing.
"""

import random
import pandas as pd
import datetime

class Supplier:
    def __init__(self, supplier_id, company, contact_person, company_location, category, rating):
        self.supplier_id = supplier_id
        self.company = company
        self.contact_person = contact_person
        self.company_location = company_location
        self.category = category
        self.rating = rating

class Shipment:
    def __init__(self, shipment_id, supplier_id, product_type, quantity, origin, destination, 
                 status, departure_date, estimated_arrival):
        self.shipment_id = shipment_id
        self.supplier_id = supplier_id
        self.product_type = product_type
        self.quantity = quantity
        self.origin = origin
        self.destination = destination
        self.status = status
        self.departure_date = departure_date
        self.estimated_arrival = estimated_arrival
        self.actual_arrival = None
        self.tracking_updates = []

    def add_tracking_update(self, update, location=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if location:
            self.tracking_updates.append(f"{timestamp} - {location}: {update}")
        else:
            self.tracking_updates.append(f"{timestamp}: {update}")

class DataGenerator:
    def __init__(self):
        self.furniture_companies = [
            "Comfort Craft Furniture", "Elegant Living Designs", "Wood Master Creations",
            "Modern Home Furnishings", "Classic Comfort Interiors", "Luxury Living Spaces",
            "Artisan Woodworks", "Contemporary Style Co.", "Heritage Furniture Makers",
            "Premium Seating Solutions", "Table Masters Inc.", "Bedroom Bliss Creations",
            "Office Pro Furnishings", "Outdoor Living Designs", "Space Savers Furniture"
        ]
        
        self.furniture_categories = [
            "Chairs", "Sofas", "Tables", "Beds", "Desks", "Cabinets", "Shelving",
            "Office Furniture", "Outdoor Furniture", "Dining Sets", "Bar Stools",
            "Recliners", "Benches", "Bookcases", "Wardrobes"
        ]
        
        self.materials = ["Wood", "Metal", "Leather", "Fabric", "Plastic", "Glass", "Rattan"]
        self.company_locations = ["Johor Baharu", "Kuala Lumpur", "Batu Pahat", "Muar", "Kulai"]
        self.first_names = ["John", "Jane", "Robert", "Maria", "Jeff", "Sarah", "Michael", "Emma"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Alice", "Garcia", "Lee"]
        
        # Shipment-related data
        self.product_types = [
            "Wooden Chairs", "Leather Sofas", "Office Desks", "Dining Tables", 
            "Bookshelves", "Bed Frames", "Bar Stools", "Coffee Tables",
            "Wardrobes", "Console Tables", "Accent Chairs", "TV Stands"
        ]
        self.origins = ["Shanghai Port", "Shenzhen Warehouse", "Vietnam Factory", "Port of Hong Kong", "Indonesia Facility"]
        self.destinations = ["Port Klang", "Johor Port", "Port of Tanjung Pelepas", "Kuantan Port", "Penang Port"]
    
    def generate_suppliers(self, n):
        """Generate n unique suppliers"""
        suppliers = []
        used_ids = set()
        
        for i in range(n):
            # Generate Supplier id (SPL-00001)
            supplier_id = f"SPL-{i+1:05d}"
            while supplier_id in used_ids:
                i += 1
                supplier_id = f"SPL-{i+1:05d}"
            used_ids.add(supplier_id)
            
            # Generate company name
            company_base = random.choice(self.furniture_companies)
            company_suffix = random.choice([" LLC", " Inc.", " Corp.", " Ltd.", " Co.", " Sdn Bhd"])
            company = company_base + company_suffix
            
            # Add material prefix 
            if random.random() > 0.7:
                material = random.choice(self.materials)
                company = f"{material} {company}"
            
            # Generate other attributes
            contact_person = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            company_location = random.choice(self.company_locations)
            category = random.choice(self.furniture_categories)
            rating = round(random.uniform(2.5, 5.0), 1)
            
            supplier = Supplier(supplier_id, company, contact_person, company_location, category, rating)
            suppliers.append(supplier)
        
        return suppliers
    
    def generate_shipments(self, n, suppliers):
        """Generate n shipments for the given suppliers"""
        shipments = []
        used_ids = set()
        
        # Status weights distribution
        status_weights = ['Preparing'] * 15 + ['In Transit'] * 50 + ['Delayed'] * 10 + ['Delivered'] * 25
        
        for i in range(n):
            # Generate Shipment id (SHP-00001)
            shipment_id = f"SHP-{i+1:05d}"
            while shipment_id in used_ids:
                i += 1
                shipment_id = f"SHP-{i+1:05d}"
            used_ids.add(shipment_id)
            
            # Select a random supplier
            supplier = random.choice(suppliers)
            supplier_id = supplier.supplier_id
            
            # Generate shipment details
            product_type = random.choice(self.product_types)
            quantity = random.randint(10, 500)
            origin = random.choice(self.origins)
            destination = random.choice(self.destinations)
            status = random.choice(status_weights)
            
            # Generate dates
            days_ago = random.randint(1, 180)  # Up to 6 months ago
            departure_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
            est_days = random.randint(15, 90)  # 15-90 days transit
            estimated_arrival = departure_date + datetime.timedelta(days=est_days)
            
            # Create shipment
            shipment = Shipment(
                shipment_id, supplier_id, product_type, quantity,
                origin, destination, status, departure_date, estimated_arrival
            )
            
            # Add tracking updates based on status
            if status in ['In Transit', 'Delayed', 'Delivered']:
                shipment.add_tracking_update("Departured from origin", origin)
                shipment.add_tracking_update("Customs clearance completed")
                
                if status in ['Delayed', 'Delivered']:
                    shipment.add_tracking_update("Vessel arrived at intermediate port")
                    
                if status == 'Delivered':
                    # Actual arrival is before or around estimated arrival
                    days_variance = random.randint(-10, 5)
                    shipment.actual_arrival = estimated_arrival + datetime.timedelta(days=days_variance)
                    shipment.add_tracking_update("Delivered to destination", destination)
                elif status == 'Delayed':
                    shipment.add_tracking_update("Weather delay - revised ETA", "Pacific Ocean")
            
            shipments.append(shipment)
        return shipments

def main():
    """Generate and save datasets"""
    print("="*60)
    print("FURNITURE SUPPLIER & SHIPMENT DATASET GENERATOR")
    print("="*60)
    
    # Fixed seed
    random.seed(42)
    
    # Generate 30,000 suppliers and 50,000 shipments
    n_suppliers = 30000
    n_shipments = 50000
    
    print(f"\nGenerating {n_suppliers} furniture suppliers...")
    
    generator = DataGenerator()
    suppliers = generator.generate_suppliers(n_suppliers)
    
    # Convert suppliers to DataFrame
    supplier_df = pd.DataFrame([{
        "SupplierID": s.supplier_id,
        "Company Name": s.company,
        "Contact": s.contact_person,
        "Company Location": s.company_location,
        "Category": s.category,
        "Rating": s.rating
    } for s in suppliers])
    
    # Save suppliers to CSV
    supplier_output_file = "D:/UTM/SEM 3/Advance Data Structure/Assignment/Dataset & Output/supplier_dataset.csv"
    supplier_df.to_csv(supplier_output_file, index=False)
    
    print(f" Successfully generated {len(supplier_df)} suppliers")
    print(f" Supplier dataset saved to '{supplier_output_file}'")
    print(f"\nSupplier Dataset Statistics:")
    print(f"  - Total Suppliers: {len(supplier_df)}")
    print(f"  - Number of Columns: {supplier_df.shape[1]}")  
    print(f"  - Columns: {list(supplier_df.columns)}")
    print(f"  - Average Rating: {supplier_df['Rating'].mean():.2f}")
    print(f"\nSample Supplier Data (first 5 rows):")
    print(supplier_df.head().to_string(index=False))

    # Generate shipments
    print(f"\nGenerating {n_shipments} furniture shipments...")
    shipments = generator.generate_shipments(n_shipments, suppliers)
    
    # Convert shipments to DataFrame
    shipment_df = pd.DataFrame([{
        "ShipmentID": s.shipment_id,
        "SupplierID": s.supplier_id,
        "ProductType": s.product_type,
        "Quantity": s.quantity,
        "Origin": s.origin,
        "Destination": s.destination,
        "Status": s.status,
        "DepartureDate": s.departure_date.strftime("%Y-%m-%d"),
        "EstimatedArrival": s.estimated_arrival.strftime("%Y-%m-%d"),
        "ActualArrival": s.actual_arrival.strftime("%Y-%m-%d") if s.actual_arrival else "",
        "TrackingUpdates": "; ".join(s.tracking_updates) if s.tracking_updates else ""
    } for s in shipments])
    
    # Save shipments to CSV
    shipment_output_file = "D:/UTM/SEM 3/Advance Data Structure/Assignment/Dataset & Output/shipment_dataset.csv"
    shipment_df.to_csv(shipment_output_file, index=False)
    
    print(f" Successfully generated {len(shipment_df)} shipments")
    print(f" Shipment dataset saved to '{shipment_output_file}'")
    
    # Print statistics
    print(f"\nShipment Dataset Statistics:")
    print(f"  - Total Shipments: {len(shipment_df)}")
    print(f"  - Number of Columns: {shipment_df.shape[1]}")  
    print(f"  - Columns: {list(shipment_df.columns)}")
    print(f"  - Total Shipments: {len(shipment_df)}")
    print(f"  - Shipment Status Distribution:")
    status_counts = shipment_df['Status'].value_counts()
    for status, count in status_counts.items():
        percentage = (count / len(shipment_df)) * 100
        print(f"      {status}: {count} ({percentage:.1f}%)")
    
    print(f"\nSample Shipment Data (first 5 rows):")
    print(shipment_df.head().to_string(index=False))
    
    print("\n Dataset generation complete!")

if __name__ == "__main__":
    main()