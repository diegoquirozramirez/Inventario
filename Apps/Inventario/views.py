from django.shortcuts import render, redirect
from Apps.Inventario.models import Usuario, ambiente, base0, base12019, piso, direccionGerencia, sede, ficha, catalogo, userGroup
from Apps.Inventario.forms import usuarioForm, ambienteForm, base0Form, fichaForm
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

    if len(codigo) == 12 or len(cod_interno) == 5:
    
        try:
            usu = Usuario.objects.get(numero_doc_usuario=dni)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.INFO, 'No se encontró un Usuario con dni '+str(dni)+' | Advertencia: NO Manipular la URL')
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

                    _base0 = base0.objects.get(codigo_interno=cod_interno)
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

    else:
        messages.add_message(request, messages.INFO, 'Datos no admitids por el sistema, asegurese de haber ingresado correctamente los valores')
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
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
        except:
            return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
    else:
        return redirect('/MIMP/base0/'+str(idu)+'?codigo_sbn=&cod_interno='+str(cod))
 

 #SPRINT 2
from django.db.models import Q
def buscarUsuario(request):
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombres', None)
    tipo = request.GET.get('tipo', None)
    modalidad = request.GET.get('modalidad', None)
    print(str(dni), str(dni), str(nombre), str(tipo))

    try:
        if len(dni) == 8:
            usu = Usuario.objects.filter(Q(numero_doc_usuario__iexact=dni) | Q(nom_final_usuario__icontains=nombre))
            if usu.exists():
                usua = Usuario.objects.get(id=usu[0].id)
            else:
                messages.add_message(request, messages.INFO, 'Usuario no encontrado')
                return redirect('/MIMP/registrar-usuario')
        else:
            messages.add_message(request, messages.INFO, 'Caracteres minimo para DNI es 8')
            return redirect('/MIMP/registrar-usuario')
            
        print("este es q "+str(usu))
        print("tener id"+str(usua))
        existencia_ficha = ficha.objects.filter(idusuario_id=usu[0].id)
        if existencia_ficha.exists():
            mensaje = "¡Ficha Grabada y Generada!"
            estado = True
            exist_ficha = ficha.objects.get(idusuario_id=usu[0].id)
            base1 = base12019.objects.filter(idficha_id=exist_ficha.id)
            
            pis = piso.objects.all()
            dep = direccionGerencia.objects.all()
            ambi = ambiente.objects.all()
            sed = sede.objects.all()
            print(base1)
           
            contexto = {'usu':usua, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado, 'num_ficha': exist_ficha}
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
            
            contexto = {'usu':usua, 'ambi':ambi, 'base1':base1,'dni':dni, 'nombre':nombre, 'tipo':tipo, 'modalidad':modalidad, 'pis':pis, 'dep':dep, 'sed':sed, 'mensaje':mensaje, 'estado': estado}
            template = 'Inventario/cabecera.html'
            return render(request, template, contexto)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, 'No existe este Usuario con dni: '+str(dni))
        return redirect('/MIMP/registrar-usuario')


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

#cuando este con la cabecera
def deleteRegister(request,id):
    
    base01 = base12019.objects.get(id=id)

    if str(base01.prov_cata) == 'S':
        base0.objects.get(id=base01.base0_fk_id).delete()
    else:
        base12019.objects.get(id=id).delete()
    
    
    dni = request.GET.get('dni', None)
    nombre = request.GET.get('nombre', None)
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
    if codigo_sbn != '':
        codigo_sbn_base0 = base0.objects.get(codigo_sbn=codigo_sbn)
    else:
        dni = request.GET.get('dni', None)
        
        nombre = request.GET.get('nombre', None)
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombre))

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
    ambi = request.GET.get('ambiente', None)
    am = request.GET.get('ambi', None)
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombre', None)

    #piso = request.GET.get('piso', None)
    #dependencia = request.GET.get('dependencia', None)
    #codigo_sede = request.GET.get('sede.cod_sede', None) 
    #sede_id = request.GET.get('sede', None)
    # 
    if str(am) == '':
        messages.add_message(request, messages.INFO, 'Ingrese el ambiente')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))

    #ambient = ambiente.objects.get(id=ambi)  
    
    a = str(am).split(",")
    try:
        ambient = ambiente.objects.get(num_ambiente=str(a[0])) 
    except:
        messages.add_message(request, messages.INFO, 'Ambiente no Identificado')
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    
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

            )
        except IntegrityError:
            nu_ficha = ficha.objects.get(idusuario_id=id_usuario)
            messages.add_message(request, messages.INFO, 'Usuario con dni '+str(dni)+' ya se encuentra asociada a la ficha '+str(nu_ficha.num_ficha))
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))

        #para el redirect
    
        #print(num_ficha+" ,"+id_usuario+" ,"+ambiente+" ,"+piso+" ,"+str(dependencia)+" ,"+str(sede)+" ,"+dni+" ,"+nombres)

        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    else:
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

            )
        except IntegrityError:
            nu_ficha = ficha.objects.get(idusuario_id=id_usuario)
            messages.add_message(request, messages.INFO, 'Usuario con dni '+str(dni)+' ya se encuentra asociada a la ficha '+str(nu_ficha.num_ficha))
            return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))

        #para el redirect
    
        #print(num_ficha+" ,"+id_usuario+" ,"+ambiente+" ,"+piso+" ,"+str(dependencia)+" ,"+str(sede)+" ,"+dni+" ,"+nombres)

        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))


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

def updateFicha(request):
    num_ficha = request.GET.get('num_ficha', None)
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

def deleteFicha(request):
    fich = request.GET.get('num_ficha', None)
    ficha.objects.get(num_ficha=fich).delete()
    return redirect('buscar-ficha')

def verCatalogo(request):
    fich = request.GET.get('ficha', None)
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombre', None)
    context = {'dni':dni, 'nombres':nombres, 'ficha':fich}
    template = 'Catalogo/catalogo.html'
    return render(request, template, context)

import json
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


import json
from django.core import serializers
def get_ambiente(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = ambiente.objects.filter(nom_ambiente__icontains=q)

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
def deleteBienFicha(request,id):   
    ficha = request.GET.get('num_ficha', None)   
    try:
        base12019.objects.get(id=id).delete()
        return redirect('/consultar-ficha/?num_ficha='+str(ficha))   
    except:
        return redirect('/consultar-ficha/?num_ficha='+str(ficha))   
    

def updateBienFicha(request, id):
    fich = request.GET.get('num_ficha', None)
    fi = ficha.objects.get(num_ficha=str(fich))
    print(fi)
    bien1 = base12019.objects.get(id=id)
    bien0 = base0.objects.get(id=bien1.base0_fk_id)
    if request.method == 'POST':
        form = base0Form(request.POST, instance = bien0)
        if form.is_valid():
            form.save()
        return redirect('/consultar-ficha/?num_ficha='+str(fich))
    else:
        form = base0Form(instance=bien0)
    context = {'form':form,'fi':fi, 'bien0':bien0}
    template = 'Ficha/bienUpdate.html'
    return render(request, template, context)

def standByCatalogo(request):
    #valor de la denominacion
    confor = request.GET.get('codigo_conformidad', None)
    fich = request.GET.get('ficha', None)
    fi = ficha.objects.get(num_ficha=str(fich))
    cata = request.GET.get('catalogo', None)
    codcat = catalogo.objects.get(denominacion_bien=str(cata))
    dni = request.GET.get('dni', None)
    nombres = request.GET.get('nombres', None)
    if request.method == 'POST':
        form = base0Form(request.POST or None)
        if form.is_valid():
            form_aux = form.save(commit = False)
            if form_aux.descripcion == cata:
                form_aux.codigo_sbn = str(codcat.numero_bien)
                form_aux.aux_ficha = str(fich)+str(request.user.id)
                form_aux.save()

                #b0 = base0.objects.get(aux_ficha=(str(fich)+str(request.user.id)))

                #base0.objects.filter(id=b0.id).update(
                    #aux_ficha=str(fich)+str(b0.id),
                #)
                
                base12019.objects.create(
                    base0_fk = form_aux,
                    user = request.user,
                    idficha_id = fi.id,
                    codigo_conformidad = str(confor),
                    prov_cata = 'S',
                )

            else:
                messages.add_message(request, messages.INFO, 'No manipules el Campo con atributo solo de Lectura')
                return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
        return redirect('/MIMP/buscar-usuario?dni='+str(dni)+'&nombres='+str(nombres))
    else:
        form = base0Form()

    template = 'Catalogo/standby.html'
    context = {'form':form, 'cata':cata, 'ficha':fich,'confor': confor}
    return render(request, template, context)