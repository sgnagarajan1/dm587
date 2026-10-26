"""Completed classes for Questions 14-16."""

class Backpack:
    """A pack with an owner, colour, item capacity and independent contents."""

    def __init__(self, name, color, max_size = 5):
        """Store the owner, colour and capacity; start with no items."""
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Add item if capacity permits; otherwise print No Room!."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove an existing item, as in the starter class."""
        self.contents.remove(item)

    def dump(self):
        """Reset contents to an empty list."""
        self.contents = []

    def __add__(self, other):
        """Return the total item count of two packs (starter method)."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare item counts (starter method)."""
        return len(self.contents) < len(other.contents)

    def __eq__(self, other):
        """Compare name, colour and item count, as specified."""
        if not isinstance(other, Backpack):
            return NotImplemented
        return (self.name == other.name and self.color == other.color
                and len(self.contents) == len(other.contents))

    def __str__(self):
        """Return the requested multiline description."""
        return ('<<Owner:\t{0}\nColor:\t\t{1}\nSize:\t\t{2}\nMax Size:\t{3}\nContents:\t{4}>>'.format(self.name, self.color, len(self.contents), self.max_size, self.contents))


class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """

    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum((len(str(item)) for item in self.contents))

class Jetpack(Backpack):
    """A backpack with a fuel supply used for flying."""
    def __init__(self, name, color, max_size = 2, fuel = 10):
        """Initialise the inherited pack attributes and fuel balance."""
        super().__init__(name, color, max_size)
        self.fuel = fuel

    def fly(self, amount):
        """Burn a non-negative amount of fuel if enough remains."""
        if amount > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= amount

    def dump(self):
        """Empty both contents and fuel."""
        super().dump()
        self.fuel = 0

