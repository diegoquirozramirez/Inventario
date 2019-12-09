from django.shortcuts import render, redirect
from Apps.Inventario.models import Usuario, ambiente, base0, base12019
from Apps.Inventario.forms import usuarioForm, ambienteForm, base0Form
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib import messages 

# Create your views here.
def cabecera(request, idu):
    usu = Usuario.objects.get(id=idu)
    try:
        ambi = ambiente.objects.filter(usuario_ambiente_id=idu)
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
            ide = Usuario.objects.last()
            print(ide.id)
            return redirect('consultar', idu=ide.id)
    else:
        form = usuarioForm()

    context = {'form':form}
    template = 'Usuario/registrar.html'
    return render(request, template, context)

#funcion especial para general codigo de ambiente concatenado

def asignarCodAmbiente(request, idu):  
    #correlativo = '0001'
    #ambi = ambiente.objects.get(id=ida)
    if request.method == 'POST':
        form = ambienteForm(request.POST or None)
        if form.is_valid():
            form_aux = form.save(commit = False)
            form_aux.cod_ambiente = str(form_aux.sede_ambiente.cod_sede)+str(form_aux.piso_ambiente.cod_piso)+str(form_aux.cod_correlativo)
            form_aux.usuario_ambiente_id = idu
            
            form_aux.save()
            return redirect('consultar', idu=idu)
    else:
        form = ambienteForm()
    
    context = {'form':form}
    template = 'Inventario/ambiente.html'
    return render(request, template, context)  

def updateAsignarCodAmbiente(request, idu, ida):  
    #correlativo = '0001'
    ambi = ambiente.objects.get(id=ida)
    if request.method == 'POST':
        form = ambienteForm(request.POST, instance=ambi)
        if form.is_valid():
            form_aux = form.save(commit = False)
            form_aux.cod_ambiente = str(form_aux.sede_ambiente.cod_sede)+str(form_aux.piso_ambiente.cod_piso)+str(form_aux.cod_correlativo)
            form_aux.usuario_ambiente_id = idu            
            form_aux.save()
            return redirect('consultar', idu=idu)
    else:
        form = ambienteForm(instance=ambi)
    
    context = {'form':form}
    template = 'Inventario/ambiente.html'
    return render(request, template, context)

def listadoUsuario(request):
    usu = Usuario.objects.all()
    context = {'usu':usu}
    template = 'Usuario/listado.html'
    return render(request, template, context)

def base0Consulta(request):
    codigo = request.GET.get('codigo_sbn', None)
    cod_interno = request.GET.get('cod_interno', None)
    #ambiente = request.GET.get('ambiente', None)
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    usu = Usuario.objects.get(numero_doc_usuario=dni)
    ambi = ambiente.objects.all()
    print(cod_interno)
    #usuario = request.GET['idu']
    #if codigo == '' and cod_interno == '':
     #   messages.add_message(request, messages.INFO, 'Ingrese código SBN o código interno')
      #  return redirect('consultar', idu=idu)

    if codigo != '' and cod_interno == '':        
        codigo_sbn_base0 = base0.objects.filter(codigo_sbn=codigo)
       #form = 
        if codigo_sbn_base0.exists():
            if base12019.objects.filter(base0_fk = codigo_sbn_base0[0].id).exists():
                mensaje = "Registrado"
            else:
                mensaje = "No registrado"
            
            _base0 = base0.objects.get(codigo_sbn=codigo)
            if request.method == 'POST':
                form = base0Form(request.POST, instance=_base0)
                if form.is_valid():
                    form.save()
                return redirect('home')
            else:
                form = base0Form(instance=_base0)

            context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form, 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad , 'usu':usu, 'ambi':ambi}
            template = 'Inventario/base0.html'
            return render(request, template, context)
        else:
            messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo SBN '+str(codigo))
            return redirect("home")
    else:
        if codigo == '' and cod_interno != '':
            
            codigo_sbn_base0 = base0.objects.filter(codigo_interno=cod_interno)
        
         
            if codigo_sbn_base0.exists():
                if base12019.objects.filter(base0_fk = codigo_sbn_base0[0].id).exists():
                    mensaje = "Registrado"
                else:
                    mensaje = "No registrado"

                _base0 = base0.objects.get(codigo_sbn=codigo)
                if request.method == 'POST':
                    form = base0Form(request.POST, instance=_base0)
                    if form.is_valid():
                        form.save()
                    return redirect('home')
                else:
                    form = base0Form(instance=_base0)

                
                context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form , 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad,  'usu':usu, 'ambi':ambi}
                template = 'Inventario/base0.html'
                return render(request, template, context)
            else:
                messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo interno '+str(cod_interno))
                return redirect("home")
        else:
            if codigo != '' and cod_interno != '':
                codigo_sbn_base0 = base0.objects.filter(codigo_sbn=codigo).filter(codigo_interno=cod_interno)
                                
                if codigo_sbn_base0.exists():
                    if base12019.objects.filter(base0_fk = codigo_sbn_base0[0].id).exists():
                        mensaje = "Registrado"
                    else:
                        mensaje = "No registrado"

                    _base0 = base0.objects.get(codigo_sbn=codigo)
                    if request.method == 'POST':
                        form = base0Form(request.POST, instance=_base0)
                        if form.is_valid():
                            form.save()
                        return redirect('home')
                    else:
                        form = base0Form(instance=_base0)
                    

                    context = {'codigo_sbn_base0':codigo_sbn_base0,'codigo':codigo, 'cod_interno':cod_interno,'mensaje':mensaje, 'form':form ,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'usu':usu, 'ambi':ambi}
                    template = 'Inventario/base0.html'
                    return render(request, template, context)
                else:
                    return redirect('home')
        

def addBase12019sbn(request):#, idbase0, idu, cod):
    descripcion = request.GET.get('id_descipcion', None)
    print(descripcion)
    return redirect('/MIMP/base0/?codigo_sbn=952285140375&cod_interno=')
    """if base0.objects.filter(id=idbase0).exists():
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
    """

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
 

 #SPRINT 2

def buscarUsuario(request):
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombres', None)
    tipo = request.GET.get('tipo', None)
    modalidad = request.GET.get('modalidad', None)
    usu = Usuario.objects.get(numero_doc_usuario=dni)
    ambi = ambiente.objects.all()
    base1 = base12019.objects.filter(user=request.user)
    contexto = {'usu':usu, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad}
    template = 'Inventario/cabecera.html'
    return render(request, template, contexto)

def captureBase0(request):
    
    des = request.GET.get('descripcion', None)
    obs1 = request.GET.get('observacion1', None)
    det = request.GET.get('detalle', None)
    obs2 = request.GET.get('observacion2', None)
    mar = request.GET.get('mar', None)
    obs3 = request.GET.get('observacion3', None)
    mod = request.GET.get('modelo', None)
    est = request.GET.get('est', None)
    ser = request.GET.get('serie', None)
    op = request.GET.get('op', None)
    med = request.GET.get('medida', None)
    placa = request.GET.get('placa', None)
    col = request.GET.get('col', None)
    mot = request.GET.get('motor', None)
    id = request.GET.get('id', None)

    #codigo_interno = request.GET.get('codigo_interno', None)
    #codigo_sbn = request.GET.get('codigo_sbn', None)
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    base0.objects.filter(id=id).update(
        
        mar = mar ,
        col = col ,
        est = est,
        op = op ,

        
        descripcion = des,
        detalle = det ,
        modelo = mod,
        serie = ser,
        medida = med ,
        placa = placa ,
        motor = mot ,
       
        observacion1 = obs1,
        observacion2 = obs2,
        observacion3 = obs3,
    )
    
    try:

        base12019.objects.create(
            base0_fk_id = id,
            user = request.user
        )
        messages.add_message(request, messages.INFO, 'Se registro correctamente')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre)+'&tipo='+str(tipo)+'&modalidad='+str(modalidad))

    except IntegrityError:
        messages.add_message(request, messages.INFO, 'Ya se registró')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre)+'&tipo='+str(tipo)+'&modalidad='+str(modalidad))


def deleteRegister(request,id):
    base12019.objects.filter(id=id).delete()
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre)+'&tipo='+str(tipo)+'&modalidad='+str(modalidad))

def editRegister(request, id):    
    base = base12019.objects.get(id=id)
    print(base.base0_fk.id)
    base1 = base0.objects.get(id=base.base0_fk_id)
    
    if request.method == 'POST':
        dni = request.GET.get('dni', None)
        
        nombre = request.GET.get('nombre', None)
        tipo = request.GET.get('tipo', None)
        modalidad= request.GET.get('modalidad', None)
        codigo_sbn = request.GET.get('codigo_sbn', None)
        
        
        form = base0Form(request.POST, instance=base1)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = base0Form(instance=base1)
        dni = request.GET.get('dni', None)
        
        nombre = request.GET.get('nombre', None)
        tipo = request.GET.get('tipo', None)
        modalidad= request.GET.get('modalidad', None)
        codigo_sbn = request.GET.get('codigo_sbn', None)

    template= 'Inventario/update.html'    
    usu = Usuario.objects.get(numero_doc_usuario=dni)
    codigo_sbn_base0 = base0.objects.get(codigo_sbn=codigo_sbn)
    ambi = ambiente.objects.all()
    context = {'form':form, 'id':base.base0_fk_id, 'dni':dni, 'nombre':nombre, 'tipo':tipo,'modalidad':modalidad, 'usu':usu, 'ambi':ambi, 'codigo_sbn_base0':codigo_sbn_base0 }

    return render(request, template, context)

def updateOneRegister(request):
    des = request.GET.get('descripcion', None)
    obs1 = request.GET.get('observacion1', None)
    det = request.GET.get('detalle', None)
    obs2 = request.GET.get('observacion2', None)
    mar = request.GET.get('mar', None)
    obs3 = request.GET.get('observacion3', None)
    mod = request.GET.get('modelo', None)
    est = request.GET.get('est', None)
    ser = request.GET.get('serie', None)
    op = request.GET.get('op', None)
    med = request.GET.get('medida', None)
    placa = request.GET.get('placa', None)
    col = request.GET.get('col', None)
    mot = request.GET.get('motor', None)
    id = request.GET.get('id', None)

    #codigo_interno = request.GET.get('codigo_interno', None)
    #codigo_sbn = request.GET.get('codigo_sbn', None)
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    base0.objects.filter(id=id).update(
        
        mar = mar ,
        col = col ,
        est = est,
        op = op ,

        
        descripcion = des,
        detalle = det ,
        modelo = mod,
        serie = ser,
        medida = med ,
        placa = placa ,
        motor = mot ,
       
        observacion1 = obs1,
        observacion2 = obs2,
        observacion3 = obs3,
    )

    messages.add_message(request, messages.INFO, 'Se actualizo correctamente')
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre)+'&tipo='+str(tipo)+'&modalidad='+str(modalidad))

