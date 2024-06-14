from django.db import models
from django import forms
from django.contrib.auth.models import User  


# Create your models here.



CATEGORY_CHOISES=(
    ('CR','CURD'),
    ('ML','MILK'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discription=models.TextField()
    composiiton=models.TextField(default='')
    Prodapp=models.TextField(default='')

    category=models.CharField(choices=CATEGORY_CHOISES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='users/default_user.png', upload_to='users', blank=True, null=True)