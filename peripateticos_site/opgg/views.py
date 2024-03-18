from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from opgg.models import Autores

# Create your views here.
class HomeView(TemplateView):
    template_name = 'autores.html'

    def get(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,self.template_name,context)
    
class ListaAutores(ListView):
    template_name = 'autores-lista.html'
    model = Autores

    def get_queryset(self):
        return Autores.objects.filter(visualizacion=True)
    
class ListaTodoAutores(ListView):
    template_name = 'todosautores.html'
    model = Autores

    def get_queryset(self):
        return Autores.objects.all().order_by('nombre')
        
class CrearAutorView(CreateView):
    template_name = 'crear-autor.html'
    model = Autores
    fields = ('__all__')
    success_url = '/lista'

class ActualizarAutorView(UpdateView):
    template_name = 'crear-autor.html'
    model = Autores
    fields = ('__all__')
    success_url = '/lista'

class EliminarAutorView(DeleteView):
    template_name = 'eliminar-autor.html'
    model =  Autores
    fields =('__all__')
    success_url = '/lista'

class ErrorView(TemplateView):
    template_name = 'error.html'

    def get(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        context = self.get_context_data()
        return render(request,self.template_name,context)


