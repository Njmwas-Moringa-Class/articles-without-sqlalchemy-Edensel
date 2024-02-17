from Author_magazine import Contribution

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributions = []
        Magazine._all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def add_contribution(self, author, article):
        contribution = Contribution(author, self, article)
        self._contributions.append(contribution)
        return contribution

    def contributors(self):
        return [contribution.author for contribution in self._contributions]

    def article_titles(self):
        return [contribution.article.title() for contribution in self._contributions]

    def contributing_authors(self):
        return [author for author in self.contributors() if len(author.articles()) > 2]

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all_magazines if magazine.name() == name), None)

    @classmethod
    def all(cls):
        return cls._all_magazines
