# Generated by Django 4.2.2 on 2023-08-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='male',
            name='girls',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rlt',
        ),
        migrations.RemoveField(
            model_name='users',
            name='products',
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Female',
        ),
        migrations.DeleteModel(
            name='Male',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='users',
        ),
        migrations.DeleteModel(
            name='video',
        ),
    ]
