from django.urls import path
from  opgg  import views
from django.conf import settings 
from django.conf.urls.static import static 
# importing views from views..py


urlpatterns = [
    path('',views.HomeView.as_view()),
    path('lista',views.ListaAutores.as_view()),
    path('crear',views.CrearAutorView.as_view()),
    path('modificar/<int:pk>/',views.ActualizarAutorView.as_view()),
    path('todosautores',views.ListaTodoAutores.as_view()),
    path('eliminar/<int:pk>/',views.EliminarAutorView.as_view())

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
