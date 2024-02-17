import sys
sys.path.append('lib')

from Author import Author
from Magazine import Magazine
from Article import Article
from Author_magazine import Contribution


if __name__ == '__main__':
    # Creating sample instances
    author1 = Author("Alice Smith")
    author2 = Author("Bob Johnson")
    author3 = Author("Charlie Brown")

    magazine1 = Magazine("Science Today", "Science")
    magazine2 = Magazine("World News", "Current Affairs")

    article1 = Article(author1, magazine1, "Exploring the Cosmos")
    article2 = Article(author2, magazine1, "The Future of Space Travel")
    article3 = Article(author2, magazine2, "Global Politics in 21st Century")

    # Adding contributions
    contribution1 = author1.add_contribution(magazine1, article1)
    contribution2 = author2.add_contribution(magazine1, article2)
    contribution3 = author2.add_contribution(magazine2, article3)

    # Testing functionalities
    print("Author 1 name:", author1.name())
    print("Author 2 name:", author2.name())
    print("Author 3 name:", author3.name())

    print("Magazine 1 name:", magazine1.name())
    print("Magazine 1 category:", magazine1.category())
    print("Magazine 2 name:", magazine2.name())
    print("Magazine 2 category:", magazine2.category())

    print("Article 1 title:", article1.title())
    print("Article 1 author:", article1.author().name())
    print("Article 1 magazine:", article1.magazine().name())

    print("All articles:", [article.title() for article in Article.all()])
    print("All magazines:", [magazine.name() for magazine in Magazine.all()])
    print("All contributions:", [(contribution.author.name(), contribution.magazine.name()) for contribution in Contribution.all()])

    print("Author 1 articles:", [article.title() for article in author1.articles()])
    print("Author 2 articles:", [article.title() for article in author2.articles()])
    print("Author 3 articles:", [article.title() for article in author3.articles()])

    print("Author 1 magazines:", [magazine.name() for magazine in author1.magazines()])
    print("Author 2 magazines:", [magazine.name() for magazine in author2.magazines()])
    print("Author 3 magazines:", [magazine.name() for magazine in author3.magazines()])

    print("Magazine 1 contributors:", [author.name() for author in magazine1.contributors()])
    print("Magazine 2 contributors:", [author.name() for author in magazine2.contributors()])

    print("Debugging completed successfully.")
