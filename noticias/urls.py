from django.urls import path

from . import views

app_name = 'noticias'
urlpatterns = [
    path('', views.list_noticias, name='index'),
    path('search/', views.search_noticias, name='search'),
    path('create/', views.create_noticia, name='create'),
    path('<int:noticia_id>/', views.detail_noticia, name='detail'),
    path('update/<int:noticia_id>/', views.update_noticia, name='update'),
    path('delete/<int:noticia_id>/', views.delete_noticia, name='delete'),
]