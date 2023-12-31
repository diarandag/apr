from django.contrib import admin
from django.urls import path
from django import views
from . import views
from .views import login_view

urlpatterns = [
    path('', views.inicio, name="inicio"),  
    path('index', views.index, name="index"),
    path('login', login_view, name='login'),
    path('login_rut', views.login_rut, name='login_rut'),
    path('lista', views.lista, name="lista"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar/<int:user_id>/', views.actualizar, name='actualizar'),
    path('eliminar/<int:user_id>/', views.eliminar, name='eliminar'),
    path('olista', views.listaop, name="listaop"),
    path('oagregar', views.agregarop, name="oagregar"),
    #path('oactualizar', views.actualizarop, name="oactualizar"),
    path('eliminarop/<str:email>/', views.eliminarop, name='eliminarop'),
    path('ingresos', views.ingresos, name="ingresos"),
    path('egresos', views.egresos, name="egresos"),
    path('saldo', views.saldo, name="saldo"),
    path('crear_notificacion', views.crear_notificacion, name='crear_notificacion'),
    path('centro_notificaciones', views.centro_notificaciones, name='centro_notificaciones'),
    path('crear_notificacioncli', views.crear_notificacioncli, name='crear_notificacioncli'),
    path('centro_notificacionescli', views.centro_notificacionescli, name='centro_notificacionescli'),
    path('eliminar_notificacion/<int:notificacion_id>/', views.eliminar_notificacion, name='eliminar_notificacion'),
    path('agregar_proveedor', views.agregar_proveedor, name='agregar_proveedor'),
    path('lista_proveedores', views.lista_proveedores, name='lista_proveedores'),
    path('eliminar_proveedor/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('agregar_tarifa', views.agregar_tarifa, name='agregar_tarifa'),
    path('lista_tarifas', views.lista_tarifas, name='lista_tarifas'),
    path('eliminar_tarifa/<int:tarifa_id>/', views.eliminar_tarifa, name='eliminar_tarifa'),
    path('generar_boleta_pdf/', views.generar_boleta_pdf, name='generar_boleta_pdf'),
    path('perfilcliente', views.perfilcliente, name='perfilcliente'),
    path('boleta', views.boleta, name='boleta'),
    path('pagina_de_pago/', views.pagina_de_pago, name='pagina_de_pago'),
    path('detalle_cliente/', views.detalle_cliente, name='detalle_cliente'),
    path('volver', views.volver, name='volver'),
    path('logout/', views.logout_view, name='logout'),
    path('crear_preferencia', views.crear_preferencia, name='crear_preferencia'),
    #path('mercadopago', views.mercadopago, name='mercadopago'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('agregar_consumo/<int:user_id>/', views.agregar_consumo, name='agregar_consumo')
]