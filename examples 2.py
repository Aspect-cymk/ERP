import pickle
import random
# Constants
BRANCH_ID = random.getrandbits(16)  # Generate a unique branch ID
# Data Storage (using dictionaries for simplicity)
employees = {}  # {empid: {'name': str, 'salary': float, 'department': str}}
customers = {}  # {custid: {'name': str, 'email': str, 'phone': str, 'address': str}}
products = {}  # {productid: {'name': str, 'price': float, 'quantity': int}}
orders = []  # [{'orderid': int, 'customerid': int, 'productid': int, 'quantity': int}]
# Functions
def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")
def display_menu():
    """Displays the main menu."""
    clear_screen()
    print("----- ERP System -----")
    print("1. Employee Management")
    print("2. Customer Management")
    print("3. Product Management")
    print("4. Order Management")
    print("5. Reports")
    print("6. Exit")
def load_data():
    """Loads data from pickle files (if they exist)."""
    global employees, customers, products, orders
    try:
        with open("employees.dat", "rb") as f:
            employees = pickle.load(f)
    except FileNotFoundError:
        print("Employee data file not found. Starting with an empty database.")
    try:
        with open("customers.dat", "rb") as f:
            customers = pickle.load(f)
    except FileNotFoundError:
        print("Customer data file not found. Starting with an empty database.")
    try:
        with open("products.dat", "rb") as f:
            products = pickle.load(f)
    except FileNotFoundError:
        print("Product data file not found. Starting with an empty database.")
    try:
        with open("orders.dat", "rb") as f:
            orders = pickle.load(f)
    except FileNotFoundError:
        print("Order data file not found. Starting with an empty database.")
def save_data():
    """Saves data to pickle files."""
    with open("employees.dat", "wb") as f:
        pickle.dump(employees, f)
    with open("customers.dat", "wb") as f:
        pickle.dump(customers, f)
    with open("products.dat", "wb") as f:
        pickle.dump(products, f)
    with open("orders.dat", "wb") as f:
        pickle.dump(orders, f)
# Employee Management
def add_employee():
    """Adds a new employee record."""
    empid = input("Enter Employee ID: ")
    if empid in employees:
        print("Employee ID already exists.")
        return
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    employees[empid] = {'name': name, 'salary': salary, 'department': department}
    print("Employee added successfully.")
def view_employees():
    """Displays all employee records."""
    if not employees:
        print("No employees in the database.")
        return
    print("----- Employees -----")
    for empid, details in employees.items():
        print(f"Employee ID: {empid}, Name: {details['name']}, Salary: {details['salary']}, Department: {details['department']}")
def update_employee():
    """Updates an existing employee record."""
    empid = input("Enter Employee ID to update: ")
    if empid not in employees:
        print("Employee not found.")
        return
    print("1. Update Name")
    print("2. Update Salary")
    print("3. Update Department")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        employees[empid]['name'] = new_name
        print("Name updated successfully.")
    elif choice == '2':
        new_salary = float(input("Enter new salary: "))
        employees[empid]['salary'] = new_salary
        print("Salary updated successfully.")
    elif choice == '3':
        new_department = input("Enter new department: ")
        employees[empid]['department'] = new_department
        print("Department updated successfully.")
    else:
        print("Invalid choice.")
def delete_employee():
    """Deletes an employee record."""
    empid = input("Enter Employee ID to delete: ")
    if empid not in employees:
        print("Employee not found.")
        return
    del employees[empid]
    print("Employee deleted successfully.")
# Customer Management
def add_customer():
    """Adds a new customer record."""
    custid = input("Enter Customer ID: ")
    if custid in customers:
        print("Customer ID already exists.")
        return
    name = input("Enter Customer Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    customers[custid] = {'name': name, 'email': email, 'phone': phone, 'address': address}
    print("Customer added successfully.")
def view_customers():
    """Displays all customer records."""
    if not customers:
        print("No customers in the database.")
        return
    print("----- Customers -----")
    for custid, details in customers.items():
        print(f"Customer ID: {custid}, Name: {details['name']}, Email: {details['email']}, Phone: {details['phone']}, Address: {details['address']}")
def update_customer():
    """Updates an existing customer record."""
    custid = input("Enter Customer ID to update: ")
    if custid not in customers:
        print("Customer not found.")
        return
    print("1. Update Name")
    print("2. Update Email")
    print("3. Update Phone Number")
    print("4. Update Address")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        customers[custid]['name'] = new_name
        print("Name updated successfully.")
    elif choice == '2':
        new_email = input("Enter new email: ")
        customers[custid]['email'] = new_email
        print("Email updated successfully.")
    elif choice == '3':
        new_phone = input("Enter new phone number: ")
        customers[custid]['phone'] = new_phone
        print("Phone number updated successfully.")
    elif choice == '4':
        new_address = input("Enter new address: ")
        customers[custid]['address'] = new_address
        print("Address updated successfully.")
    else:
        print("Invalid choice.")
def delete_customer():
    """Deletes a customer record."""
    custid = input("Enter Customer ID to delete: ")
    if custid not in customers:
        print("Customer not found.")
        return
    del customers[custid]
    print("Customer deleted successfully.")
# Product Management
def add_product():
    """Adds a new product record."""
    productid = input("Enter Product ID: ")
    if productid in products:
        print("Product ID already exists.")
        return
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    products[productid] = {'name': name, 'price': price, 'quantity': quantity}
    print("Product added successfully.")
def view_products():
    """Displays all product records."""
    if not products:
        print("No products in the database.")
        return
    print("----- Products -----")
    for productid, details in products.items():
        print(f"Product ID: {productid}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")
def update_product():
    """Updates an existing product record."""
    productid = input("Enter Product ID to update: ")
    if productid not in products:
        print("Product not found.")
        return
    print("1. Update Name")
    print("2. Update Price")
    print("3. Update Quantity")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        products[productid]['name'] = new_name
        print("Name updated successfully.")
    elif choice == '2':
        new_price = float(input("Enter new price: "))
        products[productid]['price'] = new_price
        print("Price updated successfully.")
    elif choice == '3':
        new_quantity = int(input("Enter new quantity: "))
        products[productid]['quantity'] = new_quantity
        print("Quantity updated successfully.")
    else:
        print("Invalid choice.")
def delete_product():
    """Deletes a product record."""
    productid = input("Enter Product ID to delete: ")
    if productid not in products:
        print("Product not found.")
        return
    del products[productid]
    print("Product deleted successfully.")
# Order Management
def create_order():
    """Creates a new order."""
    orderid = len(orders) + 1  # Automatic order ID generation
    custid = input("Enter Customer ID: ")
    if custid not in customers:
        print("Customer not found.")
        return
    productid = input("Enter Product ID: ")
    if productid not in products:
        print("Product not found.")
        return
    quantity = int(input("Enter Quantity: "))
    if quantity > products[productid]['quantity']:
        print("Insufficient product quantity in stock.")
        return
    products[productid]['quantity'] -= quantity  # Update product quantity
    orders.append({'orderid': orderid, 'customerid': custid, 'productid': productid, 'quantity': quantity})
    print("Order created successfully.")
def view_orders():
    """Displays all order records."""
    if not orders:
        print("No orders in the database.")
        return
    print("----- Orders -----")
    for order in orders:
        customer_name = customers[order['customerid']]['name'] if order['customerid'] in customers else "Unknown"
        product_name = products[order['productid']]['name'] if order['productid'] in products else "Unknown"
        print(f"Order ID: {order['orderid']}, Customer: {customer_name}, Product: {product_name}, Quantity: {order['quantity']}")
def cancel_order():
    """Cancels an existing order."""
    orderid = int(input("Enter Order ID to cancel: "))
    for i, order in enumerate(orders):
        if order['orderid'] == orderid:
            productid = order['productid']
            quantity = order['quantity']
            products[productid]['quantity'] += quantity  # Restore product quantity
            del orders[i]
            print("Order cancelled successfully.")
            return
    print("Order not found.")
# Reports
def generate_employee_report():
    """Generates a report of all employees."""
    if not employees:
        print("No employees in the database.")
        return
    print("----- Employee Report -----")
    print(f"{'Employee ID':<15} {'Name':<20} {'Salary':<10} {'Department':<15}")
    for empid, details in employees.items():
        print(f"{empid:<15} {details['name']:<20} {details['salary']:<10} {details['department']:<15}")
def generate_customer_report():
    """Generates a report of all customers."""
    if not customers:
        print("No customers in the database.")
        return
    print("----- Customer Report -----")
    print(f"{'Customer ID':<15} {'Name':<20} {'Email':<30} {'Phone':<15} {'Address':<30}")
    for custid, details in customers.items():
        print(f"{custid:<15} {details['name']:<20} {details['email']:<30} {details['phone']:<15} {details['address']:<30}")
def generate_product_report():
    """Generates a report of all products."""
    if not products:
        print("No products in the database.")
        return
    print("----- Product Report -----")
    print(f"{'Product ID':<15} {'Name':<20} {'Price':<10} {'Quantity':<10}")
    for productid, details in products.items():
        print(f"{productid:<15} {details['name']:<20} {details['price']:<10} {details['quantity']:<10}")
def generate_order_report():
    """Generates a report of all orders."""
    if not orders:
        print("No orders in the database.")
        return
    print("----- Order Report -----")
    print(f"{'Order ID':<10} {'Customer ID':<15} {'Product ID':<15} {'Quantity':<10}")
    for order in orders:
        print(f"{order['orderid']:<10} {order['customerid']:<15} {order['productid']:<15} {order['quantity']:<10}")
# Main ERP Program
def main():
    """Main function to run the ERP program."""
    load_data()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            clear_screen()
            print("----- Employee Management -----")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Back to Main Menu")
            emp_choice = input("Enter your choice: ")
            if emp_choice == '1':
                add_employee()
            elif emp_choice == '2':
                view_employees()
            elif emp_choice == '3':
                update_employee()
            elif emp_choice == '4':
                delete_employee()
            elif emp_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '2':
            clear_screen()
            print("----- Customer Management -----")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back to Main Menu")
            cus_choice = input("Enter your choice: ")
            if cus_choice == '1':
                add_customer()
            elif cus_choice == '2':
                view_customers()
            elif cus_choice == '3':
                update_customer()
            elif cus_choice == '4':
                delete_customer()
            elif cus_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '3':
            clear_screen()
            print("----- Product Management -----")
            print("1. Add Product")
            print("2. View Products")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back to Main Menu")
            prod_choice = input("Enter your choice: ")
            if prod_choice == '1':
                add_product()
            elif prod_choice == '2':
                view_products()
            elif prod_choice == '3':
                update_product()
            elif prod_choice == '4':
                delete_product()
            elif prod_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '4':
            clear_screen()
            print("----- Order Management -----")
            print("1. Create Order")
            print("2. View Orders")
            print("3. Cancel Order")
            print("4. Back to Main Menu")
            order_choice = input("Enter your choice: ")
            if order_choice == '1':
                create_order()
            elif order_choice == '2':
                view_orders()
            elif order_choice == '3':
                cancel_order()
            elif order_choice == '4':
                continue
            else:
                print("Invalid choice.")
        elif choice == '5':
            clear_screen()
            print("----- Reports -----")
            print("1. Employee Report")
            print("2. Customer Report")
            print("3. Product Report")
            print("4. Order Report")
            print("5. Back to Main Menu")
            report_choice = input("Enter your choice: ")
            if report_choice == '1':
                generate_employee_report()
            elif report_choice == '2':
                generate_customer_report()
            elif report_choice == '3':
                generate_product_report()
            elif report_choice == '4':
                generate_order_report()
            elif report_choice == '5':
                continue
            else:
                print("Invalid choice.")
        elif choice == '6':
            save_data()
            print("Exiting ERP System...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()