from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ecommerce_app'

urlpatterns = [
    path('', views.allProduct_catagory, name='allProductCat'),
    path('<slug:c_slug>/', views.allProduct_catagory, name='product_by_catagory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name='ProCatDetail'),

]
