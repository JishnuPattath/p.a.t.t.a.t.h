
from django.urls import path
from . import views

app_name = 'christopher'

urlpatterns = [
    path('',views.webpage,name='webpage'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('addmovie',views.addMovie,name='addMovie'),
    path('update/<int:id>/',views.update_movie,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
