# Generated by Django 4.2.2 on 2023-09-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Prodapp',
            field=models.TextField(default=''),
        ),
    ]
