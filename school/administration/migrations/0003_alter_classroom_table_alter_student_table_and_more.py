# Generated by Django 4.1.4 on 2023-01-03 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_alter_classroom_table_alter_student_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classroom',
            table='classrooms',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teachers',
        ),
    ]
