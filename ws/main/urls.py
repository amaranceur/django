from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin_login', admin, name='admin'),
    path('logout/', logout_, name='logout'),
    path('managment/<str:a>/', managment, name='managment'),
    path('orders/', home, name='orders'),
    path('managment/<str:thing>/<int:pk>', detailes, name='details'),
    path('managment/<str:thing>/<int:pk>/delete', delete_, name='delete'),
    path('managment/AddCostumer',create_costumer,name='add_c'),
    path('managment/AddProduct',create_product,name='add_p'),
    path('managment/AddSaller',create_saller,name="add_s"),
    path('costumer_login',costumer_login,name="costumerlogin"),
    path('saller_login',saller_login,name="sallerlogin"),
    path('product/<int:pk>',product,name='product'),
    path('buy_product/<int:pk>',add_orders,name='addproduct')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)