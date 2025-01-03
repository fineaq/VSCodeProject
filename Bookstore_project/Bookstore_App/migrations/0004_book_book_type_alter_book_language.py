# Generated by Django 5.1.4 on 2024-12-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore_App', '0003_genre_rename_pages_book_pages_book_publisher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('COMIC', 'Comic'), ('MAGAZINE', 'Magazine'), ('NOVEL', 'Novel'), ('TEXTBOOK', 'Textbook'), ('OTHER', 'Other')], default='OTHER', max_length=20, verbose_name='Type of Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('ENGLISH', 'English'), ('KOREAN', 'Korean'), ('INDONESIAN', 'Bahasa'), ('SPANISH', 'Spanish'), ('OTHER', 'Other')], default='OTHER', max_length=20),
        ),
    ]
