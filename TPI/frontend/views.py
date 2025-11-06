from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from apps.usuarios.forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.incidentes.forms import ReporteIncidenteForm # Importa el formulario

@login_required
def mapa(request):
    return render(request, "mapa.html")


class SignUpView(generic.CreateView):
    # ¡Ahora usa el formulario personalizado!
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required # Solo permite acceso si el operario está logueado
def mapa(request):
    # Si el método es POST, el formulario fue enviado
    if request.method == 'POST':
        form = ReporteIncidenteForm(request.POST)
        
        if form.is_valid():
            # 1. Guardar el incidente (pero no lo comiteamos a la DB todavía)
            incidente = form.save(commit=False)
            
            # 2. Asignar campos que el usuario NO llenó (como el que reporta)
            #    Asumo que el modelo Incidente tiene un campo 'reporta' relacionado a Usuario
            #    y campos por defecto para 'estado' y 'fechaHora'
            incidente.reporta = request.user 
            incidente.estado = 'PENDIENTE' # Estado inicial por defecto
            incidente.save() # Ahora sí, guardar en la base de datos
            
            # Redirigir de vuelta al mapa
            return redirect('mapa') 
            
    # Si el método es GET (o el POST fue inválido), mostramos la página con el formulario vacío
    else:
        form = ReporteIncidenteForm()

    context = {
        'form': form,
    }
    return render(request, 'mapa.html', context)