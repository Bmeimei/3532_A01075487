# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 10:21 
# File Name:        user.py

from user_types import UserTypes
from user_type import UserType
from troublemaker import Troublemaker
from angel import Angel
from rebel import Rebel
from budget import Budgets
from transaction import Transaction
from exception import check_type, check_string_is_empty, check_all_input_type, check_all_input_value


class User:
    """
    A bank account class for registering user.
    """

    _BANK_NAME = "ITCB"
    """
    Default Bank Name is ITCB (Reverse of BCIT).
    """

    _INITIAL_BALANCE = 0
    """
    Default account Balance is 0.
    """

    def __init__(self, name: str, age: int, user_type: UserTypes, budgets: Budgets,
                 bank_balance: float = _INITIAL_BALANCE, bank_name: str = _BANK_NAME) -> None:
        """
        User account includes Child's financial details.

        :param name: child's name as a string
        :param age: child's age as an int, could be 0.
        :param user_type: user account type
        :param budgets: child's budgets
        :param bank_balance: account balance as a float, default value is 0
        :param bank_name: bank name as a string, default value is ITCB
        :raise TypeError: if the input variables are invalid types.
        :raise ValueError: if the input are invalid values.
        """
        self.__check_input_type_and_value(name, age, user_type, budgets, bank_balance, bank_name)
        self._name = name
        self._age = age
        self._budgets = budgets
        self._user_type = self.__select_account_type(user_type)
        self._bank_balance = bank_balance
        self._bank_name = bank_name
        self._transactions_record = []

    def __check_input_type_and_value(self, name: str, age: int, user_type: UserTypes, budgets: Budgets,
                                     bank_balance: float, bank_name: str) -> None:
        """
        Checks the inputs type and value before constructing the class.

        :param name: child's name as a string
        :param age: child's age as an int, could be 0.
        :param user_type: user account type
        :param budgets: child's budgets
        :param bank_balance: account balance as a float, default value is 0
        :param bank_name: bank name as a string, default value is ITCB
        :raise TypeError: if the input variables are invalid types.
        :raise ValueError: if the age or bank balance is negative.
        """
        check_all_input_type([name, bank_name], str)
        check_all_input_type([age, bank_balance], int, float)
        check_type(user_type, UserTypes)
        check_type(budgets, Budgets)
        check_string_is_empty(name)
        check_string_is_empty(bank_name)
        check_all_input_value([age, bank_balance], self._INITIAL_BALANCE)

    def __select_account_type(self, user_type: UserTypes) -> UserType:
        """
        Returns a specific user type and passing the current budgets based on the input UserTypes.

        :param user_type: input UserTypes as a Enum UserTypes.
        :return: a specific user type
        """
        total_account = {
            UserTypes.TROUBLEMAKER: Troublemaker,
            UserTypes.REBEL: Rebel,
            UserTypes.ANGEL: Angel
        }
        return total_account.get(user_type)(self.budgets)

    def __str__(self) -> str:
        """
        Returns A formatted string that represents the current user.

        :return: A formatted string that represents the current user.
        """
        return "Name: %s\n" \
               "Age: %d\n" \
               "User Type: %s\n" \
               "Budgets: {%s}\n" \
               "Bank Balance: %f\n" \
               "Bank Name: %s" % (self._name, self._age, self._user_type,
                                  self._budgets.__str__(), self._bank_balance, self._bank_name)

    def __repr__(self) -> str:
        """
        Returns a string that represents the status of current user.

        :return: A long string with a bracket that shows the status of user
        """
        return "{%s, %d, %s, %s, %f, %s}" % (self._name, self._age, self._user_type,
                                             self._budgets.__repr__(), self._bank_balance, self._bank_name)

    def get_name(self) -> str:
        """
        Gets User name.

        :return: user name as a string
        """
        return self._name

    def get_age(self) -> int:
        """
        Gets User age.
        :return: user age as an int
        """
        return self._age

    def get_user_type(self) -> UserType:
        """
        Gets user account type.
        :return: user account type
        """
        return self._user_type

    def get_bank_name(self) -> str:
        """
        Gets bank name.
        :return: bank name as a string
        """
        return self._bank_name

    @property
    def budgets(self) -> str:
        """
        Creates a property for budgets.

        :return: A formatted string that represents the budgets
        """
        return self._budgets.__str__()

    @budgets.setter
    def budgets(self, budgets: Budgets) -> None:
        """
        Sets a new budget.

        :param budgets: the new budget that replaces the old one
        """
        self._budgets = budgets

    @property
    def bank_balance(self) -> float:
        """
        Creates a property for bank balance.

        :return: the bank balance as a float
        """
        return self._bank_balance

    @bank_balance.setter
    def bank_balance(self, bank_balance) -> None:
        """
        Sets the bank balance.

        :param bank_balance: new bank balance as a float
        """
        self._bank_balance = bank_balance

    def get_transactions(self) -> list:
        """
        Gets the total transactions record.

        :return: The history transactions as a list
        """
        return self._transactions_record

    def conduct_transactions(self, transaction: Transaction) -> None:
        """
        Conducts a transaction and add it into history transactions.

        :param transaction: a new transaction
        """
        self._transactions_record.append(transaction)


def main():
    user = User("Luke", 20, UserTypes.TROUBLEMAKER, Budgets())
    print(user)


if __name__ == '__main__':
    main()