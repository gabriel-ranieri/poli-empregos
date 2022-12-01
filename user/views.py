from django.shortcuts import render
from django.shortcuts import redirect
from .models import Estudante, Empresa, User
from django.views.generic import CreateView
from .forms import EstudanteSignUpForm,EmpresaSignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth import login


def SignUp(request):
    return render(request,'register.html')

class EstudanteSignUpView(CreateView):
    model = User
    form_class = EstudanteSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'estudante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('login')

class EmpresaSignUpView(CreateView):
    model = User
    form_class = EmpresaSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'empresa'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('login')
