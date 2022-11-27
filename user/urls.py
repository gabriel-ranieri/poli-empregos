from django.urls import path
from .views import *

urlpatterns = [
    #path('registration', registration,name='registration'),
    path('/signup/',SignUp,name='signup'),
    path('/signup/estudante', EstudanteSignUpView.as_view(), name='estudante_signup'),
    path('/signup/empresa', EmpresaSignUpView.as_view(), name='empresa_signup'),
]