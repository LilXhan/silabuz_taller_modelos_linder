# Generated by Django 4.1.4 on 2023-01-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('authors', models.CharField(max_length=400)),
                ('average_rating', models.FloatField(default=0.0)),
                ('isbn', models.CharField(max_length=300)),
                ('isbn13', models.CharField(max_length=300)),
                ('language_code', models.CharField(max_length=20)),
                ('num_pages', models.IntegerField(default=0)),
                ('ratings_count', models.IntegerField(default=0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('publication_date', models.DateField(auto_now=True)),
                ('publisher', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
