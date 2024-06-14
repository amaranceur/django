from django.db import models

# Create your models here.
class sallers(models.Model):
    name=models.CharField( max_length=50)
    prename=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    carte=models.CharField( max_length=50)
    zipcode=models.CharField( max_length=50)
    class Meta:    
        def __str__(self):
            return self.name
class Product(models.Model):
    name=models.CharField( max_length=50)
    quantity=models.IntegerField()
    saller=models.ForeignKey(sallers, on_delete=models.PROTECT,default=None)
    class Meta:   
        def __str__(self):
            return self.name