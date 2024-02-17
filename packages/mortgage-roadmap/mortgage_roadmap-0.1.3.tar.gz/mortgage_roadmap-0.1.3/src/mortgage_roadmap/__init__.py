# -*- coding: utf-8 -*-
""" mortgage_calculator: 
    =============================

    Repository that calculate the mortgage roadmap of two types of mortgage calculators:
        - Mortgage_Constant_ChargeOff: Mortgage roadmap where you pay an constat chart off each month
        - Mortgage_Constant_Pay: Mortgage roadmap where you pay an constat fee each month

    How it work:
    -----------

    - import the classes::

        >>> from mortgage_roadmap import ( Mortgage_Constant_ChargeOff, Mortgage_Constant_Pay )
        >>>
        >>> a = Mortgage_Constant_ChargeOff(100000., 50, 4.8)
        >>> ...

    - import the module:: 

        >>> import mortgage_roadmap 
        >>>
        >>> a = mortgage_roadmap.Mortgage_Constant_ChargeOff(100000., 50, 4.8)
        >>> ...
    
    Content:
    --------

    - Mortgage_Constant_ChargeOff (class): Class that calculate an constant chargeoff Morgage:
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        - Methods:
            - Strict Class Methods:
                - getDecimals(cls): strict class method that return the defined number of decimals as output of the calculations
                - setDecimals(cls, value: int): strict class method that is used to set the number of decimals as output of the calculations
            - Create or Build Informs:
                - create_Dataframe(self): Create an dataframe with all the information related with the mortgage
                - create_XLS_File(self, path: str): method that create an excel file with the extension '.xls'
                - create_XLSX_File(self, path: str): method that create an excel file with the extension '.xlsx'
                - create_CSV_File(self, path: str): method that create an comma separated csv file with the extension '.csv'
            - Getters:
                - self.number_of_decimals: get the number of decimals for the outputs
                - self.initial_dept: Is the initial dept of the mortgage
                - self.quotas: Number of quotas of the Mortgage
                - self.APR: The interest that must be payed ofver an period of 12 months
                - self.roadmap: Is the Mortgage roadmap of all the quotas
                - self.inform: dict taht include the roadmap but also all the other relevant information of the mortgage
                - self.total_interest_pay: That is total amout to pay in interest
                - self.total_pay: Is the total ampount to pay of the Mortgage (dept + interest_pay)
            - Setters:
                - self:number_of_decimals: Setter that define the number of decimals (integer) of the outputs
            - Example::

                >>> a = Mortgage_Constant_ChargeOff(100000.,50,5)
                >>> a.create_Dataframe
                >>>
                >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
                >>>
                >>> a.create_XLSX_File('data/xlsx/output7.xlsx')
                >>> ...

    - Mortgage_Constant_Pay (class): Class that calculate an constant Pay Morgage:
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        - Methods:
            - Strict Class Methods:
                - getDecimals(cls): strict class method that return the defined number of decimals as output of the calculations
                - setDecimals(cls, value: int): strict class method that is used to set the number of decimals as output of the calculations
            - Create or Build Informs:
                - create_Dataframe(self): Create an dataframe with all the information related with the mortgage
                - create_XLS_File(self, path: str): method that create an excel file with the extension '.xls'
                - create_XLSX_File(self, path: str): method that create an excel file with the extension '.xlsx'
                - create_CSV_File(self, path: str): method that create an comma separated csv file with the extension '.csv'
            - Getters:
                - self.number_of_decimals: get the number of decimals for the outputs
                - self.initial_dept: Is the initial dept of the mortgage
                - self.quotas: Number of quotas of the Mortgage
                - self.APR: The interest that must be payed ofver an period of 12 months
                - self.roadmap: Is the Mortgage roadmap of all the quotas
                - self.inform: dict taht include the roadmap but also all the other relevant information of the mortgage
                - self.total_interest_pay: That is total amout to pay in interest
                - self.total_pay: Is the total ampount to pay of the Mortgage (dept + interest_pay)
            - Setters:
                - self:number_of_decimals: Setter that define the number of decimals (integer) of the outputs
            - Example::

                >>> a = Mortgage_Constant_Pay(100000.,50,5)
                >>> a.create_Dataframe
                >>>
                >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
                >>>
                >>> a.create_XLSX_File('data/xlsx/output7.xlsx')
                >>> ...

    Example:
    --------- ::

        >>> from mortgage_roadmap import *
        >>> Mortgage_Constant_ChargeOff.setDecimals(4))
        >>>
        >>> a = Mortgage_Constant_ChargeOff(100000., 50, 4,8)
        >>> a.create_Dataframe
        >>>
        >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
        >>>
        >>> a.create_XLSX_File('data/xlsx/mortgage_inform.xlsx')

"""

__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "0.1.3"

# ======== IMPORTS ===========

from .base import *

# ======= BASE FUNCTIONS =====

__all__ = [ 
            "Mortgage_Constant_ChargeOff", 
            "Mortgage_Constant_Pay"
        ]

if __name__ == '__main__':
    
    pass