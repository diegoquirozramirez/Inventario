from django.shortcuts import render, redirect
from Apps.Inventario.models import Usuario, ambiente, base0, base12019, piso, direccionGerencia, sede, ficha
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

    try:
        usu = Usuario.objects.get(numero_doc_usuario=dni)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, 'No se encontró un Usuario con dni '+str(dni)+' | Advertencia: NO Manipular la URL')
        return redirect('registar-usuario')

    pis = piso.objects.all()
    dep = direccionGerencia.objects.all()
    ambi = ambiente.objects.all()
    sed = sede.objects.all()
      
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

            usu = Usuario.objects.get(numero_doc_usuario=dni)
            fich = ficha.objects.get(idusuario_id=usu.id)           

            context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form, 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad , 'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep, 'ficha':fich.id}
            template = 'Inventario/base0.html'
            return render(request, template, context)
        else:
            messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo SBN '+str(codigo))
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
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
                    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
                else:
                    form = base0Form(instance=_base0)

                usu = Usuario.objects.get(numero_doc_usuario=dni)
                fich = ficha.objects.get(idusuario_id=usu.id) 
                
                context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form , 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad,  'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep,'ficha':fich.id}
                template = 'Inventario/base0.html'
                return render(request, template, context)
            else:
                messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo interno '+str(cod_interno))
                return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
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
                        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
                    else:
                        form = base0Form(instance=_base0)
                    

                    context = {'codigo_sbn_base0':codigo_sbn_base0,'codigo':codigo, 'cod_interno':cod_interno,'mensaje':mensaje, 'form':form ,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep}
                    template = 'Inventario/base0.html'
                    return render(request, template, context)
                else:
                    messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo interno '+str(cod_interno)+' ni el código SBN '+str(codigo))
                    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
        

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
    try:
        usu = Usuario.objects.get(numero_doc_usuario=dni)
        existencia_ficha = ficha.objects.filter(idusuario_id=usu.id)
        if existencia_ficha.exists():
            mensaje = "¡Ficha Grabada y Generada!"
            estado = True
            exist_ficha = ficha.objects.get(idusuario_id=usu.id)
            base1 = base12019.objects.filter(idficha_id=exist_ficha.id)

            pis = piso.objects.all()
            dep = direccionGerencia.objects.all()
            ambi = ambiente.objects.all()
            sed = sede.objects.all()
            print(base1)
            #base1 = base12019.objects.filter(user=request.user)
            contexto = {'usu':usu, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado, 'num_ficha': exist_ficha}
            template = 'Inventario/cabecera.html'
            return render(request, template, contexto)
                 
        else:
            mensaje = ""
            estado = False
            pis = piso.objects.all()
            dep = direccionGerencia.objects.all()
            ambi = ambiente.objects.all()
            sed = sede.objects.all()
            base1 = ''
            #base1 = base12019.objects.filter(user=request.user)
            contexto = {'usu':usu, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado}
            template = 'Inventario/cabecera.html'
            return render(request, template, contexto)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, 'No existe este Usuario con dni: '+str(dni))
        return redirect('registar-usuario')


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
    ficha = request.GET.get('ficha', None)
    cod_confor = request.GET.get('codigo_conformidad', None)

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

        if str(id) == '' or str(ficha) == '' or str(cod_confor) == '':
            messages.add_message(request, messages.INFO, 'Ingrese el Codigo de Confirmación para registrar este bien')
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
        else:
            base12019.objects.create(
                base0_fk_id = id,
                user = request.user,
                idficha_id = ficha,
                codigo_conformidad = cod_confor
            )
            messages.add_message(request, messages.INFO, 'Se registro correctamente')
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

    except IntegrityError:
        messages.add_message(request, messages.INFO, 'Ya se registró a una Ficha')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))


def deleteRegister(request,id):
    base12019.objects.filter(id=id).delete()
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

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
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

#Sprint 3

def grabarGenerarFicha(request):
    #num_ficha = request.GET.get('ficha', None)
    id_usuario = request.GET.get('usuario', None)
    ambiente = request.GET.get('ambiente', None)
    piso = request.GET.get('piso', None)
    dependencia = request.GET.get('dependencia', None)
    codigo_sede = request.GET.get('sede.cod_sede', None) 
    sede_id = request.GET.get('sede', None)  
    

    #para grabar y generar ficha
    sed = sede.objects.get(id=sede_id)

    print(str(sed.nom_sede)+', '+str(sed.cod_sede))
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombre', None)


    #if str(num_ficha) == '':
    #    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    #else:

    try:

        ficha.objects.create(
            num_ficha =str(sed.cod_sede),
            
            idusuario_id = id_usuario,
                #datos libres
            ambiente = ambiente,
            piso = piso,
            dependencia = str(dependencia), 
            sede = str(sed.nom_sede),

        )
    except IntegrityError:
        nu_ficha = ficha.objects.get(idusuario_id=id_usuario)
        messages.add_message(request, messages.INFO, 'Usuario con dni '+str(dni)+' ya se encuentra asociada a la ficha '+str(nu_ficha.num_ficha))
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))

    #para el redirect
   
    #print(num_ficha+" ,"+id_usuario+" ,"+ambiente+" ,"+piso+" ,"+str(dependencia)+" ,"+str(sede)+" ,"+dni+" ,"+nombres)

    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))