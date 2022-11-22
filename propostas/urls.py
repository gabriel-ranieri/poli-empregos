from django.urls import path

from . import views

app_name = 'propostas'
urlpatterns = [
    path('', views.list_propostas, name='index'),
    path('search/', views.search_propostas, name='search'),
    path('create/', views.create_propostas, name='create'),
    path('<int:propostas_id>/', views.detail_propostas, name='detail'),
]