import json

from typing import List, Dict, Union
from .product import Product


class Prescription:
    """Represents a prescription object

    Attributes:
        DoctorName: the name of the doctor who gave the prescription
        PrescriptionID: ID of the prescription
        Medications: list of the medications, this is the quantity, the ID, the name, and whether it was processed or not
        # see format in prescriptions.json
        CustomerID: ID of the customer
    """
    def __init__(self, DoctorName: str, PrescriptionID: str, Medications: List[Dict[str, Union[int, str, bool]]],
                 CustomerID: str, Date: str) -> None:
        self.DoctorName = DoctorName
        self.PrescriptionID = PrescriptionID
        self.Medications = Medications
        self.CustomerID = CustomerID

    def medecineInPrescription(self, product: Product, quantity: int) -> bool:
        """Verifies if a medecine with the specified quantity is included in a prescription

        Args:
            product: the product to verify
            quantity: the quantity to be added

        Returns: A boolean denoting whether the value was found
        """
        #TODO: Implement the function
        # 
        for medication in self.Medications:
            if medication["ID"]==product.code and medication["Quantity"]>=quantity and not medication["ProcessedStatus"]:
                return True
        return False
        
        
    def markComplete(self, product: Product):
        """Mark a product's sale complete in the prescriptions file

        Args:
            product: the product sold

        Returns: None
        """
        #TODO: Change the value "ProcessedStatus" of the relevant product to True

        for medication in self.Medications:
            if medication["ID"] == product.code and not medication["ProcessedStatus"]:
                medication["ProcessedStatus"] = True
                break

    def dump(self, outfile: str):
        """Dumps the updated prescription to the specified file
        
        Args: 
            outfile: path to the file where the output should be written

        Returns: None
        """
       
        try:
            with open(outfile, 'r') as f:
                prescriptions_data = json.load(f)
            
            #TODO: Update the prescription that is being edited in the loaded data

            for prescription_data in prescriptions_data:
                if prescription_data["PrescriptionID"] == self.PrescriptionID:
                    prescription_data["Medications"] = self.Medications
                    break
            #TODO: Save the updated object
            #TODO: Read the output file (safely). 
            with open(outfile, 'w') as f:
                json.dump(prescriptions_data, f, indent=4)
        except FileNotFoundError:
            pass
    
    @classmethod
    def get(cls, infile: str, id: str):
        """Retrieves a specific prescription from a file
        
        Args:
            infile: path to the input file
            id: identifier of the prescription to add

        Returns: A prescription object as a dictionary
        """
        #TODO: Load the file and find the object with the relevant ID
        #TODO: Return the relevant prescription
        try:
            with open(infile, 'r') as f:
                prescriptions_data = json.load(f)
                for prescription_data in prescriptions_data:
                    if prescription_data["PrescriptionID"] == id:
                        return cls(**prescription_data)
        except FileNotFoundError:
            pass
