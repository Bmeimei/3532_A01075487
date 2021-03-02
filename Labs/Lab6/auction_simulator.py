"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        if not isinstance(bidder, Bidder):
            print("Register Failed")
            return None
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        if not self.bidders:
            print("Currently No bidders!")
            return None
        for bidder in self.bidders:
            bidder.__call__(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if str(bidder) != "Starting Bid":
            print("%s bidded %f in response to %s's bid of %f" %
                  (str(bidder), bid, self._highest_bidder, self._highest_bid))
            bidder.highest_bid = bid
        self._highest_bid = bid
        self.highest_bidder = bidder
        self._notify_bidders()

    def print_highest_bid(self) -> None:
        print("Highest Bids Per Bidder")
        bidder_dict = {bidder: bidder.highest_bid for bidder in self.bidders}
        for bidder, highest in sorted(bidder_dict.items(), key=lambda x: x[1], reverse=True):
            print("Bidder: %s   Highest Bid: %f" % (str(bidder), highest))

    @property
    def highest_bid(self):
        """
        Gets the highest bid.
        """
        return self._highest_bid

    @property
    def highest_bidder(self):
        """
        Gets the current highest bidder.
        """
        return self._highest_bidder

    @highest_bidder.setter
    def highest_bidder(self, new_bidder) -> None:
        """
        Sets the new bidder as the highest bidder.
        """
        self._highest_bidder = new_bidder


class Bidder:

    def __init__(self, name: str, budget=0, bid_probability=0.35, bid_increase_perc=1.1):
        if not 0 < bid_probability < 1:
            bid_probability = 0.35
        if not bid_increase_perc <= 1:
            bid_increase_perc = 1.1
        if budget < 0:
            budget = 0
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer: Auctioneer):
        highest_bidder = auctioneer.highest_bidder
        if self != highest_bidder:
            highest_bid = auctioneer.highest_bid
            if self.budget >= highest_bid and random.random() < self.bid_probability:
                highest_bid *= self.bid_increase_perc
                # All In!
                if highest_bid >= self.budget:
                    highest_bid = self.budget
                auctioneer.accept_bid(highest_bid, self)

    def __str__(self) -> str:
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._auctioneer = Auctioneer()
        for bidder in bidders:
            self._auctioneer.register_bidder(bidder)

    def simulate_auction(self, item: str, start_price: float):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print("Auctioning %s starting at %f" % (item, start_price))
        start_bidder = Bidder("Starting Bid")
        self._auctioneer.accept_bid(start_price, start_bidder)
        print("\n"
              "------------------------------------------------\n"
              "The winner of the auction is: %s at %f" %
              (self._auctioneer.highest_bidder, self._auctioneer.highest_bid))
        self._auctioneer.print_highest_bid()


def main():
    bidders = [Bidder("Jojo", 3000, random.random(), 1.2), Bidder("Melissa", 7000, random.random(), 1.5),
               Bidder("Priya", 15000, random.random(), 1.1), Bidder("Kewei", 800, random.random(), 1.9),
               Bidder("Scott", 4000, random.random(), 2)]

    # Hardcoding the bidders.

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)


if __name__ == '__main__':
    main()
