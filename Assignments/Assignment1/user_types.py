# Author:           Luke Mei
# Student Number :  A01075487
# Created time :    2021/1/19 21:53 
# File Name:        user_types.py
from enum import Enum, auto

class UserTypes(Enum):
    """
    The Enum class that contains three different User Types.
    Including:

    - Angel
    - Troublemaker
    - Rebel
    """

    ANGEL = auto()
    """
    The Angel represents a user who's parents are not worried at all.
    This child has never (as far as their parents are concerned) broken a single rule.
    They already have a five-year plan in place and a roadmap which is guaranteed to get them into Harvard.
    The Angel is the child who would set up their own FAM account so they can monitor their expenses.
    
    - Never gets locked out of a budget category.
      They can continue spending money even if they exceed the budget in question.
    - Gets politely notified if they exceed a budget category.
    - Gets a warning if they exceed more than 90% of a budget.
    """

    TROUBLEMAKER = auto()
    """
    The Troublemaker represents a user who often finds themselves in... well.. trouble.
    These are usually minor incidents and their parents are concerned but not worried.
    Parents usually set up a FAM account to monitor their expenses and impose light restrictions.
    
    - Gets a warning if they exceed more than 75% of a budget category.
    - Gets politely notified iIf they exceed a budget category.
    - Gets locked out of conducting transactions in a budget category
      if they exceed it by 120% of the amount assigned to the budget in question.
    """

    REBEL = auto()
    """
    The Rebel represents a user who refuses to follow any rules and believes that society
    should be broken down and restructured.
    They do not want to pursue "a standard education", "conform to the economic/capitalist foundations of society"
    or "get a job".
    Parents of these children are quite worried and turn to F.A.M. when they are out of options.
    
    - They get a warning for every transaction after exceeding 50% of a budget.
    - Gets ruthlessly notified iIf they exceed a budget category.
    - Gets locked out of conducting transactions in a budget category
      if they exceed it by 100% of the amount assigned to the budget in question.
    - If they exceed their budget in 2 or more categories then they get locked out of their account completely.
    """