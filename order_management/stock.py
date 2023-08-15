import json
from typing import List
from .product import Product

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, id: int, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be updated (+1 adds 1, -2 removes 2 for example)
        """
        product = self.getProductByID(id)
        new_quantity = product.quantity + change
        if new_quantity >= 0:
            product.quantity = new_quantity
        else:
            raise ValueError("Quantity cannot go below 0.")

    def getProductByID(self, id: int) -> Product:
        """Gets a product by its ID
        
        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        for product in self.products:
            if product.code == id:
                return product
        raise ValueError("Product not found.")

    def dump(self, outfile: str):
        """Saves the stock to a JSON file"""
        stock_data = [product.__dict__ for product in self.products]
        with open(outfile, 'w') as f:
            json.dump(stock_data, f, indent=4)

    @staticmethod
    def load(infile: str):
        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
        """
        with open(infile, 'r') as f:
            stock_data = json.load(f)
            products = [Product(**data) for data in stock_data]
            return Stock(products)

    def __str__(self) -> str:
        """Returns a string representation of the stock"""
        output = []
        for product in self.products:
            output.append(f"ID: {product.code}, Name: {product.name}, Brand: {product.brand}, Description: {product.description}, Quantity: {product.quantity}, Price: {product.price}, Requires Prescription: {'Yes' if product.requires_prescription else 'No'}")
        return "\n".join(output)
