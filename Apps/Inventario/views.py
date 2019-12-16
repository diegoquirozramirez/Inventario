from django.shortcuts import render, redirect
from Apps.Inventario.models import Usuario, ambiente, base0, base12019, piso, direccionGerencia, sede, ficha, catalogo, userGroup, modalidad
from Apps.Inventario.forms import usuarioForm, ambienteForm, base0Form, fichaForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib import messages 

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def cabecera(request, idu):
    usu = Usuario.objects.get(id=idu)
    try:
        ambi = ambiente.objects.filter(usuario_ambiente_id=idu)
    except ObjectDoesNotExist:
        ambi = ''
    context = {'usu':usu,'idu':idu, 'ambi':ambi}
    template = 'Inventario/consulta.html'
    return render(request, template, context)

@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def listadoUsuario(request):
    usu = Usuario.objects.all()
    context = {'usu':usu}
    template = 'Usuario/listado.html'
    return render(request, template, context)

@login_required(login_url='/')
def base0Consulta(request):
    f = request.GET.get('ficha', None)
    fi = ficha.objects.get(num_ficha=f)
    codigo = request.GET.get('codigo_sbn', None)
    cod_interno = request.GET.get('cod_interno', None)
    #ambiente = request.GET.get('ambiente', None)
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    count = base12019.objects.filter(user=request.user).count()
    if codigo != '':
        if base0.objects.filter(codigo_sbn=codigo).exists():
            b = base0.objects.get(codigo_sbn=codigo)
            cod_sbn_cat = b.codigo_sbn
    if cod_interno != '':
        if base0.objects.filter(codigo_interno=cod_interno).exists():
            b = base0.objects.get(codigo_interno=cod_interno)
            cod_sbn_cat = b.codigo_sbn

    if len(codigo) == 12 or len(cod_interno) == 5:
    
        try:
            fcha = ficha.objects.get(idusuario__nom_final_usuario=str(nombre))
            usu = Usuario.objects.get(id=fcha.idusuario_id)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.INFO, 'No se encontró un Usuario con dni '+str(dni))
            return redirect('/MIMP/registrar-usuario')

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

                fich = ficha.objects.get(idusuario__nom_final_usuario=str(nombre))
                usu = Usuario.objects.get(id=fcha.idusuario_id)
                #usu = Usuario.objects.get(numero_doc_usuario=dni)
                #fich = ficha.objects.get(idusuario_id=usu.id)           

                context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form, 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad , 'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep, 'ficha':fich.id, 'count':count, 'num_ficha':fi, 'cod_sbn_cat':cod_sbn_cat}
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

                    _base0 = base0.objects.get(codigo_interno=cod_interno)
                    if request.method == 'POST':
                        form = base0Form(request.POST, instance=_base0)
                        if form.is_valid():
                            form.save()
                        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
                    else:
                        form = base0Form(instance=_base0)

                    
                    fich = ficha.objects.get(idusuario__nom_final_usuario=str(nombre))
                    usu = Usuario.objects.get(id=fcha.idusuario_id)
                    #usu = Usuario.objects.get(numero_doc_usuario=dni)
                    #fich = ficha.objects.get(idusuario_id=usu.id) 
                    
                    context = {'codigo_sbn_base0':codigo_sbn_base0, 'codigo':codigo, 'cod_interno':cod_interno, 'mensaje':mensaje, 'form':form , 'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad,  'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep,'ficha':fich.id, 'count':count, 'num_ficha':fi, 'cod_sbn_cat':cod_sbn_cat}
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
                        
                        
                        fich = ficha.objects.get(idusuario__nom_final_usuario=str(nombre))
                        usu = Usuario.objects.get(id=fcha.idusuario_id)
                        #usu = Usuario.objects.get(numero_doc_usuario=dni)
                        #fich = ficha.objects.get(idusuario_id=usu.id) 


                        context = {'codigo_sbn_base0':codigo_sbn_base0,'codigo':codigo, 'cod_interno':cod_interno,'mensaje':mensaje, 'form':form ,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'usu':usu, 'ambi':ambi,'pis':pis, 'sed':sed, 'dep':dep, 'ficha':fich.id, 'count':count, 'num_ficha':fi, 'cod_sbn_cat':cod_sbn_cat}
                        template = 'Inventario/base0.html'
                        return render(request, template, context)
                    else:
                        messages.add_message(request, messages.INFO, 'No se encontró registro con el codigo interno '+str(cod_interno)+' ni el código SBN '+str(codigo)+", o no tengan relación alguna.")
                        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

    else:
        messages.add_message(request, messages.INFO, 'Datos no admitidos, asegúrese de haber ingresado correctamente los valores o no haya dejado campos en blanco')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
            
@login_required(login_url='/')
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

@login_required(login_url='/')
def addBase12019cint(request, idbase0, idu, cod):
    if base0.objects.filter(id=idbase0).exists():
        try:
            base12019.objects.create(
                base0_fk_id=idbase0,
                user = request.user
            )
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
        except:
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
    else:
        return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
 

 #SPRINT 2
from django.db.models import Q
@login_required(login_url='/')
def buscarUsuario(request):
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombres', None)
    tipo = request.GET.get('tipo', None)
    modali = request.GET.get('modalidad', None)
    print(str(dni), str(dni), str(nombre), str(tipo))
    count = base12019.objects.filter(user=request.user).count()
    mod = modalidad.objects.all()
    try:
        #if len(dni) == 8:
        usu = Usuario.objects.filter(Q(numero_doc_usuario__iexact=dni) | Q(nom_final_usuario__icontains=nombre))
        if usu.exists():
            usua = Usuario.objects.get(id=usu[0].id)
        else:
            messages.add_message(request, messages.INFO, 'Usuario no encontrado')
            return redirect('/MIMP/buscar-usuario?nombres=*')
        #else:
        #    messages.add_message(request, messages.INFO, 'Caracteres minimo para DNI es 8')
        #    return redirect('/MIMP/registrar-usuario')
            
        print("este es q "+str(usu))
        print("tener id"+str(usua))
        existencia_ficha = ficha.objects.filter(idusuario_id__nom_final_usuario=str(nombre))
        if existencia_ficha.exists():
            mensaje = "¡Ficha Grabada y Generada!"
            estado = True
            exist_ficha = ficha.objects.get(idusuario_id__nom_final_usuario=str(nombre))
            base1 = base12019.objects.filter(idficha_id=exist_ficha.id).order_by('item')
                        
            pis = piso.objects.all()
            dep = direccionGerencia.objects.all()
            ambi = ambiente.objects.all()
            sed = sede.objects.all()
            print(base1)
           
            contexto = {'usu':usua, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modali':modali, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado, 'num_ficha': exist_ficha,'count':count, 'mod':mod}
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
            
            contexto = {'usu':usua, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modali':modali, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado,'count':count, 'mod':mod}
            template = 'Inventario/cabecera.html'
            return render(request, template, contexto)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, 'No existe este Usuario con dni: '+str(dni))
        return redirect('/MIMP/buscar-usuario?nombres=*')

@login_required(login_url='/')
def captureBase0(request):
    
    des = request.GET.get('descripcion', '')
    obs1 = request.GET.get('observacion1', '')
    det = request.GET.get('detalle', '')
    obs2 = request.GET.get('observacion2', None)
    mar = request.GET.get('mar', None)
    obs3 = request.GET.get('observacion3', None)
    mod = request.GET.get('modelo', '')
    est = request.GET.get('est', None)
    ser = request.GET.get('serie', '')
    op = request.GET.get('op', None)
    med = request.GET.get('medida', '')
    placa = request.GET.get('placa', '')
    col = request.GET.get('col', None)
    mot = request.GET.get('motor', '')
    id = request.GET.get('id', None)

    
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    tipo = request.GET.get('tipo', None)
    modalidad= request.GET.get('modalidad', None)
    ficha = request.GET.get('ficha', None)
    cod_confor = request.GET.get('codigo_conformidad', None)

    if base12019.objects.filter(codigo_conformidad=str(cod_confor)):
        messages.add_message(request, messages.INFO, 'Codigo de Confirmación usado')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

    c_sbn = request.GET.get('codigo_sbn', None)

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
   
    item_first = 1
    try:

        if str(id) == '' or str(ficha) == '' or str(cod_confor) == '':
            messages.add_message(request, messages.INFO, 'Ingrese el Codigo de Confirmación para registrar este bien')
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
        else:
            if base12019.objects.filter(idficha_id=ficha).exists():
                print("No es nuevo")
                item_last = base12019.objects.filter(idficha_id=ficha).order_by('item').last()

                base12019.objects.create(
                    base0_fk_id = id,
                    user = request.user,
                    idficha_id = ficha,
                    codigo_conformidad = cod_confor,
                    codigo_sbn = c_sbn,
                    item = item_last.item + 1,
                )
                messages.add_message(request, messages.INFO, 'Se registro correctamente')
                return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))
            else:
                print("no es nuevo")
                base12019.objects.create(
                    base0_fk_id = id,
                    user = request.user,
                    idficha_id = ficha,
                    codigo_conformidad = cod_confor,
                    codigo_sbn = c_sbn,
                    item = item_first,
                )
                messages.add_message(request, messages.INFO, 'Se registro correctamente')
                return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

    except IntegrityError:
        messages.add_message(request, messages.INFO, 'Ya se registró a una Ficha')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

#cuando este con la cabecera
@login_required(login_url='/')
def deleteRegister(request,id):
    
    base01 = base12019.objects.get(id=id)

    if str(base01.prov_cata) == 'S':
        base0.objects.get(id=base01.base0_fk_id).delete()
    else:
        base12019.objects.get(id=id).delete()
    
    
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))


@login_required(login_url='/')
def editRegister(request, id):    
    base = base12019.objects.get(id=id)
    print(base.base0_fk.id)
    base1 = base0.objects.get(id=base.base0_fk_id)
    fi = ficha.objects.get(id=base.idficha_id)
    
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
       
    usu = Usuario.objects.get(id=fi.idusuario_id)
    if codigo_sbn != '':
        pass#codigo_sbn_base0 = base0.objects.get(codigo_sbn=codigo_sbn)
    else:
        dni = request.GET.get('dni', None)
        
        nombre = request.GET.get('nombre', None)
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

    ambi = ambiente.objects.all()
    context = {'form':form, 'id':base.base0_fk_id, 'dni':dni, 'nombre':nombre, 'tipo':tipo,'modalidad':modalidad, 'usu':usu, 'ambi':ambi,  'num_ficha':fi }

    return render(request, template, context)

@login_required(login_url='/')
def updateOneRegister(request):
    des = request.GET.get('descripcion', None)
    obs1 = request.GET.get('observacion1', None)
    det = request.GET.get('detalle', None)
    #obs2 = request.GET.get('observacion2', None)
    mar = request.GET.get('mar', None)
    #obs3 = request.GET.get('observacion3', None)
    mod = request.GET.get('modelo', None)
    est = request.GET.get('est', None)
    ser = request.GET.get('serie', None)
    op = request.GET.get('op', None)
    med = request.GET.get('medida', None)
    #placa = request.GET.get('placa', None)
    col = request.GET.get('col', None)
    #mot = request.GET.get('motor', None)
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
        #placa = placa ,
        #motor = mot ,
       
        observacion1 = obs1,
        #observacion2 = obs2,
        #observacion3 = obs3,
    )

    messages.add_message(request, messages.INFO, 'Se actualizo correctamente')
    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

#Sprint 3

@login_required(login_url='/')
def grabarGenerarFicha(request):
    #num_ficha = request.GET.get('ficha', None)
    id_usuario = request.GET.get('usuario', None)
    mod = request.GET.get('modalidad', None)
    am = request.GET.get('ambi', None)
    dni = request.GET.get('dni_ficha', None)
    nombres = request.GET.get('nombre', None)
    direccion = request.GET.get('direccion', None)

    if str(nombres) == '*':
        messages.add_message(request, messages.INFO, 'Diríjase a Nueva Hoja')
        return redirect('/MIMP/buscar-usuario?nombres=*')

    #piso = request.GET.get('piso', None)
    #dependencia = request.GET.get('dependencia', None)
    #codigo_sede = request.GET.get('sede.cod_sede', None) 
    #sede_id = request.GET.get('sede', None)
    # 
    if str(am) == '':
        messages.add_message(request, messages.INFO, 'Ingrese el ambiente')
        return redirect('/MIMP/buscar-usuario?nombres=*')

    if str(dni) == '':
        messages.add_message(request, messages.INFO, 'Ingrese el dni')
        return redirect('/MIMP/buscar-usuario?nombres=*')

    #ambient = ambiente.objects.get(id=ambi)  
    
    a = str(am).split(",")
    try:
        ambient = ambiente.objects.get(num_ambiente=str(a[0])) 
    except:
        messages.add_message(request, messages.INFO, 'Ambiente no Identificado')
        return redirect('/MIMP/buscar-usuario?nombres=*')
    
    #print(a[0],a[1],a[2])

    #para grabar y generar ficha
    #sed = sede.objects.get(id=sede_id)

    #print(str(sed.nom_sede)+', '+str(sed.cod_sede))
    

    #if str(num_ficha) == '':
    #    return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    #else:

    if ficha.objects.all().exists() == False:
        ug = userGroup.objects.get(user=request.user)
        primer_numero = 1
        try:

            ficha.objects.create(
                num_ficha =str(ug.codgroup)+str(ambient.sede_ambiente.cod_sede)+str(primer_numero),
                
                idusuario_id = id_usuario,
                    #datos libres
                ambiente = a[1],#str(ambient.nom_ambiente),
                piso = a[3],#str(ambient.piso_ambiente.deta_piso),
                #dependencia = str(dependencia), 
                sede = a[2],# str(ambient.sede_ambiente.nom_sede),
                cod_ambiente = a[0],
                user = request.user,
                modalidad_ficha = str(mod),
                dni_ficha = str(dni),
                dependencia = direccion,

            )
        except IntegrityError:
            nu_ficha = ficha.objects.get(idusuario_id=id_usuario)
            messages.add_message(request, messages.INFO, 'Usuario con dni '+str(dni)+' ya se encuentra asociada a la ficha '+str(nu_ficha.num_ficha))
            return redirect('/MIMP/buscar-usuario?nombres=*')

        #para el redirect
    
        #print(num_ficha+" ,"+id_usuario+" ,"+ambiente+" ,"+piso+" ,"+str(dependencia)+" ,"+str(sede)+" ,"+dni+" ,"+nombres)

        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    else:
        ug_exists = userGroup.objects.filter(user=request.user)
        if ug_exists.exists():

            ug = userGroup.objects.get(user=request.user)
            fl = ficha.objects.last()
            try:

                ficha.objects.create(
                    num_ficha =str(ug.codgroup)+str(ambient.sede_ambiente.cod_sede)+str(int(fl.numero_aux)+1),
                    
                    idusuario_id = id_usuario,
                        #datos libres
                    ambiente = a[1],
                    piso = a[3],
                    #dependencia = str(dependencia), 
                    sede =  a[2],
                    numero_aux = int(fl.numero_aux)+1,
                    cod_ambiente = a[0],
                    user =  request.user,
                    modalidad_ficha=str(mod),
                    dni_ficha = str(dni),
                    dependencia = direccion,

                )
            except IntegrityError:
                nu_ficha = ficha.objects.get(idusuario_id=id_usuario)
                messages.add_message(request, messages.INFO, 'Usuario con dni '+str(dni)+' ya se encuentra asociada a la ficha '+str(nu_ficha.num_ficha))
                return redirect('/MIMP/buscar-usuario?nombres=*')

            #para el redirect
        
            #print(num_ficha+" ,"+id_usuario+" ,"+ambiente+" ,"+piso+" ,"+str(dependencia)+" ,"+str(sede)+" ,"+dni+" ,"+nombres)

            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
        else:
            messages.add_message(request, messages.INFO, str(request.user).upper()+' no está asociado algun grupo.')
            return redirect('/MIMP/buscar-usuario?nombres=*')

@login_required(login_url='/')
def buscarFicha(request):
    template = 'Ficha/buscar.html'
    return render(request, template)

#con ajax
from django.core import serializers
from django.http import HttpResponse
"""def consultarFicha(request):
    fich = request.GET.get('ficha', None)
    data = ficha.objects.filter(num_ficha=fich)
    datas = serializers.serialize('json', data, fields=('num_ficha','fecha_ficha','ambiente','piso','dependencia','sede'))  
    return HttpResponse(datas, content_type='application/json')"""


@login_required(login_url='/')
def updateFicha(request):
    num_ficha = request.GET.get('num_ficha_edit2', None)
    fich = ficha.objects.get(num_ficha=num_ficha)
    if request.method == 'POST':
        form = fichaForm(request.POST, instance=fich)
        if form.is_valid():
            form.save()
        return redirect('/consultar-ficha/?num_ficha='+str(num_ficha))
    else:
        form = fichaForm(instance=fich)
    context = {'form':form, 'num_ficha':num_ficha}
    template = 'Ficha/update.html'
    return render(request, template, context)

@login_required(login_url='/')
def consultarFicha(request):
    fich = request.GET.get('num_ficha', None)
    if fich == '':
        messages.add_message(request, messages.INFO, 'Ingrese el Número de Ficha '+str(fich))
        return redirect('buscar-ficha')

    try:
        data = ficha.objects.get(num_ficha=fich)
        registros = base12019.objects.filter(idficha_id=data.id)
        print(registros)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, 'No existe la ficha con Número '+str(fich))
        return redirect('buscar-ficha')

    template = 'Ficha/ficha.html'
    context = {'data':data, 'registros':registros}
    return render(request, template, context)

@login_required(login_url='/')
def deleteFicha(request):
    fich = request.GET.get('num_ficha', None)
    ficha.objects.get(num_ficha=fich).delete()
    return redirect('buscar-ficha')

@login_required(login_url='/')
def verCatalogo(request):
    fich = request.GET.get('ficha', None)
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombre', None)
    fi = ficha.objects.get(num_ficha=fich)
    context = {'dni':dni, 'nombres':nombres, 'ficha':fich, 'num_ficha':fi}
    template = 'Catalogo/catalogo.html'
    return render(request, template, context)

import json
@login_required(login_url='/')
def get_catalogos(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = catalogo.objects.filter(denominacion_bien__icontains=q)
        dic = {}
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.denominacion_bien#+ "," +str(pl.id)
            results.append(place_json)
            dic = {'bien':pl.denominacion_bien,'cod_bien':pl.numero_bien}
        data = json.dumps(results)
        #print(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


from django.core import serializers
@login_required(login_url='/')
def get_ambiente(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = ambiente.objects.filter(num_ambiente__icontains=q)

        #alli = [*ambiente.objects.filter(nom_ambiente__icontains=q)]
        place_json =  serializers.serialize("json", ambiente.objects.filter(nom_ambiente__icontains=q), fields=('nom_ambiente','num_ambiente','sede_ambiente__nom_sede','piso_ambiente__nom_piso'))#+ " | " +str(pl.sede_ambiente.nom_sede)+" | "+str(pl.piso_ambiente.nom_piso)
        
        results = []
        for pl in places:
            place_json = {}
            place_json = str(pl.num_ambiente)+","+pl.nom_ambiente+","+str(pl.sede_ambiente.nom_sede)+","+str(pl.piso_ambiente.nom_piso)
            results.append(place_json)
            #dic = {'bien':pl.denominacion_bien,'cod_bien':pl.numero_bien}
        data = json.dumps(results)

    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

#cuando este de ficha sin cabecera
@login_required(login_url='/')
def deleteBienFicha(request,id):   
    #ficha = request.GET.get('num_ficha', None)   
    try:
        base12019.objects.get(id=id).delete()
        ba1 = base12019.objects.get(id=id)
        fi = ficha.objects.get(id=ba1.idficha_id)
        messages.add_message(request, messages.INFO, "Registro Eliminado"+str(ba1.idficha__num_ficha))
        return redirect('/buscar-ficha/')   
    except:
        return redirect('/buscar-ficha/')   
    
@login_required(login_url='/')
def updateBienFicha(request, id):
    #fich = request.GET.get('num_ficha', None)
    #fi = ficha.objects.get(num_ficha=str(fich))
   # print(fi)
    bien1 = base12019.objects.get(id=id)
    bien0 = base0.objects.get(id=bien1.base0_fk_id)
    if request.method == 'POST':
        form = base0Form(request.POST, instance = bien0)
        if form.is_valid():
            form.save()
        return redirect('/buscar-ficha/')#'/consultar-ficha/?num_ficha='+str(fich))
    else:
        form = base0Form(instance=bien0)
    context = {'form':form, 'bien0':bien0}
    template = 'Ficha/bienUpdate.html'
    return render(request, template, context)


@login_required(login_url='/')
def standByCatalogo(request):
    #valor de la denominacion
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombres', None)
    confor = request.GET.get('codigo_conformidad', None)
    if base12019.objects.filter(codigo_conformidad=str(confor)):
        messages.add_message(request, messages.INFO, 'Codigo de Confirmación usado')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    
    fich = request.GET.get('ficha', None)
    fi = ficha.objects.get(num_ficha=str(fich))
   
    cata = request.GET.get('catalogo', None)
    codcat = catalogo.objects.get(denominacion_bien=str(cata))
    
    if request.method == 'POST':
        form = base0Form(request.POST)
        if form.is_valid():
            form_aux = form.save(commit = False)
            """if form_aux.descripcion == cata:
                form_aux.codigo_sbn = str(codcat.numero_bien)
                form_aux.aux_ficha = str(fich)+str(request.user.id)
                form_aux.save()

                #b0 = base0.objects.get(aux_ficha=(str(fich)+str(request.user.id)))

                #base0.objects.filter(id=b0.id).update(
                    #aux_ficha=str(fich)+str(b0.id),
                #)
                
                base12019.objects.create(
                    base0_fk_id = form_aux.id,
                    user = request.user,
                    idficha_id = fi.id,
                    codigo_conformidad = str(confor),
                    prov_cata = 'S',
                )
                print("FOrmulario")
                print(form_aux)
            else:
                messages.add_message(request, messages.INFO, 'No manipules el Campo con atributo solo de Lectura')
                return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))"""
            form_aux.codigo_sbn = str(codcat.numero_bien)
            form_aux.aux_ficha = str(fich)+str(request.user.id)
            form_aux.save()

                #b0 = base0.objects.get(aux_ficha=(str(fich)+str(request.user.id)))

                #base0.objects.filter(id=b0.id).update(
                    #aux_ficha=str(fich)+str(b0.id),
                #)

            print("FOrmulario")
            print(form_aux)

            if base12019.objects.filter(idficha_id=fi.id).exists(): 
                      
                item_last = base12019.objects.filter(idficha_id=fi.id).order_by('item').last()
                base12019.objects.create(               

                    base0_fk = form_aux,
                    user = request.user,
                    idficha_id = fi.id,
                    codigo_conformidad = str(confor),
                    prov_cata = 'S',
                    item = item_last.item+1,
                )
                
            else:
                item_last = 1
                base12019.objects.create(               

                    base0_fk = form_aux,
                    user = request.user,
                    idficha_id = fi.id,
                    codigo_conformidad = str(confor),
                    prov_cata = 'S',
                    item = item_last,
                )
                
            
            print("FOrmulario")
            print(form_aux)
        messages.add_message(request, messages.INFO, 'Se registró correctamente')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    else:
        form = base0Form()

    template = 'Catalogo/standby.html'
    context = {'form':form, 'cata':cata, 'ficha':fich,'confor': confor, 'num_ficha':fi}
    return render(request, template, context)

@login_required(login_url='/')
def get_ficha(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = ficha.objects.filter(num_ficha__icontains=q)
      
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.num_ficha#+","+pl.nom_ambiente+","+str(pl.sede_ambiente.nom_sede)+","+str(pl.piso_ambiente.nom_piso)
            results.append(place_json)
            #dic = {'bien':pl.denominacion_bien,'cod_bien':pl.numero_bien}
        data = json.dumps(results)

    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@login_required(login_url='/')
def get_usuario(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Usuario.objects.filter(nom_final_usuario__icontains=q)
      
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.nom_final_usuario#+","+pl.nom_ambiente+","+str(pl.sede_ambiente.nom_sede)+","+str(pl.piso_ambiente.nom_piso)
            results.append(place_json)
            #dic = {'bien':pl.denominacion_bien,'cod_bien':pl.numero_bien}
        data = json.dumps(results)

    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# Para funcionamiento de Ajax
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.generic import View



def viewFicha(request):
    fi = request.GET.get('fi', None)
    fich = ficha.objects.filter(num_ficha=fi)
    ba1 = base12019.objects.filter(idficha__num_ficha=fich)
    fich = [  ficha_serilizer(fich) for fich in fich ]
    #ba1 = [ base1_serilizer(ba1) for ba1 in ba1 ]
    return HttpResponse(json.dumps(fich),content_type='application/json')

def ficha_serilizer(ficha):
    return {
        'id':ficha.id,
        'num_ficha':ficha.num_ficha,
        'fecha_ficha':str(ficha.fecha_ficha),
        'ambiente':ficha.ambiente,
        'dependencia': ficha.dependencia,
        'cod_ambiente': ficha.cod_ambiente,
        'piso': ficha.piso,
        'sede': ficha.sede,
        'idusuario':ficha.idusuario.nom_final_usuario,
        }
    
def viewFichaBienes(request):
    fi = request.GET.get('fi', None)
  
    ba1 = base12019.objects.filter(idficha__num_ficha=fi)
    
    ba1 = [ base1_serilizer(ba1) for ba1 in ba1 ]

    return HttpResponse(json.dumps(ba1),content_type='application/json')


def base1_serilizer(ba1):
    return {
        'id':ba1.id,
        'codigo_interno':ba1.base0_fk.codigo_interno,
        'codigo_sbn':ba1.base0_fk.codigo_sbn,
        'descripcion':ba1.base0_fk.descripcion,
        'detalle':ba1.base0_fk.detalle,
        'marca':str(ba1.base0_fk.mar),
        'modelo':ba1.base0_fk.modelo,
        'medida':ba1.base0_fk.medida,
        'serie':ba1.base0_fk.serie,
        'estado':str(ba1.base0_fk.est.nom_es),
        'operatividad':str(ba1.base0_fk.op),
        'observaciones':ba1.base0_fk.observacion1,
      
        }
       
def get_direccion(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = direccionGerencia.objects.filter(nom_dirger__icontains=q)
        dic = {}
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.nom_dirger#+ "," +str(pl.id)
            results.append(place_json)
            #dic = {'bien':pl.denominacion_bien,'cod_bien':pl.numero_bien}
        data = json.dumps(results)
        #print(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
        