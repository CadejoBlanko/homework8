import json
import os

from mongoengine import connect
from models import Author, Quote


def load_authors():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    authors_file = os.path.join(current_dir, 'authors.json')
    with open(authors_file, 'r') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            Author(**author_data).save()


def load_quotes():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    quotes_file = os.path.join(current_dir, 'quotes.json')
    with open(quotes_file, 'r') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data.pop('author') 
            author = Author.objects(fullname=author_name).first()
            if not author:  
                author = Author(fullname=author_name).save()
            quote_data['author'] = author  
            Quote(**quote_data).save()


if __name__ == '__main__':
    connect('HomeWork08', host='mongodb+srv://Cadejo:0aGnluXd4Y56CviJ@homework08.lgshiv5.mongodb.net/?retryWrites=true&w=majority')
    load_authors()
    load_quotes()