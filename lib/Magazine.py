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

    def all():
        return Magazine._all_magazines

    def contributors(self):
        return list(set(contribution.author for contribution in self._contributions))

    def add_contribution(self, author):
        contribution = Contribution(author, self)
        self._contributions.append(contribution)
        return contribution

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all_magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls._all_magazines for article in magazine._articles]

    @classmethod
    def contributing_authors(cls):
        return [author for magazine in cls._all_magazines for author in magazine.contributors() if len(author.articles()) > 2]
