# Generated by Django 4.1.4 on 2023-01-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
