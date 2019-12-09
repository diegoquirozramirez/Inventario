"""Inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Apps import views
from Apps.Inventario import views as inventario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('MIMP/registrar-usuario', inventario.registraUsuario, name="registar-usuario"),
    path('MIMP/consultar/<int:idu>', inventario.cabecera, name="consultar"),
    path('MIMP/asignar-ambiente/<int:idu>', inventario.asignarCodAmbiente, name="asignar-ambiente"),
    path('MIMP/actualizar-ambiente/<int:idu>/<int:ida>', inventario.updateAsignarCodAmbiente, name="actualizar-ambiente"),
    path('MIMP/listado-usuario', inventario.listadoUsuario, name="listado-usuario"),
    path('MIMP/base0/', inventario.base0Consulta, name="base0-consultar"),
    #path('MIMP/register-base2019/<int:idbase0>/<int:idu>/<str:cod>/sbn', inventario.addBase12019sbn, name="addBase12019sbn"),
    path('MIMP/register-base2019/<int:idbase0>/<int:idu>/<str:cod>/cint', inventario.addBase12019cint, name="addBase12019cint"),

    #sprint 2
    path('MIMP/buscar-usuario', inventario.buscarUsuario, name="buscar-usuario"),
    path('MIMP/register-base2019/', inventario.addBase12019sbn, name="addBase12019sbn"),
    path('MIMP/register-base2019/capture', inventario.captureBase0, name="capture-base0"),
    path('delete/<int:id>', inventario.deleteRegister, name="delete")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
