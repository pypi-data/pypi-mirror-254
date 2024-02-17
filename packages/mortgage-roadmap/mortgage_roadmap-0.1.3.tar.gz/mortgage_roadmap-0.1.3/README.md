# mortgage_calculator

Repository that calculate the mortgage roadmap of two types of mortgage calculators:

* Mortgage_Constant_ChargeOff: Mortgage roadmap where you pay an constat chart off each month
* Mortgage_Constant_Pay: Mortgage roadmap where you pay an constat fee each monthmap

## How it work:

1. Create en python environent and install the package using de command:
    ````
    pip install mortgage-roadmap
    ````
2. Once you get installed the package you can import the packahe in the python module by:

    - import the classes:

        ````python
        from mortgage_roadmap import ( Mortgage_Constant_ChargeOff, Mortgage_Constant_Pay )
        ````

    - import the module:
        ````python
        import mortgage_roadmap 
        ````

## Examples:

1. Basic exaple where we import the nodule with all the classes. Then we change the amount of units that we will as output. Thrn we create a dataframe as output an as last we export the information in an excel file

````python
from mortgage_roadmap import *
Mortgage_Constant_ChargeOff.setDecimals(4)

a = Mortgage_Constant_ChargeOff(100000., 50, 4,8)

a.create_Dataframe

{'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....'

a.create_XLSX_File('data/xlsx/mortgage_inform.xlsx')
````

## Compatibility:

1. Dependency of this package: 
    * sympy
    * basic-decorators

2. Optional Packages to use all features of this package:
    * pandas
    * openpyxl

## Content:

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


