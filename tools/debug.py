#!/usr/bin/env python3
import sys
sys.path.append('lib')  # Assuming 'lib' is one level above 'tools'

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
    
    #create an author instance
    author = Author("Densel Esekon")
    
    #create author and magazine instances
    author = Author("Densel Esekon")
    magazine = Magazine("Spice FM", "Royal Media")

    # Add an article to the author
    article = author.add_article(magazine, "Spice FM")

    # Check if articles() method returns the list of articles
    author.articles() == [article]

    # Check if magazines() method returns the correct list of magazines
    author.magazines() == [magazine]

    # Check if topic_areas() method returns the correct list of categories
    author.topic_areas() == ["Politic"]

    # Create Author and Magazine instances
    author = Author("Densel Esekon")
    magazine = Magazine("Spice FM", "Royal Media")

    # Add an article to the magazine
    article = magazine.add_article(author, "The Future of AI")

    # Check if contributors() method returns the correct list of authors
    magazine.contributors() == [author]

    # Check if article_titles() method returns the correct list of article titles
    magazine.article_titles() == ["The Future of AI"]

    # Check if contributing_authors() method returns the correct list of authors
    magazine.contributing_authors() == [author]
    # Create Author and Magazine instances
    author = Author("John Doe")
    magazine = Magazine("Tech Weekly", "Technology")

    # Create an Article instance
    article = Article(author, magazine, "The Future of AI")

    # Check if title() method returns the correct title
    article.title() == "The Future of AI"

    # Check if author() method returns the correct author
    article.author() == author

    # Check if magazine() method returns the correct magazine
    article.magazine() == magazine

    # Check if all() method returns all article instances
    Article.all() == [article]


    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()
