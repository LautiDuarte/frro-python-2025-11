from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from apps.usuarios.forms import CustomUserCreationForm

def mapa(request):
    return render(request, "mapa.html")


class SignUpView(generic.CreateView):
    # ¡Ahora usa el formulario personalizado!
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'