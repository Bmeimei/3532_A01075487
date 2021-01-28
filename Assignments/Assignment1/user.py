# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 10:21 
# File Name:        user.py

from user_types import UserTypes
from budget import Budgets
from exception import check_type, check_string_is_empty, check_all_input_type, check_all_input_value
from user_transaction import UserTransaction


class User(UserTransaction):
    """
    A bank account class for registering user.

    - name: child's name as a string
    - age: child's age as an int, could be 0.
    - user_type: user account type as UserTypes
    - budgets: child's budgets
    - bank_balance: account balance as a float, default value is 0
    - bank_name: bank name as a string, default value is ITCB
    """

    _BANK_NAME = "ITCB"
    """
    Default Bank Name is ITCB (Reverse of BCIT).
    """

    _DEFAULT_NAME = "Luke"
    """
    Default User Bank is Luke.
    """

    _DEFAULT_AGE = 10
    """
    Default Age is 10.
    """

    _DEFAULT_USER_TYPE = UserTypes.ANGEL
    """
    Default User Type is Angel Type.
    """

    _DEFAULT_BUDGET = Budgets()
    """
    Default Budgets.
    """

    _INITIAL_BALANCE = 0
    """
    Default account Balance is 0.
    """

    def __init__(self, name: str = _BANK_NAME, age: int = _DEFAULT_AGE, user_type: UserTypes = _DEFAULT_USER_TYPE,
                 budgets: Budgets = _DEFAULT_BUDGET, bank_balance: float = _INITIAL_BALANCE,
                 bank_name: str = _BANK_NAME) -> None:
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
        super().__init__(budgets, user_type, bank_balance)
        self.__check_input_type_and_value(name, age, user_type, budgets, bank_balance, bank_name)
        self._name = name
        self._age = age
        if len(bank_name.strip()) == 0:
            bank_name = self._BANK_NAME
        self._bank_name = bank_name

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
        check_all_input_value([age, bank_balance], self._INITIAL_BALANCE)

    @property
    def name(self) -> str:
        """
        Gets User name.

        :return: user name as a string
        """
        return self._name.title()

    @property
    def age(self) -> int:
        """
        Gets User age.

        :return: user age as an int
        """
        return self._age

    @property
    def bank_name(self) -> str:
        """
        Gets bank name.

        :return: bank name as a string
        """
        return self._bank_name

    def __str__(self) -> str:
        """
        Returns A formatted string that represents the current user.

        :return: A formatted string that represents the current user.
        """
        return "Name: %s\n" \
               "Age: %d\n" \
               "User Type: %s\n" \
               "Budgets: {%s}\n" \
               "Bank Balance: %s\n" \
               "Bank Name: %s" % (self._name, self._age, self._user_type,
                                  self.budgets.__str__(), self._bank_balance, self._bank_name)

    def __repr__(self) -> str:
        """
        Returns a string that represents the status of current user.

        :return: A long string with a bracket that shows the status of user
        """
        return "{%s, %d, %s, %s, %f, %s}" % (self._name, self._age, self._user_type,
                                             self.budgets.__repr__(), self._bank_balance, self._bank_name)


def main():
    budget = Budgets(500, 500, 500, 500)
    user = User("Luke", 20, UserTypes.ANGEL, budget, 1000)
    print(user)


if __name__ == '__main__':
    main()