from Author_magazine import Contribution

class Author:
    _all_authors = []

    def __init__(self, name):
        self._name = name
        self._contributions = []
        Author._all_authors.append(self)

    def name(self):
        return self._name

    def contributions(self):
        return self._contributions

    def magazines(self):
        return list(set(contribution.magazine for contribution in self._contributions))

    def add_contribution(self, magazine):
        contribution = Contribution(self, magazine)
        self._contributions.append(contribution)
        return contribution

    def topic_areas(self):
        return list(set(contribution.magazine.category() for contribution in self._contributions))

    @classmethod
    def all(cls):
        return cls._all_authors


