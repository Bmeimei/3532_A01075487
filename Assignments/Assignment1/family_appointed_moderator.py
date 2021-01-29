# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/20 0:13 
# File Name:        family_appointed_moderator.py

from menu import ViewMenu
from features import Features
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

    @staticmethod
    def _showing_menu() -> None:
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
            '2': self._record_transaction,
            '3': self._view_transactions_by_budget,
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
        print(self._user.budgets)

    def _record_transaction(self) -> None:
        """
        Takes the user to a sub-menu where they are prompted to enter the transaction details.

        :return: a recorded transaction
        """
        amount = float(input("Please type the positive amount for the purchase:"))
        category = self.__input_category()
        name = input("Please type the name of the shop/website where the purchase took place:")
        self._user.process_and_record_transaction(amount, category, name)

    def _view_transactions_by_budget(self) -> None:
        """
        Takes the user to a sub-menu where they select their budget category
        and view all the transactions to date in that category.
        """
        select = input("Please type the category:\n"
                       "1: Games and Entertainment\n"
                       "2: Clothing and Accessorise\n"
                       "3: Eating Out\n"
                       "4: Miscellaneous\n")
        if select not in self._categories_dict:
            print("Invalid Categories Command!")
            return None
        category = self._categories_dict[select]
        transaction_record = self._user.budgets.get_transaction_history()
        transaction_sublist = filter(lambda x: x.get_category_type() == category, transaction_record)
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
        print(self._user)
        transaction_record = self._user.budgets.get_transaction_history()
        transaction_sorted_list = sorted(transaction_record, key=lambda x: x.get_timestamp())
        if len(transaction_sorted_list) == 0:
            print("Currently no transactions in this account.")
        for key, transaction in enumerate(transaction_sorted_list):
            print(key + 1, ":", transaction)

    def _exit_and_show_users_status(self) -> None:
        """
        Exits the program and shows the user status.
        """
        print(self._user)
        print("-------------------------------\n"
              "THANKS FOR USING F.A.M. ^ ^")

    def __input_category(self) -> Categories:
        """
        Helper function to select categories.
        :return: A specific category
        """
        categories_dict = self._categories_dict
        while True:
            select = input("Please type the category:\n"
                           "1: Games and Entertainment\n"
                           "2: Clothing and Accessorise\n"
                           "3: Eating Out\n"
                           "4: Miscellaneous\n")
            if select in categories_dict:
                return categories_dict[select]
            print("Invalid Input!")


def main():
    """
    Driver!
    """
    fam = FAM()
    fam.execute_features()


if __name__ == '__main__':
    main()