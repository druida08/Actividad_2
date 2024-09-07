from django.contrib import admin
from django.urls import path
from empleo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar-empresa/', views.registrar_empresa, name='registrar_empresa'),
    path('registrar-oferta/', views.registrar_oferta_empleo, name='registrar_oferta'),
    path('lista-empresas/', views.lista_empresas, name='lista_empresas'),
    path('lista-ofertas/', views.lista_ofertas, name='lista_ofertas'),
]
