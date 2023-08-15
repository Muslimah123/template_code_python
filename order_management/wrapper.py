from .cart import Cart
from .stock import Stock
from .product import Product
from .prescription import Prescription
from datetime import datetime

import json

## would need to create a new object for each new order
class Wrapper:
    """
    Main class used to manage orders and carts.

    Attributes:
        sales: A list of the sales done during the program's execution
        stock: The stock used in the execution
        agentID: the username of the pharmacist running the program
    """
    def __init__(self, stock: Stock, agentID: str) -> None:
        self.sales = []
        self.stock = stock
        self.agentID = agentID

    def checkout(self, cart: Cart, customerID: str, prescription: Prescription = None):
        """Handles the checkout procedure of the program.
        
        Args:
            cart: The cart to pay for
            prescription: the prescription that accompanies the order (default: None)
        """

        #TODO: First check that all the product that require a prescription have all the criteria met
        # (i.e., (1) there is a prescription that (2) matches the customer's ID, and (3) contains the medication
        # in the specified quantity).
        # Raise an exception if either of those conditions is unmet.
        for product_code, quantity in cart.products.items():
            product = self.stock.getProductByID(product_code)
            
            if prescription and product.requires_prescription:
                if not prescription.medicine_in_prescription(product, quantity) or prescription.CustomerID != customerID:
                    raise ValueError("Prescription criteria not met")

        #TODO: Get the current datetime and save a Sale information for each product sold with the following schema
        # {"name": "<name>", "quantity": <quantity>, "price": <unit price>, "purchase_price": <total price>, "timestamp": <timestamp>,
        # "customerID": <customer username>, "salesperson": <pharmacist username>}
        total_price = quantity * product.price
        sale = {
                "name": product.name,
                "quantity": quantity,
                "price": product.price,
                "purchase_price": total_price,
                "timestamp": datetime.now().timestamp(),
                "customerID": customerID,
                "salesperson": self.agentID
            }

        #TODO: Append the list to the current sales
        self.sales.append(sale)

        #TODO: Make sure that the sold products are marked as complete in the prescriptions.
        if prescription:
                prescription.mark_complete(product)

    def dump(self, outfile: str):
        """Dumps the current sales data to a file

        Args:
            outfile: the path to the output file
        """
        #TODO: Load the content, if any of the existing file
        try:
            with open(outfile, 'r') as f:
                sales_data = json.load(f)
        except FileNotFoundError:
            sales_data = []
        
        
        #TODO: Update the content by appending the new entries to it, and save to the file
        sales_data.extend(self.sales)
        
        with open(outfile, 'w') as f:
            json.dump(sales_data, f, indent=4)