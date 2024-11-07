# ERP Program without Classes (Python)

import datetime
import random
import pickle

# --- Data Structures ---

# Product Data
products = {}

# Customer Data
customers = {}

# Employee Data
employees = {}

# Orders Data
orders = {}

# --- Functions ---

# --- Product Functions ---

def add_product():
    """Adds a new product to the products dictionary."""
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    product_price = float(input("Enter Product Price: "))
    product_quantity = int(input("Enter Product Quantity: "))
    products[product_id] = {
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    }
    print(f"Product {product_name} added successfully!")

def view_products():
    """Displays all products."""
    if not products:
        print("No products available.")
        return
    print("-" * 40)
    print("Product ID | Product Name | Price | Quantity")
    print("-" * 40)
    for product_id, product_details in products.items():
        print(f"{product_id}        | {product_details['name']}          | {product_details['price']} | {product_details['quantity']}")
    print("-" * 40)

def update_product():
    """Updates an existing product."""
    product_id = input("Enter Product ID to update: ")
    if product_id not in products:
        print("Product not found.")
        return
    print(f"Current Details: {products[product_id]}")
    update_choice = input("What do you want to update (name/price/quantity/all/cancel): ")
    if update_choice.lower() == "name":
        products[product_id]["name"] = input("Enter new name: ")
    elif update_choice.lower() == "price":
        products[product_id]["price"] = float(input("Enter new price: "))
    elif update_choice.lower() == "quantity":
        products[product_id]["quantity"] = int(input("Enter new quantity: "))
    elif update_choice.lower() == "all":
        products[product_id]["name"] = input("Enter new name: ")
        products[product_id]["price"] = float(input("Enter new price: "))
        products[product_id]["quantity"] = int(input("Enter new quantity: "))
    elif update_choice.lower() == "cancel":
        print("Update cancelled.")
        return
    else:
        print("Invalid choice.")
        return
    print("Product updated successfully!")

def delete_product():
    """Deletes a product."""
    product_id = input("Enter Product ID to delete: ")
    if product_id not in products:
        print("Product not found.")
        return
    del products[product_id]
    print("Product deleted successfully!")

# --- Customer Functions ---

def add_customer():
    """Adds a new customer."""
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    customer_address = input("Enter Customer Address: ")
    customer_phone = input("Enter Customer Phone Number: ")
    customers[customer_id] = {
        "name": customer_name,
        "address": customer_address,
        "phone": customer_phone
    }
    print(f"Customer {customer_name} added successfully!")

def view_customers():
    """Displays all customers."""
    if not customers:
        print("No customers available.")
        return
    print("-" * 40)
    print("Customer ID | Customer Name | Address | Phone")
    print("-" * 40)
    for customer_id, customer_details in customers.items():
        print(f"{customer_id}        | {customer_details['name']}          | {customer_details['address']} | {customer_details['phone']}")
    print("-" * 40)

def update_customer():
    """Updates an existing customer."""
    customer_id = input("Enter Customer ID to update: ")
    if customer_id not in customers:
        print("Customer not found.")
        return
    print(f"Current Details: {customers[customer_id]}")
    update_choice = input("What do you want to update (name/address/phone/all/cancel): ")
    if update_choice.lower() == "name":
        customers[customer_id]["name"] = input("Enter new name: ")
    elif update_choice.lower() == "address":
        customers[customer_id]["address"] = input("Enter new address: ")
    elif update_choice.lower() == "phone":
        customers[customer_id]["phone"] = input("Enter new phone number: ")
    elif update_choice.lower() == "all":
        customers[customer_id]["name"] = input("Enter new name: ")
        customers[customer_id]["address"] = input("Enter new address: ")
        customers[customer_id]["phone"] = input("Enter new phone number: ")
    elif update_choice.lower() == "cancel":
        print("Update cancelled.")
        return
    else:
        print("Invalid choice.")
        return
    print("Customer updated successfully!")

def delete_customer():
    """Deletes a customer."""
    customer_id = input("Enter Customer ID to delete: ")
    if customer_id not in customers:
        print("Customer not found.")
        return
    del customers[customer_id]
    print("Customer deleted successfully!")

# --- Employee Functions ---

def add_employee():
    """Adds a new employee."""
    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name: ")
    employee_salary = float(input("Enter Employee Salary: "))
    employee_department = input("Enter Employee Department: ")
    employees[employee_id] = {
        "name": employee_name,
        "salary": employee_salary,
        "department": employee_department
    }
    print(f"Employee {employee_name} added successfully!")

def view_employees():
    """Displays all employees."""
    if not employees:
        print("No employees available.")
        return
    print("-" * 40)
    print("Employee ID | Employee Name | Salary | Department")
    print("-" * 40)
    for employee_id, employee_details in employees.items():
        print(f"{employee_id}        | {employee_details['name']}          | {employee_details['salary']} | {employee_details['department']}")
    print("-" * 40)

def update_employee():
    """Updates an existing employee."""
    employee_id = input("Enter Employee ID to update: ")
    if employee_id not in employees:
        print("Employee not found.")
        return
    print(f"Current Details: {employees[employee_id]}")
    update_choice = input("What do you want to update (name/salary/department/all/cancel): ")
    if update_choice.lower() == "name":
        employees[employee_id]["name"] = input("Enter new name: ")
    elif update_choice.lower() == "salary":
        employees[employee_id]["salary"] = float(input("Enter new salary: "))
    elif update_choice.lower() == "department":
        employees[employee_id]["department"] = input("Enter new department: ")
    elif update_choice.lower() == "all":
        employees[employee_id]["name"] = input("Enter new name: ")
        employees[employee_id]["salary"] = float(input("Enter new salary: "))
        employees[employee_id]["department"] = input("Enter new department: ")
    elif update_choice.lower() == "cancel":
        print("Update cancelled.")
        return
    else:
        print("Invalid choice.")
        return
    print("Employee updated successfully!")

def delete_employee():
    """Deletes an employee."""
    employee_id = input("Enter Employee ID to delete: ")
    if employee_id not in employees:
        print("Employee not found.")
        return
    del employees[employee_id]
    print("Employee deleted successfully!")

# --- Order Functions ---

def place_order():
    """Places a new order."""
    order_id = str(random.randint(1000, 9999))
    while order_id in orders:
        order_id = str(random.randint(1000, 9999))
    customer_id = input("Enter Customer ID: ")
    if customer_id not in customers:
        print("Customer not found.")
        return
    order_date = datetime.datetime.now().strftime("%Y-%m-%d")
    order_items = []
    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ")
        if product_id.lower() == "done":
            break
        if product_id not in products:
            print("Product not found.")
            continue
        quantity = int(input("Enter Quantity: "))
        if quantity > products[product_id]["quantity"]:
            print("Insufficient stock.")
            continue
        order_items.append((product_id, quantity))
        products[product_id]["quantity"] -= quantity
    orders[order_id] = {
        "customer_id": customer_id,
        "date": order_date,
        "items": order_items
    }
    print(f"Order placed successfully! Order ID: {order_id}")

def view_orders():
    """Displays all orders."""
    if not orders:
        print("No orders available.")
        return
    print("-" * 40)
    print("Order ID | Customer ID | Order Date | Items")
    print("-" * 40)
    for order_id, order_details in orders.items():
        print(f"{order_id}        | {order_details['customer_id']} | {order_details['date']} | {order_details['items']}")
    print("-" * 40)

def calculate_order_total(order_id):
    """Calculates the total amount for a given order."""
    if order_id not in orders:
        print("Order not found.")
        return
    total_amount = 0
    for product_id, quantity in orders[order_id]["items"]:
        total_amount += products[product_id]["price"] * quantity
    return total_amount

def generate_invoice(order_id):
    """Generates an invoice for a given order."""
    if order_id not in orders:
        print("Order not found.")
        return
    total_amount = calculate_order_total(order_id)
    customer_name = customers[orders[order_id]["customer_id"]]["name"]
    print("-" * 40)
    print("INVOICE")
    print("-" * 40)
    print(f"Order ID: {order_id}")
    print(f"Customer Name: {customer_name}")
    print(f"Order Date: {orders[order_id]['date']}")
    print("-" * 40)
    print("Product ID | Product Name | Quantity | Price | Total")
    print("-" * 40)
    for product_id, quantity in orders[order_id]["items"]:
        product_name = products[product_id]["name"]
        price = products[product_id]["price"]
        total_item_price = price * quantity
        print(f"{product_id}        | {product_name}          | {quantity}      | {price}   | {total_item_price}")
    print("-" * 40)
    print(f"Total Amount: {total_amount}")
    print("-" * 40)

# --- Load Data ---

def load_data():
    """Loads data from files if they exist."""
    try:
        with open("products.dat", "rb") as f:
            global products
            products = pickle.load(f)
    except FileNotFoundError:
        pass
    try:
        with open("customers.dat", "rb") as f:
            global customers
            customers = pickle.load(f)
    except FileNotFoundError:
        pass
    try:
        with open("employees.dat", "rb") as f:
            global employees
            employees = pickle.load(f)
    except FileNotFoundError:
        pass
    try:
        with open("orders.dat", "rb") as f:
            global orders
            orders = pickle.load(f)
    except FileNotFoundError:
        pass

# --- Save Data ---

def save_data():
    """Saves data to files."""
    with open("products.dat", "wb") as f:
        pickle.dump(products, f)
    with open("customers.dat", "wb") as f:
        pickle.dump(customers, f)
    with open("employees.dat", "wb") as f:
        pickle.dump(employees, f)
    with open("orders.dat", "wb") as f:
        pickle.dump(orders, f)

# --- Main Menu ---

def main():
    """Main function to run the ERP program."""
    load_data()
    while True:
        print("\nERP System Menu:")
        print("1. Products")
        print("2. Customers")
        print("3. Employees")
        print("4. Orders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nProduct Management:")
            print("1. Add Product")
            print("2. View Products")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back to Main Menu")
            product_choice = input("Enter your choice: ")
            if product_choice == '1':
                add_product()
            elif product_choice == '2':
                view_products()
            elif product_choice == '3':
                update_product()
            elif product_choice == '4':
                delete_product()
            elif product_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '2':
            print("\nCustomer Management:")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back to Main Menu")
            customer_choice = input("Enter your choice: ")
            if customer_choice == '1':
                add_customer()
            elif customer_choice == '2':
                view_customers()
            elif customer_choice == '3':
                update_customer()
            elif customer_choice == '4':
                delete_customer()
            elif customer_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '3':
            print("\nEmployee Management:")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Back to Main Menu")
            employee_choice = input("Enter your choice: ")
            if employee_choice == '1':
                add_employee()
            elif employee_choice == '2':
                view_employees()
            elif employee_choice == '3':
                update_employee()
            elif employee_choice == '4':
                delete_employee()
            elif employee_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '4':
            print("\nOrder Management:")
            print("1. Place Order")
            print("2. View Orders")
            print("3. Generate Invoice")
            print("4. Back to Main Menu")
            order_choice = input("Enter your choice: ")
            if order_choice == '1':
                place_order()
            elif order_choice == '2':
                view_orders()
            elif order_choice == '3':
                order_id = input("Enter Order ID to generate invoice: ")
                generate_invoice(order_id)
            elif order_choice == '4':
                continue
            else:
                print("Invalid choice.")
        elif choice == '5':
            save_data()
            print("Exiting ERP System...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()