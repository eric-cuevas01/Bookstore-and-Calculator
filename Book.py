class Book:
    """
    Class: Book contains the detail of the books. It allows comparing
    two instances according to the title.
    for example b1 < b2 if b1.title.lower() < b2.title.lower()
    """

    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank)
        self.similar = similar

    def __lt__(self, other):
        """
        This function allows to make direct comparation using the operator <
        """
        return self.title.lower() < other.title.lower()

    def __gt__(self, other):
        """
        This function allows to make direct comparation using the operator >
        """
        return self.title.lower() > other.title.lower()

    def __le__(self, other):
        """
        This function allows to make direct comparation using the operator <=
        """
        return self.title.lower() <= other.title.lower()

    def __ge__(self, other):
        """
        This function allows to make direct comparation using the operator >=
        """
        return self.title.lower() >= other.title.lower()

    def __eq__(self, other):
        """
        This function allows to make direct comparation using the operator ==
        """
        return self.title.lower() == other.title.lower() and self.key == other.key
