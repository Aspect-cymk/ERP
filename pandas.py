#CUSTOMERS MODULE
def customers():
    """Main function for customer management."""
    while True:
        print("\nCustomer Management System:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
def add_customer():
    """Adds a new customer record to the binary file."""
    try:
        with open("customers.dat", "ab") as file:
            customer = {}
            customer["customer_id"] = input("Enter Customer ID: ")
            customer["name"] = input("Enter Customer Name: ")
            customer["email"] = input("Enter Customer Email: ")
            customer["phone"] = input("Enter Customer Phone: ")
            pickle.dump(customer, file)
            print("Customer added successfully!")
    except Exception as e:
        print(f"Error adding customer: {e}")
    def view_customers():
        """Displays all customer records from the binary file."""
        try:
            with open("customers.dat", "rb") as file:
                print("Customer Records:")
                print("-" * 50)
                print(f"{'Customer ID':<15} {'Name':<20} {'Email':<30} {'Phone':<15}")
                print("-" * 50)
                while True:
                    try:
                        customer = pickle.load(file)
                        print(f"{customer['customer_id']:<15} {customer['name']:<20} {customer['email']:<30} {customer['phone']:<15}")
                    except EOFError:
                        break
                print("-" * 50)
        except Exception as e:
            print(f"Error viewing customers: {e}")
def update_customer():
    """Updates an existing customer record in the binary file."""
    try:
        with open("customers.dat", "rb+") as file:
            customer_id_to_update = input("Enter the Customer ID to update: ")
            found = False
            while True:
                try:
                    customer = pickle.load(file)
                    if customer["customer_id"] == customer_id_to_update:
                        print("Customer Found:")
                        print(f"{'Customer ID':<15} {'Name':<20} {'Email':<30} {'Phone':<15}")
                        print(f"{customer['customer_id']:<15} {customer['name']:<20} {customer['email']:<30} {customer['phone']:<15}")
                        print("-" * 50)
                        customer["name"] = input("Enter New Name (or press Enter to keep current): ") or customer["name"]
                        customer["email"] = input("Enter New Email (or press Enter to keep current): ") or customer["email"]
                        customer["phone"] = input("Enter New Phone (or press Enter to keep current): ") or customer["phone"]
                        file.seek(-pickle.dumps(customer).__len__(), 1)
                        pickle.dump(customer, file)
                        found = True
                        print("Customer updated successfully!")
                        break
                except EOFError:
                    break
        if not found:
            print(f"Customer with ID '{customer_id_to_update}' not found.")
    except Exception as e:
        print(f"Error updating customer: {e}")
def delete_customer():
    """Deletes a customer record from the binary file."""
    try:
        with open("customers.dat", "rb+") as file:
            customer_id_to_delete = input("Enter the Customer ID to delete: ")
            temp_file = "temp.dat"
            found = False
            while True:
                try:
                    customer = pickle.load(file)
                    if customer["customer_id"] != customer_id_to_delete:
                        with open(temp_file, "ab") as temp:
                            pickle.dump(customer, temp)
                    else:
                        found = True
                except EOFError:
                    break
        if found:
            print("Customer deleted successfully!")
            with open(temp_file, "rb") as temp:
                with open("customers.dat", "wb") as file:
                    while True:
                        try:
                            customer = pickle.load(temp)
                            pickle.dump(customer, file)
                        except EOFError:
                            break
        else:
            print(f"Customer with ID '{customer_id_to_delete}' not found.")
        if found:
            os.remove(temp_file)
    except Exception as e:
        print(f"Error deleting customer: {e}")
customers()