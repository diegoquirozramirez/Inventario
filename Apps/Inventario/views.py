from django.shortcuts import render, redirect
from Apps.Inventario.models import usuario, ambiente, base0, base12019
from Apps.Inventario.forms import usuarioForm, ambienteForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
# Create your views here.
def cabecera(request, idu):
    usu = usuario.objects.get(id=idu)
    try:
        ambi = ambiente.objects.get(usuario_ambiente_id=idu)
    except ObjectDoesNotExist:
        ambi = ''
    context = {'usu':usu,'idu':idu, 'ambi':ambi}
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

def asignarCodAmbiente(request, idu):  
    correlativo = '0001'
    #ambi = ambiente.objects.get(id=ida)
    if request.method == 'POST':
        form = ambienteForm(request.POST or None)
        if form.is_valid():
            form_aux = form.save(commit = False)
            form_aux.cod_ambiente = str(form_aux.sede_ambiente.cod_sede)+str(form_aux.piso_ambiente.cod_piso)+str(correlativo)
            form_aux.usuario_ambiente_id = idu
            print(form_aux.usuario_ambiente_id)
            form_aux.save()
            return redirect('consultar', idu=idu)
    else:
        form = ambienteForm()
    
    context = {'form':form}
    template = 'Inventario/ambiente.html'
    return render(request, template, context)  

def updateAsignarCodAmbiente(request, idu, ida):  
    correlativo = '0001'
    ambi = ambiente.objects.get(id=ida)
    if request.method == 'POST':
        form = ambienteForm(request.POST, instance=ambi)
        if form.is_valid():
            form_aux = form.save(commit = False)
            form_aux.cod_ambiente = str(form_aux.sede_ambiente.cod_sede)+str(form_aux.piso_ambiente.cod_piso)+str(correlativo)
            form_aux.usuario_ambiente_id = idu            
            form_aux.save()
            return redirect('consultar', idu=idu)
    else:
        form = ambienteForm(instance=ambi)
    
    context = {'form':form}
    template = 'Inventario/ambiente.html'
    return render(request, template, context)

def listadoUsuario(request):
    usu = usuario.objects.all()
    context = {'usu':usu}
    template = 'Usuario/listado.html'
    return render(request, template, context)

def base0Consulta(request, idu):
    codigo = request.GET.get('codigo_sbn', None)
    cod_interno = request.GET.get('cod_interno', None)
    #usuario = request.GET['idu']
    if codigo != '' and cod_interno == '':        
        codigo_sbn_base0 = base0.objects.filter(codigo_sbn=codigo).filter(usuario_base0_id=idu)
        if codigo_sbn_base0.exists():
            context = {'codigo_sbn_base0':codigo_sbn_base0, 'idu':idu,'codigo':codigo, 'cod_interno':cod_interno}
            template = 'Inventario/base0.html'
            return render(request, template, context)
        else:
            print("No Existe")
            return redirect('consultar', idu=idu)
    else:
        if codigo == '' and cod_interno != '':
            codigo_sbn_base0 = base0.objects.filter(codigo_interno=cod_interno).filter(usuario_base0_id=idu)
            if codigo_sbn_base0.exists():
                context = {'codigo_sbn_base0':codigo_sbn_base0, 'idu':idu,'codigo':codigo, 'cod_interno':cod_interno}
                template = 'Inventario/base0.html'
                return render(request, template, context)
            else:
                print("No Existe")
                return redirect('consultar', idu=idu)
        else:
            if codigo != '' and cod_interno != '':
                codigo_sbn_base0 = base0.objects.filter(codigo_sbn=codigo).filter(codigo_interno=cod_interno).filter(usuario_base0_id=idu)
                if codigo_sbn_base0.exists():
                    context = {'codigo_sbn_base0':codigo_sbn_base0, 'idu':idu,'codigo':codigo, 'cod_interno':cod_interno}
                    template = 'Inventario/base0.html'
                    return render(request, template, context)
                else:
                    print("No Existe")
                    return redirect('consultar', idu=idu)
        

def addBase12019sbn(request, idbase0, idu, cod):
    if base0.objects.filter(id=idbase0).exists():
        try:
            base12019.objects.create(
                base0_fk_id=idbase0,
                user = request.user
            )
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn='+str(cod)+'&cod_interno=')#'base0-consultar', idu=idu)
        except:
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn='+str(cod)+'&cod_interno=')
    else:
        return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn='+str(cod)+'&cod_interno=')

def addBase12019cint(request, idbase0, idu, cod):
    if base0.objects.filter(id=idbase0).exists():
        try:
            base12019.objects.create(
                base0_fk_id=idbase0,
                user = request.user
            )
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))#'base0-consultar', idu=idu)
        except:
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
    else:
        return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
 