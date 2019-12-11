from django.contrib import admin
from Apps.Inventario.models import ambiente,color,departamento,direccionGerencia,distrito,edificio,estado,etiquetado,ficha,jefeUsuario,marca,modalidad,oficina,operatividad,piso,provincia,recurso,sector,sede,situacion,suboficina,tipoDoc,Usuario
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from Apps.Inventario import models
# Register your models here.
class ambienteResource(resources.ModelResource):
    class Meta:
        model = ambiente

class ambienteAdmin(ImportExportModelAdmin):
    resources_class = ambienteResource
admin.site.register(ambiente, ambienteAdmin)
#admin.site.register(cabecera)
class colorResource(resources.ModelResource):
    class Meta:
        model = color

class colorAdmin(ImportExportModelAdmin):
    resources_class = colorResource
admin.site.register(color, colorAdmin)

class departamentoResource(resources.ModelResource):
    class Meta:
        model = departamento

class departamentoAdmin(ImportExportModelAdmin):
    resources_class = departamentoResource
admin.site.register(departamento, departamentoAdmin)

class direccionGerenciaResource(resources.ModelResource):
    class Meta:
        model = direccionGerencia

class direccionGerenciaAdmin(ImportExportModelAdmin):
    resources_class = direccionGerenciaResource
admin.site.register(direccionGerencia, direccionGerenciaAdmin)

class distritoResource(resources.ModelResource):
    class Meta:
        model = distrito

class distritoAdmin(ImportExportModelAdmin):
    resources_class = distritoResource

admin.site.register(distrito, distritoAdmin)

class estadoResource(resources.ModelResource):
    class Meta:
        model = estado

class estadoAdmin(ImportExportModelAdmin):
    resources_class = departamentoResource
admin.site.register(estado, estadoAdmin)

admin.site.register(etiquetado)
admin.site.register(ficha)
admin.site.register(jefeUsuario)

class marcaResource(resources.ModelResource):
    class Meta:
        model = marca

class marcaAdmin(ImportExportModelAdmin):
    resources_class = marcaResource
admin.site.register(marca, marcaAdmin)

admin.site.register(modalidad)

class oficinaResource(resources.ModelResource):
    class Meta:
        model = oficina

class oficinaAdmin(ImportExportModelAdmin):
    resources_class = oficinaResource
admin.site.register(oficina, oficinaAdmin)
admin.site.register(operatividad)
class pisoResource(resources.ModelResource):
    class Meta:
        model = piso

class pisoAdmin(ImportExportModelAdmin):
    resources_class = pisoResource
admin.site.register(piso, pisoAdmin )

class provinciaResource(resources.ModelResource):
    class Meta:
        model = provincia

class provinciaAdmin(ImportExportModelAdmin):
    resources_class = provinciaResource

admin.site.register(provincia, provinciaAdmin)
admin.site.register(recurso)
admin.site.register(sector)
class sedeResource(resources.ModelResource):
    class Meta:
        model = sede

class sedeAdmin(ImportExportModelAdmin):
    resources_class = sedeResource
admin.site.register(sede, sedeAdmin)

admin.site.register(situacion)
admin.site.register(suboficina)
admin.site.register(tipoDoc)
class usuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class usuarioAdmin(ImportExportModelAdmin):
    resources_class = usuarioResource
admin.site.register(Usuario, usuarioAdmin)

class base0Resource(resources.ModelResource):
    class Meta:
        model = models.base0

class base0Admin(ImportExportModelAdmin):
    resources_class = base0Resource
admin.site.register(models.base0, base0Admin)

admin.site.register(models.base12019)
class edificioResource(resources.ModelResource):
    class Meta:
        model = edificio

class edificioAdmin(ImportExportModelAdmin):
    resources_class = edificioResource
admin.site.register(models.edificio, edificioAdmin)

class catalogoResource(resources.ModelResource):
    class Meta:
        model = models.catalogo

class catalogoAdmin(ImportExportModelAdmin):
    resources_class = catalogoResource
admin.site.register(models.catalogo, catalogoAdmin)