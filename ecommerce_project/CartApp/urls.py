from django.urls import path
from .import views

app_name = 'CartApp'

urlpatterns = [
    path('add/<int:product_id>/',views.addCart,name='addCart'),
    path('', views.cartDetail,name='cartDetail'),
    path('remove/<int:product_id>/',views.cartRemove,name='cartRemove'),
    path('fullremove/<int:product_id>/',views.fullRemove,name='fullRemove'),

]