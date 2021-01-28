# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 22:22 
# File Name:        budget.py

from exception import check_all_input_type, check_all_input_value
from categories import Categories
from rebel import Rebel
from user_type import UserType
from user_lockable_type import LockableUserType
from transaction import Transaction


class Budgets:
    """
    Each child that is being monitored is assigned the following budget categories.
    The exact value of each budget is assigned when registering the child as a user.

    Budgets has four attributes as floats, including:

    - Games and Entertainment
    - Clothing and Accessorise
    - Eating Out
    - Miscellaneous
    """

    _INITIAL_BALANCE = 0
    """
    Default Balance for Budgets is 0.
    """

    def __init__(self, games_entertainment: float = _INITIAL_BALANCE, clothing_accessorise: float = _INITIAL_BALANCE,
                 eating_out: float = _INITIAL_BALANCE, miscellaneous: float = _INITIAL_BALANCE):
        """
        Constructs the Budgets.
        There are two dicts in the constructor. categories and status.

        - categories is to record the original budgets in four categories
        - account_status represents if the account is ban or not. True means active,
          False means the account has been banned.
        - status is to record the status of categories. True means active, False means lock out

        :param games_entertainment: Cost for games and entertainment as a non zero number
        :param clothing_accessorise: Cost for clothing accessorise as a non zero number
        :param eating_out: Cost for eating out as a non zero number
        :param miscellaneous: Cost for miscellaneous as a non zero number
        :precondition: These four parameters must be non zero numbers.
        :raise TypeError: if one of these four parameters is not a number
        :raise ValueError: if ont of these four parameters is a negative number
        """
        total_list = [games_entertainment, clothing_accessorise, eating_out, miscellaneous]
        check_all_input_type(total_list, int, float)
        check_all_input_value(total_list, self._INITIAL_BALANCE)
        self._games_entertainment = games_entertainment
        self._clothing_accessorise = clothing_accessorise
        self._eating_out = eating_out
        self._miscellaneous = miscellaneous
        self.__categories = {
                            Categories.GAMES_ENTERTAINMENT: games_entertainment,
                            Categories.CLOTHING_ACCESSORISE: clothing_accessorise,
                            Categories.EATING_OUT: eating_out,
                            Categories.MISCELLANEOUS: miscellaneous
        }

        self.__account_status = True
        self.__status = {
                        Categories.GAMES_ENTERTAINMENT: True,
                        Categories.CLOTHING_ACCESSORISE: True,
                        Categories.EATING_OUT: True,
                        Categories.MISCELLANEOUS: True
        }
        self.__transaction_history = []

    def process_transaction(self, transaction: Transaction, user_type: UserType) -> None:
        """
        Process a transaction, and push it into transaction history.
        This method might lock the category or account depends on the user type.
        """
        amount = transaction.get_amount()
        category = transaction.get_category_type()
        self._deduct_category_budget(category, amount)
        self.__process_exceed_budgets(user_type, category)
        self.__transaction_history.append(transaction)

    def get_transaction_history(self) -> list[Transaction]:
        """
        Returns the transaction history.

        :return: the transaction history as a list
        """
        return self.__transaction_history

    def get_account_status(self) -> bool:
        """
        Gets the boolean of the status of the account.
        True means not locked, False means banned.

        :return: A boolean that represents the account status
        """
        return self.__account_status

    def get_status(self, category: Categories) -> bool:
        """
        Gets the boolean of the lock status of a single category.
        True means not locked, False means locked.

        :param category: a category which would be searched for
        :return: A boolean that represents the lock status of category
        """
        return self.__status[category]

    def is_category_exceed(self, category: Categories) -> bool:
        """
        Checks if a specific category exceed the budget.
        :param category: the specific category
        :return: True if the category budget is under 0
        """
        category_dict = self._get_current_category_dict()
        return category_dict[category] < self._INITIAL_BALANCE

    def numbers_of_exceed_category(self) -> int:
        """
        Returns the number of exceed category.

        :return: the number of exceed category as an int
        """
        category_dict = self._get_current_category_dict()
        return len(list(filter(lambda x: x < self._INITIAL_BALANCE, category_dict.values())))

    def lock_category(self, category: Categories) -> None:
        """
        Locks a single category to prevent future transaction.

        :param category: a category which would be locked
        """
        self.__status[category] = False

    def ban_account(self) -> None:
        """
        Bans this budget account. All the category would be locked, and user can't do any transactions.
        """
        self.__account_status = False
        categories = [Categories.GAMES_ENTERTAINMENT, Categories.CLOTHING_ACCESSORISE,
                      Categories.EATING_OUT, Categories.MISCELLANEOUS]
        for category in categories:
            self.lock_category(category)

    def _deduct_category_budget(self, category: Categories, amount: float) -> None:
        """
        Sets the specific category.
        The category would deduct amount.

        :param category: the specific category that would be changed
        :param amount: the process amount
        """
        if category == Categories.GAMES_ENTERTAINMENT:
            self.games_entertainment -= amount
        elif category == Categories.CLOTHING_ACCESSORISE:
            self.clothing_accessorise -= amount
        elif category == Categories.EATING_OUT:
            self.eating_out -= amount
        else:
            self.miscellaneous -= amount

    def __process_exceed_budgets(self, user_type: UserType, category: Categories) -> None:
        """
        Helper function to process exceed budgets. Including:

        - Show notified
        - Show warning
        - Lock Category
        - Ban account
        """
        self.__show_notify_if_need(user_type, category)
        self.__show_warning_if_need(user_type, category)
        if isinstance(user_type, LockableUserType):
            self.__lock_category_if_need(user_type, category)
            self.__ban_account_if_need(user_type)

    def __lock_category_if_need(self, user_type: LockableUserType, category: Categories) -> None:
        """
        Locks the category after transaction if the remaining budgets below the lock threshold.
        """
        threshold = user_type.get_lock_threshold()
        if self.get_current_category(category) < self.get_origin_category(category) * (1 - threshold):
            self.lock_category(category)
            print(user_type.lock_category_message(category))

    def __ban_account_if_need(self, user_type: LockableUserType) -> None:
        """
        Bans the account. Only works for Rebel class which has over 1 locked categories.
        """
        if isinstance(user_type, Rebel) and self.numbers_of_exceed_category() > 1:
            self.ban_account()
            print(user_type.ban_account_message())

    def __show_warning_if_need(self, user_type: UserType, category: Categories) -> None:
        """
        The user would receive a warning that they are getting close
        to exceeding their assigned budget for the category in question.
        """
        threshold = user_type.get_threshold()
        if self.get_current_category(category) < self.get_origin_category(category) * (1 - threshold)\
                and not self.is_category_exceed(category):
            print(user_type.warning_message(category))

    def __show_notify_if_need(self, user_type: UserType, category: Categories) -> None:
        """
        The user receives a notification that they have exceeded their assigned budget for the category in question.
        """
        if self.is_category_exceed(category):
            print(user_type.notified(category))

    def get_category_status(self, category: Categories) -> str:
        """
        Gets a formatted string that represents the total status of single category.

        :param category: a category which would be searched for
        :return: a formatted string that represents the total status of single category.
        """
        origin = self.get_origin_category(category)
        current = self.get_current_category(category)
        status = "Active" if self.get_status(category) else "Locked"
        return "Status: {0}, Amount Spent: {1}, Amount Left: {2}, Total Amount: {3}".format(
            status, origin - current, current, origin)

    def get_origin_category(self, category: Categories) -> float:
        """
        Gets the original specific category amount from the category list.

        :param category: a category which would be searched for
        :return: A float that represents the specific category cost
        """
        return self.__categories[category]

    def get_current_category(self, category: Categories) -> float:
        """
        Gets the current specific category amount.
        :param category: a category which would be searched for
        :return: A float that represents the specific category cost
        """
        category_dict = self._get_current_category_dict()
        return category_dict[category]

    def _get_current_category_dict(self) -> dict:
        """
        Gets the current specific category dict.

        :return: current category dict
        """
        category_dict = {
            Categories.GAMES_ENTERTAINMENT: self.games_entertainment,
            Categories.CLOTHING_ACCESSORISE: self.clothing_accessorise,
            Categories.EATING_OUT: self.eating_out,
            Categories.MISCELLANEOUS: self.miscellaneous
        }
        return category_dict

    @property
    def games_entertainment(self) -> float:
        """
        Getter for games and entertainment.

        :return: a float that represents the games and entertainment
        """
        return self._games_entertainment

    @games_entertainment.setter
    def games_entertainment(self, games_entertainment: float) -> None:
        """
        Setter for games and entertainment.

        :param games_entertainment: new games and entertainment as a float
        """
        self._games_entertainment = games_entertainment

    @property
    def clothing_accessorise(self) -> float:
        """
        Getter for games and entertainment.

        :return: a float that represents the clothing_accessorise
        """
        return self._clothing_accessorise

    @clothing_accessorise.setter
    def clothing_accessorise(self, clothing_accessorise: float) -> None:
        """
        Setter for clothing_accessorise

        :param clothing_accessorise: new clothing and accessorise as a float
        """
        self._clothing_accessorise = clothing_accessorise

    @property
    def eating_out(self) -> float:
        """
        Getter for eating_out

        :return: a float that represents the eating out
        """
        return self._eating_out

    @eating_out.setter
    def eating_out(self, eating_out: float) -> None:
        """
        Setter for eating out.

        :param eating_out: new eating out as a float
        """
        self._eating_out = eating_out

    @property
    def miscellaneous(self) -> float:
        """
        Getter for miscellaneous.

        :return: a float that represents the miscellaneous
        """
        return self._miscellaneous

    @miscellaneous.setter
    def miscellaneous(self, miscellaneous: float) -> None:
        """
        Setter for games and entertainment.

        :param miscellaneous: new miscellaneous as a float
        """
        self._miscellaneous = miscellaneous

    def __str__(self) -> str:
        """
        Returns a formatted string that represents the current balance for budget,
        in addition to the amount spent, amount left, and the total amount allocated to the budget.

        :return: a formatted string of budget.
        """
        account_status = "Active" if self.get_account_status() else "Banned"
        status_list = [self.get_category_status(Categories.GAMES_ENTERTAINMENT),
                       self.get_category_status(Categories.CLOTHING_ACCESSORISE),
                       self.get_category_status(Categories.EATING_OUT),
                       self.get_category_status(Categories.MISCELLANEOUS)]
        return "Account Status: %s\n" \
               "Games and Entertainment:  %s\n" \
               "Clothing and Accessorise: %s\n" \
               "Eating Out:               %s\n" \
               "Miscellaneous:            %s" % (account_status,
                                                 status_list[0], status_list[1], status_list[2], status_list[3])

    def __repr__(self) -> str:
        """
        Returns the string that represents the status of this budget.

        :return: a bunch of numbers that represents the status of budget
        """
        return "{%f, %f, %f, %f}" % (self._games_entertainment, self._clothing_accessorise,
                                     self._eating_out, self._miscellaneous)