from django.urls import path

from . import views

app_name = 'propostas'
urlpatterns = [
    path('', views.list_propostas, name='index'),
    path('search/', views.search_propostas, name='search'),
    path('create/', views.create_propostas, name='create'),
    path('<int:propostas_id>/', views.detail_propostas, name='detail'),
    path('update/<int:propostas_id>/', views.update_propostas, name='update'),
    path('delete/<int:propostas_id>/', views.delete_propostas, name='delete'),
    path('empresa_profile/<username>', views.get_empresa_profile, name='empresa_profile'),
    path('inscrito/<int:id>', views.inscrito_add, name='inscrito_add'),
    path('<int:propostas_id>/inscritos', views.inscrito_list, name='inscrito_list'),
    path('inscricoes/<username>', views.propostas_inscrito_list, name='inscricoes'),
]