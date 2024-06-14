from django.db import models
from django.contrib.auth.hashers import check_password
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,User,UserManager,AbstractBaseUser
# Create your models here.
class Saller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='saller_profile')
    carte = models.CharField(('carte'), max_length=50)
    zipcode = models.CharField(('zipcode'), max_length=50)
    is_saller = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
def is_saller(self):
    return hasattr(self, 'saller_profile')
def is_costumer(self):
    return hasattr(self,'costumer_profile')
def hasorders(self):
    if(Order.objects.get(name_of_costumer=self.costumer)):
        return True
    else:
        return False
        
User.add_to_class('is_saller', is_saller)
User.add_to_class('is_costumer',is_costumer)
User.add_to_class('hasorders',hasorders)

class Product(models.Model):
    name=models.CharField( max_length=50)
    quantity=models.IntegerField()
    saller=models.ForeignKey(Saller, on_delete=models.CASCADE,default=None) 
    details=models.CharField(null=True, max_length=200)
    price=models.FloatField(null=True)
    image = models.ImageField(upload_to='product_images/')  # Define the image field
    def __str__(self):
            return self.name
    def buy(self,quantity):
        self.quantity=self.quantity-quantity
        self.save()
class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='costumer_profile')
    address=models.CharField( max_length=100)
    address2=models.CharField(blank=True, max_length=50)
    carte=models.CharField( max_length=50)
    zipcode=models.CharField( max_length=50)    
    def __str__(self):
            return self.user.username
    
        
class Order(models.Model):
    name_of_costumer=models.ForeignKey(Costumer, on_delete=models.CASCADE)  
    name_of_Product=models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity=models.IntegerField(default=1)
  # Assuming a related_name of 'saller' in ForeignKey

    