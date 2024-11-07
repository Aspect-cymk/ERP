import pickle
import random
import os


# EXCHANGE RATES MODULE
def exc(): 

    print(""" /n𝕮𝖚𝖗𝖗𝖊𝖓𝖙 𝕰𝖝𝖈𝖍𝖆𝖓𝖌𝖊 𝕽𝖆𝖙𝖊𝖘

                1. 1$(USD) = 82.90 ₹(INR)
                2. 1€ (EURO)= 89.63 ₹(INR)
                3. 1¥(YEN) = 0.55 ₹(INR)
                4. 1$(CAD) = 61.40 ₹(INR)""")

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

#EMPLOYEES MODULE

def employee():
    def add_employee():
        """Adds an employee record to the binary file."""
        try:
            with open("employees.dat", "ab") as file:
                employee = {}
                employee["emp_id"] = input("Enter Employee ID: ")
                employee["name"] = input("Enter Employee Name: ")
                employee["department"] = input("Enter Department: ")
                employee["salary"] = float(input("Enter Salary: "))
                pickle.dump(employee, file)
            print("Employee added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")
    def view_employees():
        """Displays all employee records from the binary file."""
        try:
            with open("employees.dat", "rb") as file:
                print("Employee Records:")
                print("-" * 40)
                print(f"{'Emp ID':<10} {'Name':<20} {'Department':<15} {'Salary':<10}")
                print("-" * 40)
                while True:
                    try:
                        employee = pickle.load(file)
                        print(f"{employee['emp_id']:<10} {employee['name']:<20} {employee['department']:<15} {employee['salary']:<10}")
                    except EOFError:
                        break
                print("-" * 40)
        except Exception as e:
            print(f"Error viewing employees: {e}")
    def update_employee():
        """Updates an existing employee record in the binary file."""
        try:
            with open("employees.dat", "rb+") as file:
                emp_id_to_update = input("Enter the Employee ID to update: ")
                found = False
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee["emp_id"] == emp_id_to_update:
                            print("Employee Found:")
                            print(f"{'Emp ID':<10} {'Name':<20} {'Department':<15} {'Salary':<10}")
                            print(f"{employee['emp_id']:<10} {employee['name']:<20} {employee['department']:<15} {employee['salary']:<10}")
                            print("-" * 40)
                            employee["name"] = input("Enter New Name (or press Enter to keep current): ") or employee["name"]
                            employee["department"] = input("Enter New Department (or press Enter to keep current): ") or employee["department"]
                            employee["salary"] = float(input("Enter New Salary (or press Enter to keep current): ")) or employee["salary"]
                            file.seek(-pickle.dumps(employee).__len__(), 1)
                            pickle.dump(employee, file)
                            found = True
                            print("Employee updated successfully!")
                            break
                    except EOFError:
                        break
                if not found:
                    print(f"Employee with ID '{emp_id_to_update}' not found.")
        except Exception as e:
                print(f"Error updating employee: {e}")
    def delete_employee():
        """Deletes an employee record from the binary file."""
        try:
            with open("employees.dat", "rb+") as file:
                emp_id_to_delete = input("Enter the Employee ID to delete: ")
                temp_file = "temp.dat"
                found = False
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee["emp_id"] != emp_id_to_delete:
                            with open(temp_file, "ab") as temp:
                                pickle.dump(employee, temp)
                        else:
                            found = True
                    except EOFError:
                        break
                if found:
                    print("Employee deleted successfully!")
                    with open(temp_file, "rb") as temp:
                        with open("employees.dat", "wb") as file:
                            while True:
                                try:
                                    employee = pickle.load(temp)
                                    pickle.dump(employee, file)
                                except EOFError:
                                    break
                else:
                    print(f"Employee with ID '{emp_id_to_delete}' not found.")
                if found:
                    os.remove(temp_file)
        except Exception as e:
            print(f"Error deleting employee: {e}")

        """Main function to drive the menu."""
        while True:
            print("\nEmployee Management System:")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_employee()
            elif choice == '2':
                view_employees()
            elif choice == '3':
                update_employee()
            elif choice == '4':
                delete_employee()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

#ORDER MODULE
def orders():
    """Main function for order management."""
    while True:
        print("\nOrder Management System:")
        print("1. Create Order")
        print("2. View Orders")
        print("3. Cancel Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            cancel_order()
        elif choice == '4':
            break
        else:
            
            rint("Invalid choice. Please try again.")

def create_order():
    """Creates a new order record in the binary file."""
    try:
        with open("orders.dat", "ab") as file:
            order = {}
            order["order_id"] = input("Enter Order ID: ")
            order["customer_id"] = input("Enter Customer ID: ")
            order["items"] = []
            while True:
                item_name = input("Enter item name (or press Enter to finish adding items): ")
                if not item_name:
                    break
                item_quantity = int(input("Enter item quantity: "))
                order["items"].append({"name": item_name, "quantity": item_quantity})
            order["status"] = "Pending"
            pickle.dump(order, file)
        print("Order created successfully!")
    except Exception as e:
        print(f"Error creating order: {e}")

def view_orders():
    """Displays all order records from the binary file."""
    try:
        with open("orders.dat", "rb") as file:
            print("Order Records:")
            print("-" * 50)
            print(f"{'Order ID':<10} {'Customer ID':<15} {'Items':<30} {'Status':<10}")
            print("-" * 50)
            while True:
                try:
                    order = pickle.load(file)
                    items_str = ", ".join([f"{item['name']} ({item['quantity']})" for item in order["items"]])
                    print(f"{order['order_id']:<10} {order['customer_id']:<15} {items_str:<30} {order['status']:<10}")
                except EOFError:
                    break
            print("-" * 50)
    except Exception as e:
        print(f"Error viewing orders: {e}")

def cancel_order():
    """Cancels an existing order in the binary file."""
    try:
        with open("orders.dat", "rb+") as file:
            order_id_to_cancel = input("Enter the Order ID to cancel: ")
            temp_file = "temp.dat"
            found = False
            while True:
                try:
                    order = pickle.load(file)
                    if order["order_id"] == order_id_to_cancel:
                        order["status"] = "Cancelled"
                        file.seek(-pickle.dumps(order).__len__(), 1)
                        pickle.dump(order, file)
                        found = True
                        print("Order cancelled successfully!")
                        break
                    else:
                        with open(temp_file, "ab") as temp:
                            pickle.dump(order, temp)
                except EOFError:
                    break
            if not found:
                print(f"Order with ID '{order_id_to_cancel}' not found.")
            if found:
                with open(temp_file, "rb") as temp:
                    with open("orders.dat", "wb") as file:
                        while True:
                            try:
                                order = pickle.load(temp)
                                pickle.dump(order, file)
                            except EOFError:
                                break
                os.remove(temp_file)
    except Exception as e:
        print(f"Error cancelling order: {e}")


def sgn(): # SIGN UP MODULE
  stu = {}
  ans = "y"
  file = open("py.dat", "wb")
  while ans == "y":
    
    usr = input (" Enter your username :")
    pss = input (" Enter a string password :")
    pss2 = input (" Enter your password again :")
    fcs = random.getrandbits(16)
    stu["username"] = usr
    stu["password"] = pss
    stu["Branch ID"] = fcs
    if pss == pss2:
      print(" You have successfully signed up! ")
      print(" Your branch ID is : ", fcs, "NOTE: PLEASE KEEP IT SAFE!", end = "\n")
      pickle.dump(stu, file)
      ans = input("Do you want to enter more records(y/n) :")
    else:
            print("Make sure the password is correct!")
    
    file.close()

def lgn(): # LOGIN MODULE
    file = open("py.dat", "rb")
    login = input(" Enter your username: ")
    password = input(" Enter your password: ")
    try:
        while True:
          stu = pickle.load(file)
          if stu["username"] == login and stu["password"] == password:
            print("Login successful")
            found = True
            while True:
      
              print(" \nBRANCHES OF YOUR COMPANY ")
              print(" 1. HPL(PVT.LTD) BANGALORE, HSR ")
              choice = int(input(" Enter your Branch: "))
              ID = int(input(" Enter your  Branch ID: "))
      
              if ID == fcs:
        
                if choice == 1:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, HSR ")                           
          
                    ans = "y"
                    while ans == "y":
                        print("""   
   _______  ___     ___  ___  ____  __________  ________  _____  ____  ___
  / __/ _ \/ _ \   / _ \/ _ \/ __ \/_  __/ __ \/_  __/\ \/ / _ \/ __/ <  /
 / _// , _/ ___/  / ___/ , _/ /_/ / / / / /_/ / / /    \  / ___/ _/   / / 
/___/_/|_/_/     /_/  /_/|_|\____/ /_/  \____/ /_/     /_/_/  /___/  /_/  
            __  ______   _____  __   __  ________  ____  __               
           /  |/  / _ | /  _/ |/ /  /  |/  / __/ |/ / / / /               
          / /|_/ / __ |_/ //    /  / /|_/ / _//    / /_/ /                
         /_/  /_/_/ |_/___/_/|_/  /_/  /_/___/_/|_/\____/                 
                                                                         """)
                        print("1. EXCHANGE RATES MODULE")
                        print("4. CUSTOMERS MODULE")
                        print("5. EMPLOYEES MODULE")
                        print("6. ORDER MODULE")
                        print("7. Exit")
                        choice = input("Enter your choice: ")
                        if choice == '1':
                            exc()
                        elif choice == '4':
                            customers()
                        elif choice == '5':
                            employee()
                        elif choice == '6':
                            orders()
                        elif choice == '7':
                            break
                        else:
                            print("Invalid choice. Please try again.") 

                        ans = input("Do you want to continue? (y/n) ")

          else:
            print(" Wrong Branch ID entered ")

    except:
        if found == False:
            print("Wrong credentials entered! Try again.")
    file.close()
while True:
    print ("\nMENU")
    print ("""1. sign up. """)
    print ("""2. login. """)
    print("5. EXIT")
    choice = int (input ("Enter your desired choice : "))

    if choice == 1:
        sgn()

    elif choice == 2:
        lgn()
  
    elif choice == 5:
        print ("See you nxt time!")
        break

    else:
        print("Incorrect choice!!!")

#=================================================================== MODULES =================================================================================================#

# BHUVESH GETS INTO A KALESH WITH MUKESH
.






























