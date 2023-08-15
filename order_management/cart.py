from .product import Product
from .stock import Stock

class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock

    def add(self, productCode: str, quantity: int):
        """Adds a product to the cart with the specified quantity
        
        Args:
            productCode: the identifier of the product
            quantity: quantity to add

        Returns: None
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        product = self.stock.getProductByID(productCode)
        
        if quantity > product.quantity:
            raise ValueError("Not enough stock available.")
        
        if productCode in self.products:
            self.products[productCode] += quantity
        else:
            self.products[productCode] = quantity

    def __str__(self) -> str:
        """String representation of the cart"""
        output = ["Cart:"]
        total_cost = 0
        for product_code, quantity in self.products.items():
            product = self.stock.getProductByID(product_code)
            product_total_cost = product.price * quantity
            output.append(f"{product.name} ({quantity} units) - Price per unit: ${product.price:.2f} - Total cost: ${product_total_cost:.2f}")
            total_cost += product_total_cost
        output.append(f"Total cost of the cart: ${total_cost:.2f}")
        return "\n".join(output)

    def remove(self, code):
        """Removes a specific product from the cart"""
        if code in self.products:
            del self.products[code]
        else:
            print("Product not found in the cart.")

    def clear(self):
        """Clears up the cart."""
        self.products = {}

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        total_cost = 0
        for product_code, quantity in self.products.items():
            product = self.stock.getProductByID(product_code)
            total_cost += product.price * quantity
        return total_cost
