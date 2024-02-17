# -*- coding: utf-8 -*-
""" mortgage_calculator.core:
    =========================

    Core classes that are used for the main public package methods

    Content:
    --------

    - strict_classmethod: Class that is used as an decorator on class methods that make thosee methods only accesible as strict class methods::

        >>> @strict_classmethod
        >>> def getDecimals(cls):
        >>>     return cls.__number_of_decimals

    - DataFrame: Empty class that is used only as type hint. So that it can be used without the import of the 'pandas library'::

        >>> def create_Dataframe(self) -> DataFrame:
        >>>     ...

    - Base_Mortgage(ABC): Class that is used for the public Mortgage calculator subclasses that includes as main methods::
        - Process:
            - __CALCULATION__(self): abstract empty method that must be overrided by the subclasses. That are used as the main calculation.
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
            - self.number_of_decimals: Setter that define the number of decimals (integer) of the outputs
"""

# ======== IMPORTS ===========

from abc import ABC, abstractmethod
from functools import partial
from pathlib import Path
from typing import Literal
from types import MethodType
from copy import copy
import json

from basic_decorators import argument_check

# ======= BASE FUNCTIONS =====

class strict_classmethod():
    """
    Class that is used as an decorator on class methods that make thosee methods only accesible as strict class methods
    """
    def __init__(self, func):
         self.func = func

    def __get__(self, instance, owner):
         if instance is not None:
              raise TypeError("This method cannot be called from instances")
         return partial(self.func, owner)

class DataFrame():
    """
    Is the pd.DataFrame class that is used as an type hint without the need of importig the 'Pandas' library
    """
    pass 

class Base_Mortgage(ABC):
    """
    Class that is used for the public Mortgage calculator subclasses that includes as main methods::
    """
    __number_of_decimals: int = 2 # Because we want it editable as an strict class method and alse an setter with properties
    __default_number_of_decimals: int = 2 

    @argument_check(object, (int, float), int, (int, float))
    def __init__(self, INITIAL_DEPT: float | int, QUOTAS: int, APR: float | int) -> None:
        self._INITIAL_DEPT: float = float(INITIAL_DEPT)
        self._QUOTAS: int = QUOTAS
        self._APR: float = float(APR)
        self._roadmap: list[dict] | list = []
        self._total_interest_pay: float = 0.
        self._total_pay: float = 0.
        self._inform: dict = {}
        self.__pandas_installed: bool = False
        self.__default_number_of_decimals: int = 2 
        self.__isPandasInstalled()
        self.__CALCULATION__()

    @abstractmethod
    def __CALCULATION__(self) -> None: 
        """abstract empty method that must be overrided by the subclasses. That are used as the main calculation."""
        pass
    
    @strict_classmethod
    def reset(cls):
        """strict class method that return the class to his original default state"""
        cls.__number_of_decimals = cls.__default_number_of_decimals
        return True

    @strict_classmethod
    def getDecimals(cls):
        """strict class method that return the defined number of decimals as output of the calculations"""
        return cls.__number_of_decimals
    
    @strict_classmethod
    @argument_check(object, int)
    def setDecimals(cls, value: int) -> None:
        """strict class method that is used to set the number of decimals as output of the calculations"""
        cls.__number_of_decimals = value
    
    def __isPandasInstalled(self) -> bool:
        try:
            global pd
            import pandas as pd
            self.__pandas_installed = True
            return True
        except:
            print("INFO: 'pandas' Library is not installed.")
            return False

    def __handlePandasException(self) -> Literal[True]:
        if self.__pandas_installed :
            return True
        else:
            raise TypeError(f"WARNING: The 'pandas' library is not installed in the python Environment.")
        
    def create_Dataframe(self) -> DataFrame:
        """Create an dataframe with all the information related with the mortgage"""
        if self.__handlePandasException() :
            roadmap = pd.DataFrame.from_dict(self.roadmap)
            new_inform = copy(self.inform)
            del new_inform["roadmap"]
            extras = pd.DataFrame.from_dict([new_inform])
            return pd.concat([roadmap,extras],axis = 1)
    
    @argument_check(object, str) 
    def __getFileExtension(self, path: str) -> str:
            return Path(path).suffix

    @argument_check(object, str, [".xls", ".xlsx", ".csv", ".json"], MethodType)
    def __create_File_Process(self, path: str, fileformat: Literal[".xls", ".xlsx", ".csv", ".json"], PROCESS: MethodType) -> bool:
        if self.__handlePandasException() :
            if (self.__getFileExtension(path) == fileformat ):
                return PROCESS(path)
            else:
                raise TypeError(f"WARNING: the extension of the file must be: '{fileformat}'")
        return False

    @argument_check(object, str)
    def __build_JSON(self, path) -> Literal[True]:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.inform, f, ensure_ascii=False, indent=4)
        return True
    
    @argument_check(object, str)
    def create_JSON_File(self, path: str) -> bool:
        """method that create an JSON file with the extension '.json'"""
        return self.__create_File_Process(path, ".json", self.__build_JSON)

    @argument_check(object, str)
    def __build_EXCEL(self, path: str) -> Literal[True]:
        df = self.create_Dataframe()
        with pd.ExcelWriter(path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        return True
    
    @argument_check(object, str)
    def create_XLS_File(self, path: str) -> bool:
        """method that create an excel file with the extension '.xls'"""
        return self.__create_File_Process(path, ".xls", self.__build_EXCEL)

    
    @argument_check(object, str)
    def create_XLSX_File(self, path: str) -> bool:
        """method that create an excel file with the extension '.xlsx'"""
        return self.__create_File_Process(path, ".xlsx", self.__build_EXCEL)

    @argument_check(object, str)
    def __build_CSV(self, path: str) -> Literal[True]:
        df = self.create_Dataframe()
        df.to_csv(path)
        return True

    @argument_check(object, str)    
    def create_CSV_File(self, path: str) -> bool:
        """method that create an comma separated csv file with the extension '.csv'"""
        return self.__create_File_Process(path, ".csv", self.__build_CSV)

    @argument_check(object, float)
    def __makeupNumbers(self, number: float) -> float:
        return round(number, self.__number_of_decimals)

    @property
    def number_of_decimals(self) -> int:
        """get the number of decimals for the outputs"""
        return self.__number_of_decimals
    
    @number_of_decimals.setter
    @argument_check(object, int)
    def number_of_decimals(self, number_of_decimals: int) -> None:
        """Setter that define the number of decimals (integer) of the outputs"""
        self.__number_of_decimals = number_of_decimals

    @property
    def initial_dept(self) -> float:
        """Is the initial dept of the mortgage"""
        return self.__makeupNumbers(self._INITIAL_DEPT)
    
    @property
    def quotas(self) -> int:
        """Number of quotas of the Mortgage"""
        return self._QUOTAS
    
    @property
    def APR(self) -> float:
        """The interest that must be payed ofver an period of 12 months"""
        return self.__makeupNumbers(self._APR)

    @property
    def roadmap(self) -> list[dict[str, float | int ]]:
        """Is the Mortgage roadmap of all the quotas"""
        new_roadmap=[]
        for row in self._roadmap:
            new_row = {}
            for key, value in row.items():
                if key == "cuota" :
                    new_row[key] = int(value)
                else:
                    new_row[key] = self.__makeupNumbers(float(value)) 
            new_roadmap.append(new_row)
        return new_roadmap
    
    @property
    def inform(self) -> dict[str, str | list[ dict[str, float | int]]]:
        """dict that include the roadmap but also all the other relevant information of the mortgage"""
        new_inform = {}
        for key in self._inform:
            new_inform[key] = getattr(self,key)    
        return new_inform

    @property
    def total_interest_pay(self) -> float:
        """That is total amout to pay in interest"""
        return self.__makeupNumbers(float(self._total_interest_pay))

    @property
    def total_pay(self) -> float:
        """Is the total ampount to pay of the Mortgage (dept + interest_pay)"""
        return self.__makeupNumbers(float(self._total_pay))
     

if __name__ == '__main__':
    
    pass