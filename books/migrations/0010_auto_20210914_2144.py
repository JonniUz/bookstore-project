# Generated by Django 3.2.7 on 2021-09-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='thumbnailUrl',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/review'),
        ),
    ]
