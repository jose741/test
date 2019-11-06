from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login

from . import views
from .views import RegistroUsuario,VentasList,VentasCreate,VentasUpdate,VentasDelete

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.index, name = 'index'),
    path('home/perro/', views.indexPerro, name = 'indexPerro'),
    path('home/gato/', views.indexGato, name = 'indexGato'),
    path('home/cuy/', views.indexCuy, name = 'indexCuy'),
    path('home/crearCuenta/', RegistroUsuario.as_view(), name = 'crearCuenta'),
    path('home/contacto/', views.contacto, name = 'contacto'),
    path('home/iniciarSesion/', LoginView.as_view(template_name='iniciarSesion.html'), name = 'iniciarSesion'),
    path('home/cerrarSesion', logout_then_login, name = 'cerrarSesion'),
    path('home/listar', views.mascotas_list, name = 'listar'),
    path('home/compras', VentasList.as_view(template_name= 'ventas_list.html'), name = 'ventas_listar'),
    path('nueva', VentasCreate.as_view(template_name= 'ventas_crear.html'), name ='ventas_crear'),
    path('editar/(?P<pk>\d+)$',VentasUpdate.as_view(), name='ventas_editar'),
    path('home/eliminar/(?P<pk>\d+)$',VentasDelete.as_view(), name='ventas_delete'),
]
