from django.db import models

class Book(models.Model):
    #  {
    #    "title": "Harry Potter and the Half-Blood Prince (Harry Potter  #6)",
    #    "authors": "J.K. Rowling/Mary GrandPré",
    #    "average_rating": "4.57",
    #    "isbn": "0439785960",
    #    "isbn13": "9780439785969",
    #    "language_code": "eng",
    #    "num_pages": "652",
    #    "ratings_count": 2095690,
    #    "text_reviews_count": 27591,
    #    "publication_date": "9/16/2006",
    #    "publisher": "Scholastic Inc.",
    #  }
        
    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=400)
    average_rating = models.FloatField(default=0.0)
    isbn = models.CharField(max_length=300)
    isbn13 = models.CharField(max_length=300)
    language_code = models.CharField(max_length=20)
    num_pages = models.IntegerField(default=0)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=400)
  
    class Meta:
        db_table = 'books'



    