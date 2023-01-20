from django.shortcuts import render
from django.views import View
from .models import Book

# Proteger rutas 

from django.contrib.auth.mixins import LoginRequiredMixin

# Librerias para los querysets 

from django.db.models.functions import Length, ExtractYear
from django.db.models import Max, Min, Avg, StdDev, Q, Count

# Para poder consumir una api en django podemos usar urllib.request
import urllib.request
import json 

class LibraryQuery(LoginRequiredMixin,View):

    def get(self, request):

        # 1) Filtre los libros publicados después del 2007.

        books_after_2007 = Book.objects.filter(publication_date__gte='2007-1-1').values()

        # 2) Contabilice el total de libros publicados después del 2007 por año.

        books_count = Book.objects.filter(publication_date__year__gte=2007).values().annotate(year=ExtractYear('publication_date')).values('year').annotate(count=Count('id'))


        # 3) Filtre los tipos de libros cuyo ratings estén entre 3.5 y 4.2

        books_rating = Book.objects.filter(average_rating__range=(3.5, 4.2)).values()

        # 4) Muestre los libros cuyos títulos en longitud estén en el top 20.

        book_title_top_20 = Book.objects.order_by(Length('title')).values()
        book_title_top_20 = book_title_top_20[::-1][:20]

        # 5) Del punto anterior, respecto al rating del libro indicar el valor menor, el mayor valor, 
        # el promedio así como la desviación estándar.

        min_value_rating = Book.objects.aggregate(Min('average_rating'))
        max_value_rating = Book.objects.aggregate(Max('average_rating'))
        avg_rating = Book.objects.aggregate(Avg('average_rating'))
        standard_deviation_rating = Book.objects.aggregate(StdDev('average_rating'))

        # 6) Filtre libros con número dé páginas mayores a 400 y con rating mayor a 3.9. 
        # Presente el resultado ordenado alfabéticamente por el título.

        books_filter = Book.objects.filter(Q(num_pages__gte=400) & Q(average_rating__gte=3.9)).order_by('title').values()

        # 7) Ordernar los libros descendentemente por el número de páginas y el isbn.

        books_order = Book.objects.order_by('num_pages').order_by('isbn').values()

        # 8) Listar los libros cuya editora (publisher) contenga la palabra "Books" o "'Audio".

        books_publisher = Book.objects.filter(Q(publisher__icontains='Books') | Q(publisher__icontains='Audio')).values()

        # 9) Filtrar los libros con rating menor a 3.5, excluyendo a los que pertenezcan a las 
        # siguientes editoras Vintage, Cambridge University Press y Cambridge University Press. 
        # Ordenar el resultado descendentemente por número de reseñas (text_reviews_count).

        exclude_books = Book.objects.exclude(average_rating__gte=3.5).exclude(publisher='Cambridge University Press').exclude(publisher='Vintage').order_by('-text_reviews_count').values()

        # 10) Mostrar todos los libros publicados entre los meses de Mayo a Agosto, 
        # Ordenarlos descendentemente por el rating.

        books_may_august = Book.objects.filter(Q(publication_date__month='4') | Q(publication_date__month='5') | Q(publication_date__month='6') | Q(publication_date__month='7') | Q(publication_date__month='8')).order_by('-average_rating').values()


        return render(request, 'querys.html')


class Library(LoginRequiredMixin, View):

    def get(self, request):
        
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


        return render(request, 'index.html')