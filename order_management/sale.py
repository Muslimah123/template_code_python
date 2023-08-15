class Sale:
    """Class representing a sale that was successfully committed to the records.

    Attributes:
        id: unique identifier of the product sold (string)
        name: name of the product sold
        quantity: the quantity sold during the sale
        price: unit price of the product
        purchase_price: the total price at which the product was sold
        timestamp: the UNIX timestamp of the sale
        customerID: username of the buying customer (string)
        salesperson: username of the pharmacist making the sale (string)
        prescriptionID: identifier of the prescription used in the sale
    """
    def __init__(self, id: str, name: str, quantity: int, 
                 price: float, purchase_price: float, timestamp: float, 
                 customerID: str, salesperson: str, prescriptionID: str) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.purchase_price = purchase_price
        self.timestamp = timestamp
        self.customerID = customerID
        self.salesperson = salesperson
        self.prescriptionID = prescriptionID

    def __str__(self) -> str:
        """Returns a string representation of a Sale object."""
        total_cost = self.purchase_price * self.quantity
        return (
            f"Sale ID: {self.id}\n"
            f"Product Name: {self.name}\n"
            f"Unit Price: ${self.price:.2f}\n"
            f"Quantity Sold: {self.quantity}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Total Cost: ${total_cost:.2f}\n"
            f"Customer ID: {self.customerID}\n"
            f"Salesperson: {self.salesperson}\n"
            f"Prescription ID: {self.prescriptionID}"
        )
