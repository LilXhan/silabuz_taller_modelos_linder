from django.shortcuts import render
from django.views import View
from .models import Book
# Para poder consumir una api en django podemos usar urllib.request
import urllib.request
import json 
import datetime

class LibraryQuery(View):

    def get(self, request):

        # Filtre los libros publicados después del 2007.

        books_after_2007 = Book.objects.filter(publication_date__lte='2007-1-1')

        print(len(list(books_after_2007)))

        return render(request, 'querys.html')


class Library(View):

    def get(self, request):
        
        url_api = 'https://silabuzinc.github.io/books/books.json'

        response = urllib.request.urlopen(url_api)

        # books => lista de objetos o diccionarios
        books = json.loads(response.read())

        for book in books:
            book.pop('bookID')
            book.pop('FIELD13')

            # change time 
            book['publication_date'] = book['publication_date'].rsplit('/')

            if len(book['publication_date']) == 3:
                date = ''
                date += book['publication_date'][2] + '-'
                date += book['publication_date'][0] + '-'
                date += book['publication_date'][1]
            else:
                date = '2023-01-13'
            
            book['publication_date'] = date

            try:
                book['num_pages'] = int(book['num_pages'])
            except:
                book['num_pages'] = 0
                
            try:
                book['average_rating'] = float(book['average_rating'])
            except:
                book['average_rating'] = 0

            book['authors'] = book['authors'][:400]

            b = Book.objects.create(**book)
            b.save()


        return render(request, 'index.html')