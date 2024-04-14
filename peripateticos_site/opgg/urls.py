from django.urls import path
from  opgg  import views
from django.conf import settings 
from django.conf.urls.static import static 
# importing views from views..py


urlpatterns = [
    path('lista/',views.ListaAutores.as_view(),name='lista'),
    path('crear/',views.CrearAutorView.as_view(),name='crear'),
    path('modificar/<int:pk>/',views.ActualizarAutorView.as_view(),name='modificar'),
    path('autores/',views.ListaTodoAutores.as_view(),name='lista_autores'),
    path('eliminar/<int:pk>/',views.EliminarAutorView.as_view(),name='eliminar'),
    path('error',views.ErrorView.as_view(),name='error')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 