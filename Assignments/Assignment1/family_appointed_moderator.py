# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/23 11:43 
# File Name:        family_appointed_moderator.py

from user import User
from transaction import Transaction
from exception import check_type


class FAM:

    def __init__(self, user: User, transaction: Transaction):
        check_type(user, User)
        check_type(transaction, Transaction)
        self._user = user
        self._transaction = transaction
        self._user_type = user.get_user_type()