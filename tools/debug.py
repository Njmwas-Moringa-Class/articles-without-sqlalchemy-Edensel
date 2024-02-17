#!/usr/bin/env python3
import sys
sys.path.append('lib')  # Assuming 'lib' is one level above 'tools'

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    author1 = Author("Alice Smith")
    author2 = Author("Bob Johnson")
    author3 = Author("Charlie Brown")

    magazine1 = Magazine("Science Today", "Science")
    magazine2 = Magazine("World News", "Current Affairs")

    article1 = author1.add_article(magazine1, "Exploring the Cosmos")
    article2 = author2.add_article(magazine1, "The Future of Space Travel")
    article3 = author2.add_article(magazine2, "Global Politics in 21st Century")
    article4 = author3.add_article(magazine2, "Climate Change: A Global Challenge")

    # Testing
    assert author1.articles() == [article1]
    assert author1.magazines() == [magazine1]
    assert author1.topic_areas() == ["Science"]

    assert author2.articles() == [article2, article3]
    assert author2.magazines() == [magazine1, magazine2]
    assert author2.topic_areas() == ["Science", "Current Affairs"]

    assert author3.articles() == [article4]
    assert author3.magazines() == [magazine2]
    assert author3.topic_areas() == ["Current Affairs"]

    assert magazine1.contributors() == [author1, author2]
    assert magazine1.article_titles() == ["Exploring the Cosmos", "The Future of Space Travel"]
    assert magazine1.contributing_authors() == [author1, author2]

    assert magazine2.contributors() == [author2, author3]
    assert magazine2.article_titles() == ["Global Politics in 21st Century", "Climate Change: A Global Challenge"]
    assert magazine2.contributing_authors() == [author2, author3]

    assert article1.title() == "Exploring the Cosmos"
    assert article1.author() == author1
    assert article1.magazine() == magazine1

    assert article2.title() == "The Future of Space Travel"
    assert article2.author() == author2
    assert article2.magazine() == magazine1

    assert article3.title() == "Global Politics in 21st Century"
    assert article3.author() == author2
    assert article3.magazine() == magazine2

    assert article4.title() == "Climate Change: A Global Challenge"
    assert article4.author() == author3
    assert article4.magazine() == magazine2

    assert Article.all() == [article1, article2, article3, article4]

    # Print information
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # Enter debugging mode
    ipdb.set_trace()
