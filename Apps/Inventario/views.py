from django.shortcuts import render, redirect
from Apps.Inventario.models import usuario, ambiente
from Apps.Inventario.forms import usuarioForm, ambienteForm
# Create your views here.
def cabecera(request, idu):
    usu = usuario.objects.get(id=idu)
    context = {'usu':usu,'idu':idu}
    template = 'Inventario/consulta.html'
    return render(request, template, context)

def registraUsuario(request):    
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            ide = usuario.objects.last()
            print(ide.id)
            return redirect('consultar', idu=ide.id)
    else:
        form = usuarioForm()

    context = {'form':form}
    template = 'Usuario/registrar.html'
    return render(request, template, context)

#funcion especial para general codigo de ambiente concatenado

def asignarCodAmbiente(request, ida, idu):  
    correlativo = '0001'
    ambi = ambiente.objects.get(id=ida)
    if request.method == 'POST':
        form = ambienteForm(request.POST, instance=ambi)
        if form.is_valid():
            form_aux = form.save(commit = False)
            form_aux.cod_ambiente = str(form_aux.sede_ambiente.cod_sede)+str(form_aux.piso_ambiente.cod_piso)+str(correlativo)
            form_aux.save()
            return redirect('consultar', idu=idu)
    else:
        form = ambienteForm()

    context = {'form':form}
    template = 'Inventario/ambiente.html'
    return render(request, template, context)  