from django.urls import path

from . import views

app_name = 'curriculo'

urlpatterns = [
    path('list', views.CurriculoListView.as_view(), name='list'),
    path('user_profile/<username>', views.get_user_profile, name='user_profile'),
    path('profile/<int:curriculo_id>/', views.curriculo_detail, name='profile'),
    path('update/<int:curriculo_id>/', views.update_curriculo, name='update'),
    path('search/', views.search_curriculo, name='search'),
]