from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView ,
    DeleteView   
)

from .models import Empleado


class InicioView(TemplateView):
    template_name = "inicio.html"


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Empleado
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'


#Listar todos los empleados dela empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


#Listar empleados por area de la empresa
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_area.html'
    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
        departamento__name = area
        )
        return lista

#Listar empleados por palabra clave
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

#Habilidades de empleados
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        """ palabra_clave = self.request.GET.get('kword', '') """
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()

#Ver el detalle de una persona
class EmpleadoDetailView(DetailView):
    model =Empleado
    template_name = 'persona/detail_empleado.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


#Crear un nuevo empleado
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)#detiene el guardado con el commit=false
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()#Ahora si guardamos en base de datos
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

