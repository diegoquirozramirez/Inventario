from django.contrib import admin
from Apps.Inventario.models import ambiente,color,departamento,direccionGerencia,distrito,edificio,estado,etiquetado,ficha,jefeUsuario,marca,modalidad,oficina,operatividad,piso,provincia,recurso,sector,sede,situacion,suboficina,tipoDoc,usuario
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(ambiente)
#admin.site.register(cabecera)
admin.site.register(color)
class departamentoResource(resources.ModelResource):
    class Meta:
        model = departamento

class departamentoAdmin(ImportExportModelAdmin):
    resources_class = departamentoResource

admin.site.register(departamento, departamentoAdmin)
admin.site.register(direccionGerencia)
admin.site.register(distrito)
admin.site.register(estado)
admin.site.register(etiquetado)
admin.site.register(ficha)
admin.site.register(jefeUsuario)
admin.site.register(marca)
admin.site.register(modalidad)
admin.site.register(oficina)
admin.site.register(operatividad)
admin.site.register(piso)

class provinciaResource(resources.ModelResource):
    class Meta:
        model = provincia

class provinciaAdmin(ImportExportModelAdmin):
    resources_class = provinciaResource

admin.site.register(provincia, provinciaAdmin)
admin.site.register(recurso)
admin.site.register(sector)
admin.site.register(sede)
admin.site.register(situacion)
admin.site.register(suboficina)
admin.site.register(tipoDoc)
admin.site.register(usuario)

