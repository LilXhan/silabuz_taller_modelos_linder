from celery import shared_task
import time
from .models import Book

import json 
import urllib.request

@shared_task
def send_book(name, email):
    time.sleep(20)
    print(name, email)


@shared_task
def insert_books():
    
    url_api = 'https://silabuzinc.github.io/books/books.json'

    response = urllib.request.urlopen(url_api)

        # books => lista de objetos o diccionarios
    books = json.loads(response.read())
    for book in books:
        book.pop('bookID')
        book.pop('FIELD13')

        try:
            book['num_pages'] = int(book['num_pages'])
        except:
            book['num_pages'] = 0
                    
        try:
            book['average_rating'] = float(book['average_rating'])
        except:
            book['average_rating'] = 0

        book['authors'] = book['authors'][:400]

        # change time 

        condition = book['publication_date']

        if condition == '11/31/2000' or condition == '6/31/1982':
            date = '2023-1-13'
            book['publication_date'] = date
            b = Book.objects.create(**book)
            b.save()
            continue

        book['publication_date'] = book['publication_date'].split('/')

        if len(book['publication_date']) == 3:
            date = ''
            date += book['publication_date'][2] + '-'
            date += book['publication_date'][0] + '-'
            date += book['publication_date'][1]
        else:
            date = '2023-1-13'
            
        book['publication_date'] = date

        b = Book.objects.create(**book)
        b.save()