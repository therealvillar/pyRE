'''
    STATUS : IN PROGRESS
    TO DO : KEEP CLEANING UP OLD 
'''

import heapq

def first_gt_index(lst, k):
    '''
        returns the 1st element of the list greater than k
    '''
    # create a heap from the list
    heapq.heapify(lst)
    # find index of first element greater than k
    for i, val in enumerate(lst):
        if val > k:
            return i
    return None


class TransferTax:
    """
    DEFINE TRANSFER TAX RATES CURRENTLY ONLY PA DEFINED
    """
    TRANSFER_TAX_STATE = {'Pennsylvania' : 1, 'PA' : 1}
    TRANSFER_TAX_COUNTY = {'Philadelphia' : 3.27 + TRANSFER_TAX_STATE['Pennsylvania'],
                           'Montgomery' : 1 + TRANSFER_TAX_STATE['Pennsylvania'],
                           'Delco' : 1 + TRANSFER_TAX_STATE['Pennsylvania']}

    @classmethod
    def get_transfer_tax_rate(cls, location):
        """
        RETURNS TRANSFER TAX
        """
        #   MATCHES location to county/city
        if location in cls.TRANSFER_TAX_COUNTY:
            return cls.TRANSFER_TAX_COUNTY.get(location, 0)
        #   MATCHES location to state
        if location in cls.TRANSFER_TAX_STATE:
            print(\
                "NOTICE: '" + str(location) +
                "' NOT IDENTIFIED IN TRANSFER_TAX_COUNTY\n\
                    -> RETURNS STATE_TT * 2.\n\
                        CHECK DICTIONARY TransferTax"\
                            )
            return cls.TRANSFER_TAX_STATE.get(location, 0)
        #   NO MATCHES
        print(\
                "NOTICE: '" + str(location) +\
                    "' NOT IDENTIFIED IN TRANSFER_TAX_STATE or TRANSFER_TAX_COUNTY\n\
                        -> RETURNS 0.\n\
                            CHECK DICTIONARY TransferTax"\
                                )
        return 0

    @classmethod
    def get_split_transfer_tax_rate(cls, location):
        """
        RETURNS HALF OF TRANSFER TAX RATE
        """
        return cls.get_transfer_tax_rate(location) / 2


#   WORKING
class REAddress:
    """
    A class representing a real estate property's address
    """
    def __init__(self, st_add, city, state, zip_code):
        self.st_add = st_add
        self.city = city
        self.state = state
        self.zip_code = zip_code
        
    def get_transfer_tax_rate(self):
        """
        Returns the transfer tax rate for the address location
        """
        # Lookup the transfer tax rate based on the city/county or state
        if self.city in TransferTax.TRANSFER_TAX_COUNTY:
            return TransferTax.get_transfer_tax_rate(self.city)
        else:
            return TransferTax.get_transfer_tax_rate(self.state)
    
    def get_split_transfer_tax_rate(self):
        """
        Returns half of the transfer tax rate for the address location
        """
        return self.get_transfer_tax_rate() * 0.5
