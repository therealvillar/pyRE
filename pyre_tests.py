import unittest
from unittest.mock import patch
from pyre import TransferTax, REAddress

class TestTransferTax(unittest.TestCase):
    
    def test_get_transfer_tax_rate(self):
        # Test if the method returns the correct transfer tax rate for a county
        self.assertEqual(TransferTax.get_transfer_tax_rate('Philadelphia'), 4.27)
        
        # Test if the method returns the correct transfer tax rate for a state
        self.assertEqual(TransferTax.get_transfer_tax_rate('Pennsylvania'), 1)
        
        # Test if the method returns 0 for an unknown location
        self.assertEqual(TransferTax.get_transfer_tax_rate('Unknown'), 0)
        
    def test_get_split_transfer_tax_rate(self):
        # Test if the method returns half of the transfer tax rate for a county
        self.assertEqual(TransferTax.get_split_transfer_tax_rate('Philadelphia'), 2.135)
        
        # Test if the method returns half of the transfer tax rate for a state
        self.assertEqual(TransferTax.get_split_transfer_tax_rate('Pennsylvania'), 0.5)
        
class TestREAddress(unittest.TestCase):
    
    def test_get_transfer_tax_rate(self):
        # Test if the method returns the correct transfer tax rate for a county
        address1 = REAddress('123 Main St', 'Philadelphia', 'PA', '19147')
        self.assertEqual(address1.get_transfer_tax_rate(), 4.27)
        
        # Test if the method returns the correct transfer tax rate for a state
        address2 = REAddress('456 Main St', 'Pittsburgh', 'PA', '15213')
        self.assertEqual(address2.get_transfer_tax_rate(), 1)
        
    def test_get_split_transfer_tax_rate(self):
        # Test if the method returns half of the transfer tax rate for a county
        address1 = REAddress('123 Main St', 'Philadelphia', 'PA', '19147')
        self.assertEqual(address1.get_split_transfer_tax_rate(), 2.135)
        
        # Test if the method returns half of the transfer tax rate for a state
        address2 = REAddress('456 Main St', 'Pittsburgh', 'PA', '15213')
        self.assertEqual(address2.get_split_transfer_tax_rate(), 0.5)

if __name__ == '__main__':
    unittest.main()