from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription

MSG_WRONG_INPUT = "Wrong input. Try again!"
class Menu:
    """Represents the menu class for the project

    Attributes: 
        stock: stock variable
        profiles: user management module
        pharmacist: account of the salesperson
        records_file: path to the file containing the sales
        prescriptions_file: path to the file containing the prescriptions.
        stock_file: path to the file containing the stock data
    """
    def __init__(self, stock: Stock, profiles: UserManagement, pharmacist: User, records_file: str, prescriptions_file: str, stock_file: str) -> None:
        self.stock = stock
        self.profiles = profiles
        self.pharmacist = pharmacist
        self.cart = Cart(stock = stock)
        # use the file instead of the object so that we can keep track
        self.records_file = records_file
        #self.wrapper = wrapper   #Store the wrapper instance
        self.prescriptions_file = prescriptions_file
        self.stock_file = stock_file

    #TODO: Create all the necessary functions/method to create and manage the menu using the
    # available variables and all the attributes of the class

    # Make sure to dump the prescriptions, stock, and sale data after every sale.

    # Your menu should have two main options with suboptions. Such as
    """
    1. Order management
        1.1. Adding to a cart (you need to show the list of products and ask the user to select one with ID. Bonus: Can you display with numbers and ask user to choose a number instead?
                Also ask for quantity.)
        1.2. Remove from a cart (display the cart and ask the user to select the element to remove. Remove by ID or by index (bonus))
        1.3. Clear the cart (self explanatory)
        1.4. Checkout (displays the cart with the total and ask for a prescription element. Proceed to checkout and show a message is successful or not).
    2. Analytics
        2.1. Total income from purchases
        2.2. Prescription statistics
        2.3. Purchases for a user
        2.4. Sales by an agent
        2.5. Top sales

    * For each of the menu items, when necessary, display a success or error message to guide the user.
    """

    # **CHALLENGE** (BONUS): Can you implement the menu to work as a USSD application? Implement and show your design
    def display_main_menu(self):
        """Displays the main menu options"""
        while True:
            print("Main Menu:")
            print("1. Order management")
            print("2. Analytics")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.order_management_menu()
            elif choice == "2":
                self.analytics_menu()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print(MSG_WRONG_INPUT)

    def order_management_menu(self):
        """Displays the order management menu options"""
        while True:
            print("Order Management Menu:")
            print("1. Adding to a cart")
            print("2. Remove from a cart")
            print("3. Clear the cart")
            print("4. Checkout")
            print("0. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_to_cart()
            elif choice == "2":
                self.remove_from_cart()
            elif choice == "3":
                self.cart.clear()
                print("Cart cleared.")
            elif choice == "4":
                self.checkout_menu()
            elif choice == "0":
                break
            else:
                print(MSG_WRONG_INPUT)

    def add_to_cart(self):
        """Allows user to add products to the cart"""
        print("Products in stock:")
        for product in self.stock.products:
            print(f"{product.code}: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

        product_code = input("Enter the product code to add to cart: ")
        quantity = int(input("Enter the quantity to add: "))

        try:
            self.cart.add(product_code, quantity)
            print(f"{quantity} units of product {product_code} added to cart.")
        except ValueError as e:
            print(e)

    def remove_from_cart(self):
        """Allows user to remove products from the cart"""
        print("Products in cart:")
        print(self.cart)

        product_code = input("Enter the product code to remove from cart: ")

        try:
            self.cart.remove(product_code)
            print(f"Product {product_code} removed from cart.")
        except ValueError as e:
            print(e)

    def checkout_menu(self):
        """Displays the checkout menu options"""
        print("Checkout Menu:")
        customer_id = input("Enter customer ID: ")
        prescription_id = input("Enter prescription ID (if available): ")

        try:
            prescription = Prescription.get(self.prescriptions_file, prescription_id) if prescription_id else None
            self.wrapper.checkout(self.cart, customer_id, prescription)
            self.cart.clear()
            self.wrapper.dump(self.records_file)
            print("Checkout successful.")
        except Exception as e:
            print(e)

    def analytics_menu(self):
        """Displays the analytics menu options"""
        while True:
            print("Analytics Menu:")
            print("1. Total income from purchases")
            print("2. Prescription statistics")
            print("3. Purchases for a user")
            print("4. Sales by an agent")
            print("5. Top sales")
            print("0. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.total_income()
            elif choice == "2":
                self.prescription_stats()
            elif choice == "3":
                self.user_purchases()
            elif choice == "4":
                self.agent_sales()
            elif choice == "5":
                self.top_sales()
            elif choice == "0":
                break
            else:
                print(MSG_WRONG_INPUT)

    def total_income(self):
        """Displays the total income from purchases"""
        total_income = self.wrapper.total_transactions()
        print(f"Total income from purchases: {total_income}")

    def prescription_stats(self):
        """Displays prescription statistics"""
        prescription_report = BookRecords(self.sales).report_on_prescriptions()
        print("Prescription statistics:")
        print(prescription_report)

    def user_purchases(self):
        """Displays purchases for a user"""
        user_id = input("Enter customer ID: ")
        purchases = BookRecords(self.sales).purchases_by_user(user_id)
        print("Purchases for user:")
        print(purchases)

    def agent_sales(self):
        """Displays sales by an agent"""
        agent_id = input("Enter agent ID: ")
        agent_sales = BookRecords(self.sales).sales_by_agent(agent_id)
        print("Sales by agent:")
        print(agent_sales)

    def top_sales(self):
        """Displays top sales"""
        n = int(input("Enter the number of top sales to display: "))
        top_sales_report = BookRecords(self.sales).top_n_sales(n=n)
        print("Top sales:")
        print(top_sales_report)

    def run(self):
        """Runs the interactive menu"""
        print("Welcome to the E-Pharmacy System!")
        self.display_main_menu()

