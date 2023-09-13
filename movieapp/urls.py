from django.urls import path, include
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('save_movie/',views.save_movie,name='save_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
