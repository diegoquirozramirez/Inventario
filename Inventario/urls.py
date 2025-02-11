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
from Apps.Exportar import views as exportar

from django.contrib.auth.views import login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    #Login
    path('', login, name="login"),    
    path('accounts/logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),

    #sprint 1
    path('home', views.home, name="home"),
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
    path('delete/<int:id>', inventario.deleteRegister, name="delete"),
    path('actualizar/<int:id>', inventario.editRegister, name="update"),
    path('actualizar-one/', inventario.updateOneRegister, name="update-one"),

    #sprint 3
    path('generar-ficha/', inventario.grabarGenerarFicha, name="generar-ficha"),
    path('buscar-ficha/', inventario.buscarFicha, name="buscar-ficha"),
    path('consultar-ficha/', inventario.consultarFicha, name="consultar-ficha"),
    path('update-ficha/', inventario.updateFicha, name="update-ficha"),
    path('delete-ficha/', inventario.deleteFicha, name="delete-ficha"),
    path('catalogo/', inventario.verCatalogo, name="verCatalogo"),
    path('delete-bien-ficha/<int:id>/', inventario.deleteBienFicha, name="delete-bien-ficha"),
    path('update-bien-ficha/<int:id>', inventario.updateBienFicha, name="update-bien-ficha"),
    path('catalogo/get-catalogo/', inventario.get_catalogos, name="get-catalogo"),
    path('standby-catalogo/', inventario.standByCatalogo, name="standby-catalogo"),
    path('ambiente/get-ambiente/', inventario.get_ambiente, name="get-ambiente"),
    path('ficha/get-ficha/', inventario.get_ficha, name="get-ficha"),
    path('usuario/get-usuario/', inventario.get_usuario, name="get-usuario"),

    path('exportar-hoja-pdf/', exportar.exportHojaPDF, name="exportar-hoja-pdf"),
    path('viewFicha', inventario.viewFicha, name="viewFicha"),
    path('viewFichaBienes', inventario.viewFichaBienes, name="viewFichaBienes"),
    path('direccioj/get-direccion/', inventario.get_direccion, name="get-direccion"),
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
