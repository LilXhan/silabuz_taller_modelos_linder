# Generated by Django 4.1.4 on 2023-01-03 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_classroom_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProxy',
            fields=[
            ],
            options={
                'ordering': ['-id'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administration.student',),
        ),
    ]
