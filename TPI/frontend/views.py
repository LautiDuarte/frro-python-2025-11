from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from apps.incidentes.services import finalizar_asignacion
from apps.usuarios.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from apps.incidentes.forms import ReporteIncidenteForm
from django.contrib import messages
from apps.incidentes.models import Incidente
from apps.recursos.models import Recurso



# Vista de registro usando el formulario personalizado
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def index(request):
    """
    Router principal después del login. Decide a dónde enviar al usuario según su rol.
    """
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    
    rol_usuario = request.user.rol.lower()


    # Si es USUARIO (Hospital), lo enviamos a la vista que solo muestra la tabla.
    if rol_usuario == 'usuario':
        return redirect('incidentes_asignados') 

    # Si es OPERADOR, lo enviamos a la vista que gestiona el mapa.
    if rol_usuario == 'operador':
        return redirect('mapa')
        
    # Si el rol no es ninguno de los anteriores
    messages.error(request, "No tienes permisos para acceder a esta página.")
    return redirect('logout')


@login_required 
def mapa(request):
    """
    Vista que maneja la lógica del mapa (Operador).
    """
    rol_usuario = request.user.rol.lower()
    
    if rol_usuario != 'operador':
        return redirect('index')

    # 1. Manejar el reporte de incidente (POST)
    if request.method == 'POST':
        form = ReporteIncidenteForm(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.reporta = request.user 
            incidente.estado = 'PENDIENTE' 
            incidente.save() 
            messages.success(request, "¡Incidente reportado con éxito!")
            return redirect('mapa') 
        else:
            # Si el formulario no es válido, lo volvemos a mostrar con errores
            context = {
                'rol': rol_usuario,
                'form': form,
                'incidentes_mapa': Incidente.objects.all()
            }
            return render(request, 'mapa.html', context)
    else:
        form = ReporteIncidenteForm()

    # 2. Mostrar la página (GET)
    context = {
        'rol': rol_usuario,
        'form': form,
        'incidentes_mapa': Incidente.objects.all() # El operador ve todos los incidentes
    }
    return render(request, 'mapa.html', context)

# En frontend/views.py



# ... (AQUÍ VAN TUS OTRAS VISTAS: SignUpView, index, mapa) ...


@login_required
def incidentes_asignados(request):
    """
    Vista exclusiva para el rol 'usuario' (Hospital/Institucion).
    Muestra los RECURSOS de su institución y los INCIDENTES asignados a esos recursos.
    """
    if request.user.rol.lower() != 'usuario':
        messages.error(request, "Acceso no autorizado.")
        return redirect('logout')
        
    # 1. Obtener la institución del usuario (Hospital)
    institucion_del_usuario = getattr(request.user, 'institucion_asignada', None)
    if not institucion_del_usuario:
        messages.error(request, "Tu usuario no tiene una institución asignada.")
        return redirect('logout')
    
    if request.method == 'POST':
        nuevo_recurso = Recurso(
            institucion_base=institucion_del_usuario,
            estado='DISPONIBLE'
        )
        nuevo_recurso.save()
        messages.success(request, f"🚑 Recurso #{nuevo_recurso.id} creado con éxito.")
        return redirect('incidentes_asignados')
    elif 'eliminar_recurso' in request.GET:
        recurso_id = request.GET.get('eliminar_recurso')
        recurso = get_object_or_404(Recurso, id=recurso_id, institucion_base=institucion_del_usuario)
        recurso.delete()
        messages.success(request, "🗑️ Recurso eliminado correctamente.")
        return redirect('incidentes_asignados')
    elif 'finalizar_incidente' in request.GET:
        incidente_id = request.GET.get('finalizar_incidente')
        ok, msg = finalizar_asignacion(incidente_id)
        if ok:
            messages.success(request, f"✅ {msg}")
        else:
            messages.error(request, f"❌ {msg}")
        return redirect('incidentes_asignados')


    # Inicializar QuerySets vacíos
    recursos_de_la_institucion = Recurso.objects.none()
    incidentes_asignados = Incidente.objects.none()
    institucion_nombre_str = "Sin Institución Asignada"

    if institucion_del_usuario:
        institucion_nombre_str = institucion_del_usuario.nombre
        
        # 2. (Requerimiento 1) Obtener todos los RECURSOS (ambulancias)
        recursos_de_la_institucion = Recurso.objects.filter(
            institucion_base=institucion_del_usuario
        ).order_by('estado') # Ordenar por estado
        
        # 3. (Requerimiento 2) Obtener los INCIDENTES asignados a ESOS recursos
        try:
            # Usamos el related_name "asignaciones" que definiste en el modelo Asignacion
            incidentes_asignados = Incidente.objects.filter(
                asignaciones__recurso__institucion_base=institucion_del_usuario,
                estado__in=['ASIGNADO', 'PENDIENTE', 'ACTIVO'] # Estados relevantes
            ).distinct().order_by('-fecha_hora') # Ordenar por más reciente
            
        except Exception as e:
             messages.error(request, f"Error crítico al consultar la base de datos: {e}")
    
    context = {
        'rol': request.user.rol.lower(),
        'institucion_nombre': institucion_nombre_str,
        'recursos_asignados': recursos_de_la_institucion, # Lista de Recursos
        'incidentes_asignados': incidentes_asignados, # Lista de Incidentes
    }
    
    return render(request, 'usuario_incidentes.html', context)

