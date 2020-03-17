# Generated by Django 2.2 on 2020-03-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_authors_app.Author'),
            preserve_default=False,
        ),
    ]