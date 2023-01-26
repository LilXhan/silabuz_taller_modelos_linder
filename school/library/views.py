from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, ListView
from .models import Book
from .forms import InputForm
from .tasks import send_book, insert_books
from django.http import HttpResponse
# Proteger rutas 
from django.core.mail import send_mail
from django.conf import settings



from django.contrib.auth.mixins import LoginRequiredMixin

# Librerias para los querysets 

from django.db.models.functions import Length, ExtractYear
from django.db.models import Max, Min, Avg, StdDev, Q, Count

# Para poder consumir una api en django podemos usar urllib.request
import urllib.request
import json 

class BookListView(ListView):
    model = Book
    template_name = 'booklist.html'
    paginate_by = 20



class UpdateBook(UpdateView):
    model = Book
    fields = ['authors']
    template_name = 'editBook.html'

def select_view(request, id):
    book = Book.objects.get(pk=id)
    request.session['authors'] = book.authors
    request.session['id'] = book.id 

    context = {
        'book': book,
        'form': InputForm()
    }

    authors = book.authors

    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            send_book.delay(name, email)

            subject = 'Hi Flavio'
            message = f"Authors: {authors}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]

            send_mail(subject, message, email_from, recipient_list)

            return HttpResponse(f"{name} y {email}")

    return render(request, 'oneBook.html', context)



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
        insert_books.delay()     

        return HttpResponse('Ya se esta subiendo a la db')

