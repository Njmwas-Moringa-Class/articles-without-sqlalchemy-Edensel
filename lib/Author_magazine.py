# creating a many-many relationship between Author and Magazine based on the article they contribute.

class Contribution:
    _all_contributions = []

    def __init__(self, author, magazine):
        self._author = author
        self._magazine = magazine
        Contribution._all_contributions.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all_contributions
