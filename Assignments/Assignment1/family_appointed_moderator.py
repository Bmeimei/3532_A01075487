# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:13 
# File Name:        family_appointed_moderator.py

from menu import ViewMenu
from features import Features
from user import User
from user_types import UserTypes
from budget import Budgets
from transaction import Transaction
from categories import Categories


class FAM(ViewMenu, Features):
    """
    The F.A.M. (Family Appointed Moderator)
    This class implements two classes, 'ViewMenu' and 'Features' classes.
    Run execute_features to execute the program after instantiating the FAM object.
    Here's the skeleton of FAM:

    - registering_user
    - assigning_budget_categories
    - showing_menu

        - View Budgets
        - Record Transaction
        - View Transactions by Budget
        - View Bank Account Details

    - processing_menu_option
    - execute_features

    """

    __categories_dict = {"1": Categories.GAMES_ENTERTAINMENT, "2": Categories.CLOTHING_ACCESSORISE,
                         "3": Categories.EATING_OUT, "4": Categories.MISCELLANEOUS}
    """
    The Categories Dictionary.
    """

    __user_type_dict = {"1": UserTypes.ANGEL, "2": UserTypes.TROUBLEMAKER, "3": UserTypes.REBEL}
    """
    The User Type Dictionary.
    """

    def __init__(self) -> None:
        """
        Constructs a family appointed moderator.
        Instantiates the default user, and the transaction record is an empty list for containing transactions.
        """
        self.__user = User()
        self.__transaction_record = []

    def _registering_user(self) -> None:
        """
        The user (usually a parent) must register their child's financial details.
        This includes (but is not necessarily limited to):

        • The user name
        • Age
        • User Type
        • Bank Account number
        • Bank Name (optional)
        • Bank Balance
        • Their budgets
        """
        user_name = input("Please input user's name:")
        age = int(input("Please input user's age:"))
        user_type = self.__select_user_type()
        budgets = Budgets()
        bank_balance = float(input("Please input a positive bank balance:"))
        bank_name = input("Please input the bank name (Optional):")
        self.__user = User(user_name, age, user_type, budgets, bank_balance, bank_name)

    def _assigning_budget_categories(self) -> None:
        """
        Each child that is being monitored is assigned the following budget categories.
        The exact value of each budget is assigned when registering the child as a user.

        • Games and Entertainment
        • Clothing and Accessories
        • Eating Out
        • Miscellaneous
        """
        games_entertainment = float(input("Please input a positive budget for Games and Entertainment:"))
        clothing_accessories = float(input("Please input a positive budget for Clothing and Accessories:"))
        eating_out = float(input("Please input a positive budget for Eating Out:"))
        miscellaneous = float(input("Please input a positive budget for miscellaneous:"))
        self.__user.budgets = Budgets(games_entertainment, clothing_accessories, eating_out, miscellaneous)

    def _showing_menu(self) -> None:
        """
        Prints the menu.
        """
        print("1. View Budgets\n"
              "2. Record a Transaction\n"
              "3. View Transaction by Budget\n"
              "4. View Bank Account Details\n"
              "5. Exit")

    def _processing_menu_option(self, option: str) -> None:
        """
        Processing based on the menu option.
        """
        option_dict = {
            '1': self._view_budgets,
            '2': self.record_transaction,
            '3': self.view_transactions_by_budget,
            '4': self._view_bank_account_details,
            "5": self._exit_and_show_users_status
        }
        if option not in option_dict:
            print("Invalid Command!")
        else:
            option_dict[option]()

    def execute_features(self) -> None:
        """
        Execute F.A.M.

        :raise TypeError: If user inputs the wrong types.
        :raise ValueError: If user inputs wrong values.
        """
        try:
            print("Registering User:\n"
                  "-----------------")
            self._registering_user()

            print("Assigning Budgets Categories:\n"
                  "-----------------")
            self._assigning_budget_categories()

            option = None
            exit_command = "5"
            while option != exit_command:
                print("Menu:\n"
                      "-----------------")
                self._showing_menu()
                option = input("Please type the menu command:")
                self._processing_menu_option(option)
                print()
        except TypeError:
            print("Invalid Type!")
        except ValueError:
            print("Invalid Input Value!")

    def _view_budgets(self) -> None:
        """
        Shows the user the current status of their budgets (locked or not)
        in addition to the amount spent, amount left, and the total amount allocated to the budget.
        """
        print(self.__user.budgets)

    def record_transaction(self) -> None:
        """
        Takes the user to a sub-menu where they are prompted to enter the transaction details.

        :return: a recorded transaction
        """
        amount = float(input("Please type the positive amount for the purchase:"))
        category = self.__input_category()
        name = input("Please type the name of the shop/website where the purchase took place:")
        transaction = Transaction(amount, self.__user, category, name)
        if transaction.get_process_status():
            self.__transaction_record.append(transaction)

    def view_transactions_by_budget(self) -> None:
        """
        Takes the user to a sub-menu where they select their budget category
        and view all the transactions to date in that category.
        """
        select = input("Please type the category:\n"
                       "1: Games and Entertainment\n"
                       "2: Clothing and Accessorise\n"
                       "3: Eating Out\n"
                       "4: Miscellaneous\n")
        if select not in self.__categories_dict:
            print("Invalid Categories Command!")
            return None
        category = self.__categories_dict[select]
        transaction_sublist = filter(lambda x: x.get_category_type() == category, self.__transaction_record)
        transaction_sublist = sorted(transaction_sublist, key=lambda x: x.get_timestamp())
        if len(transaction_sublist) == 0:
            print("Currently no transactions in this Category: %s." % category)
        for key, transaction in enumerate(transaction_sublist):
            print(key + 1, ":", transaction)

    def _view_bank_account_details(self) -> None:
        """
        Prints out the bank account details of the user and all transactions
        conducted to date alongside the closing balance.
        """
        print(self.__user)
        transaction_sorted_list = sorted(self.__transaction_record, key=lambda x: x.get_timestamp())
        if len(transaction_sorted_list) == 0:
            print("Currently no transactions in this account.")
        for key, transaction in enumerate(transaction_sorted_list):
            print(key + 1, ":", transaction)

    def _exit_and_show_users_status(self) -> None:
        """
        Exits the program and shows the user status.
        """
        print(self.__user)

    def __input_category(self) -> Categories:
        """
        Helper function to select categories.
        :return: A specific category
        """
        categories_dict = self.__categories_dict
        while True:
            select = input("Please type the category:\n"
                           "1: Games and Entertainment\n"
                           "2: Clothing and Accessorise\n"
                           "3: Eating Out\n"
                           "4: Miscellaneous\n")
            if select in categories_dict:
                return categories_dict[select]
            print("Invalid Input!")

    def __select_user_type(self) -> UserTypes:
        """
        Helper function to select user type
        :return: A specific UserType
        """
        user_type_dict = self.__user_type_dict
        while True:
            select = input("User Type: 1: Angel  2: Troublemaker  3: Rebel:")
            if select in user_type_dict:
                return user_type_dict[select]
            print("Invalid Command! Please Type again\n"
                  "----------------------------------")


def main():
    """
    Driver!
    """
    fam = FAM()
    fam.execute_features()


if __name__ == '__main__':
    main()