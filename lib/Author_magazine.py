class Contribution:
    _all_contributions = []

    def __init__(self, author, magazine, article):
        self._author = author
        self._magazine = magazine
        self._article = article  # Add the article attribute
        Contribution._all_contributions.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def article(self):
        return self._article

    @classmethod
    def all(cls):
        return cls._all_contributions
