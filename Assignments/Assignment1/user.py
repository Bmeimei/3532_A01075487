# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 10:21 
# File Name:        user.py

from user_types import UserTypes
from user_type import UserType
from user_lockable_type import LockableUserType
from troublemaker import Troublemaker
from angel import Angel
from rebel import Rebel
from categories import Categories
from budget import Budgets
from transaction import Transaction
from exception import check_type, check_string_is_empty, check_all_input_type, check_all_input_value


class User:
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

    def __init__(self, name: str = _BANK_NAME, age: int = _DEFAULT_AGE,
                 user_type: UserTypes = _DEFAULT_USER_TYPE,
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
        self.__check_input_type_and_value(name, age, user_type, budgets, bank_balance, bank_name)
        self._name = name
        self._age = age
        self._budgets = budgets
        self._user_type = self.select_account_type(user_type)
        self._bank_balance = bank_balance
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

    @staticmethod
    def select_account_type(user_type: UserTypes) -> UserType or LockableUserType:
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
        return total_account.get(user_type)()

    def get_name(self) -> str:
        """
        Gets User name.

        :return: user name as a string
        """
        return self._name.title()

    def get_age(self) -> int:
        """
        Gets User age.

        :return: user age as an int
        """
        return self._age

    def get_user_type(self) -> UserType or LockableUserType:
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

    def get_categories_status(self, categories: Categories) -> bool:
        """
        Gets the categories status. True if it is active, False if it is locked.

        :return: categories status as a boolean
        """
        return self._budgets.get_status(categories)

    def get_account_status(self) -> bool:
        """
        Gets the boolean of the status of the account.
        True means not locked, False means banned.

        :return: A boolean that represents the account status
        """
        return self._budgets.get_account_status()

    def create_transaction(self, amount: float, category: Categories, name: str) -> Transaction or None:
        """
        Creates a transaction for budgets.

        :param amount: shopping amount as a float
        :param category: a specific category
        :param name: The name of the shop/website where the purchase took place.
        :return: if transaction success, return a Transaction instance. Otherwise return None.
        """
        if not self._verify_account(amount, category):
            return None
        return Transaction(amount, category, name)

    def process_and_record_transaction(self, amount: float, category: Categories, name: str) -> None:
        """
        Process a transaction. Record it into transaction list if it is not None.
        """
        transaction = self.create_transaction(amount, category, name)
        if transaction is not None:
            print("Your transaction has been processed successfully!\n")
            print(transaction)
            self.budgets.process_transaction(transaction, self._user_type)

    def _verify_account(self, amount: float, category: Categories) -> bool:
        """
        Helper function to verify the account status.

        :return: True if the account is valid to process transaction. False otherwise.
        """
        if not self.get_categories_status(category):
            print(self.get_user_type().lock_category_message(category) + " Transaction has been REJECTED!")
            return False
        if not self.get_account_status():
            print(self.get_user_type().ban_account_message() + " Transaction has been REJECTED!")
            return False
        if self._bank_balance < amount:
            print("Your bank balance is insufficient to afford this purchase!")
            return False
        return True

    @property
    def budgets(self) -> Budgets:
        """
        Creates a property for budgets.

        :return: A formatted string that represents the budgets
        """
        return self._budgets

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
                                  self._budgets.__str__(), self._bank_balance, self._bank_name)

    def __repr__(self) -> str:
        """
        Returns a string that represents the status of current user.

        :return: A long string with a bracket that shows the status of user
        """
        return "{%s, %d, %s, %s, %f, %s}" % (self._name, self._age, self._user_type,
                                             self._budgets.__repr__(), self._bank_balance, self._bank_name)


def main():
    budget = Budgets(500, 500, 500, 500)
    user = User("Luke", 20, UserTypes.ANGEL, budget, 1000)
    print(user)


if __name__ == '__main__':
    main()