""" mortgage_calculator.base:
    =========================

    Public classes that can be used as public packages features.

    Content:
    --------

    - Mortgage_Constant_ChargeOff (class): Class that calculate an constant chargeoff Morgage:
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        - Methods:
            - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
                - self._total_interest_pay ( float )
                - self._total_pay ( float )
                - self._roadmap ( list[dict])
                - self._inform (dict)
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
            - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
                - self._total_interest_pay ( float )
                - self._total_pay ( float )
                - self._roadmap ( list[dict])
                - self._inform (dict)
        - Example::

            >>> a = Mortgage_Constant_Pay(100000.,50,5)
            >>> a.inform
            >>>
            >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
            >>>
            >>> a.create_XLSX_File('data/xlsx/mortgage_inform.xlsx')
            >>> ...  
"""

# ======== IMPORTS ===========

from basic_decorators import argument_check

from ..core import Base_Mortgage

# ======= BASE FUNCTIONS =====

class Mortgage_Constant_ChargeOff(Base_Mortgage):
    """
    - Mortgage_Constant_ChargeOff: Class that calculate an constant chargeoff Morgage:
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        - Methods:
            - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
                - self._total_interest_pay ( float )
                - self._total_pay ( float )
                - self._roadmap ( list[dict])
                - self._inform (dict)
        - Example::

            >>> a = Mortgage_Constant_ChargeOff(100000.,50,5)
            >>> a.create_Dataframe
            >>>
            >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
            >>>
            >>> a.create_XLSX_File('data/xlsx/output7.xlsx')
            >>> ...
    """

    @argument_check(object, (int, float), int, (int, float))
    def __init__(self, INITIAL_DEPT: float | int, QUOTAS: int, APR: float | int) -> None:
        """
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        """
        Base_Mortgage.__init__(self, INITIAL_DEPT, QUOTAS, APR)

    def __CALCULATION__(self) -> bool:
        """
        - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
            - self._total_interest_pay ( float )
            - self._total_pay ( float )
            - self._roadmap ( list[dict])
            - self._inform (dict)
        """
        dept = self._INITIAL_DEPT
        quotas = self._QUOTAS
        charge_off = dept / quotas 
        percentage = self._APR

        total_interest_pay = 0
        total_pay = 0
        dictionary = []
        for i in range(quotas):
            dept += -charge_off
            interest_pay = (dept * 0.01 * percentage) / 12
            total_interest_pay += interest_pay
            topay = charge_off + interest_pay
            total_pay += topay
            row = {
                "cuota": i + 1,
                "dept": dept, 
                "charge_off": charge_off, 
                "interest_pay": interest_pay, 
                "cumulative_interest_pay": total_interest_pay, 
                "topay": topay 
                }
            dictionary.append(row)

        self._total_interest_pay = total_interest_pay
        self._total_pay = total_pay
        self._roadmap = dictionary
        self._inform = {"roadmap": dictionary, 
                        "total_pay": total_pay, 
                        "total_interest_pay": total_interest_pay,
                        "initial_dept": self._INITIAL_DEPT,
                        "quotas": self._QUOTAS,
                        "APR": self._APR
                        }
        return True


class Mortgage_Constant_Pay(Base_Mortgage):
    """
    - Mortgage_Constant_Pay: Class that calculate an constant Pay Morgage:
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        - Methods:
            - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
                - self._total_interest_pay ( float )
                - self._total_pay ( float )
                - self._roadmap ( list[dict])
                - self._inform (dict)
        - Example::

            >>> a = Mortgage_Constant_Pay(100000.,50,5)
            >>> a.create_Dataframe
            >>>
            >>> {'roadmap': [{'dept': 133543.56, 'charge_off': 1456.44, '.....
            >>>
            >>> a.create_XLSX_File('data/xlsx/output7.xlsx')
            >>> ...  
    """

    @argument_check(object, (int, float), int, (int, float))
    def __init__(self, INITIAL_DEPT: float | int, QUOTAS: int, APR: float | int) -> None:
        """
        - Parameters:
            - INITIAL_DEPT ( int | float): Is the initial dept of the mortgage
            - QUOTAS ( int ): Number of quotas of the Mortgage
            - APR ( int | float): The interest that must be payed ofver an period of 12 months
        """
        Base_Mortgage.__init__(self, INITIAL_DEPT, QUOTAS, APR)

    def __CALCULATION__(self) -> bool:
        """
        - __CALCULATION__(self): Meghod that is executed with the define parameters of the instance of the class. It define the atributes of the class that are needed for all the output methods of the class. 
            - self._total_interest_pay ( float )
            - self._total_pay ( float )
            - self._roadmap ( list[dict])
            - self._inform (dict)
        """
        try:
            import sympy as sp
        except Exception as exc:
            raise TypeError(f"WARNING: The 'sympy' library is not installed in the python Environment.\n{exc} ")

        dept = sp.Float(self._INITIAL_DEPT)
        percentage = self._APR
        cuotes = self._QUOTAS
        
        total_interest_pay = 0
        total_topay = 0
        dictionary = []
        topay = sp.Symbol('apargar')
        for i in range(cuotes):
            interest_pay = (dept * 0.01 * percentage) / 12
            charge_off = topay - interest_pay
            dept += -charge_off
            row = {
                "cuota": i + 1,
                "dept": dept, 
                "charge_off": charge_off, 
                "interest_pay": interest_pay, 
                "topay": topay 
            }
            dictionary.append(row)


        solve = sp.solveset(dept, topay)

        answere = float(solve.inf)


        for row in dictionary:
            row["charge_off"] = row["charge_off"].subs(topay,answere)

            row["dept"] = row["dept"].subs(topay,answere)

            iterest_pay_float = row["interest_pay"].subs(topay,answere)
            row["interest_pay"] = iterest_pay_float
            total_interest_pay += iterest_pay_float

            row["cumulative_interest_pay"] =  total_interest_pay.evalf()

            total_topay_float = row["topay"].subs(topay,answere)
            row["topay"] = total_topay_float
            total_topay += total_topay_float

            row["cumulative_topay"] =  total_topay.evalf()

        self._total_interest_pay = total_interest_pay
        self._total_pay = total_topay
        self._roadmap = dictionary
        self._inform = {"roadmap": dictionary, 
                        "total_pay": total_topay, 
                        "total_interest_pay": total_interest_pay,
                        "initial_dept": self._INITIAL_DEPT,
                        "quotas": self._QUOTAS,
                        "APR": self._APR
                        }
        
        return True

if __name__ == '__main__':
    
    pass