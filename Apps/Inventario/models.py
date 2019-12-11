from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class situacion(models.Model):
    cod_situ = models.CharField(max_length=2)
    nom_situ = models.CharField(max_length=60)
    obs_situ = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_situ)

class piso(models.Model):
    cod_piso = models.CharField(max_length=2)
    nom_psio = models.CharField(max_length=60)
    deta_piso = models.CharField(max_length=60, blank=True, null=True)
    obs_piso = models.CharField(max_length=60, blank=True, null=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_psio)

class sector(models.Model):
    cod_sector = models.CharField(max_length=2)
    nom_sector = models.CharField(max_length=60)
    obs_sector = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_sector)


class departamento(models.Model):
    cod_departamento = models.CharField(max_length=3) #antes 2
    nom_departamento = models.CharField(max_length=60)
    obs_departamento = models.CharField(max_length=60, blank=True)
    
    def __str__(self):
        return '{}, {}'.format(self.id,self.nom_departamento)

class provincia(models.Model):
    cod_provincia = models.CharField(max_length=3)
    nom_provincia = models.CharField(max_length=60)
    obs_provincia = models.CharField(max_length=60, blank=True)
    depa_provincia = models.ForeignKey(departamento, on_delete=models.CASCADE) #""" FK (departamento) """
    def __str__(self):
        return '{}, {}'.format(self.id,self.nom_provincia)

class distrito(models.Model):
    cod_distrito = models.CharField(max_length=4)
    nom_distrito = models.CharField(max_length=60)
    obs_distrito = models.CharField(max_length=60, blank=True)
    prov_distrito = models.ForeignKey(provincia, on_delete=models.CASCADE) #FK (provincia)
    def __str__(self):
        return '{}, {}'.format(self.id,self.nom_distrito)


class sede(models.Model):
    cod_sede = models.CharField(max_length=3)
    nom_sede = models.CharField(max_length=60)
    direc_fis_sede = models.CharField(max_length=60, blank=True, null=True)
    obs_sede = models.CharField(max_length=60, blank=True, null=True)
    depa_sede = models.ForeignKey(departamento, on_delete=models.CASCADE)#Depoartamento se convirtio en Tabla
    provi_sede = models.ForeignKey(provincia, on_delete=models.CASCADE)#Provincia se convirtio en Tabla    
    dis_sede = models.ForeignKey(distrito, on_delete=models.CASCADE)  #Distrito se convirtio en Tabla  
    def __str__(self):
        return '{} {}'.format(self.nom_sede, self.cod_sede)


class edificio(models.Model):
    cod_edificio = models.CharField(max_length=1)
    nom_edificio = models.CharField(max_length=60)
    deta_edificio = models.CharField(max_length=60)
    sede_edificio = models.ForeignKey(sede, on_delete=models.CASCADE) #""" FK (nombre de sede) """
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_edificio)



class tipoDoc(models.Model):
    cod_documento = models.CharField(max_length=1)
    tipo_doc = models.CharField(max_length=20)
    def __str__(self):
        return '{}, {}'.format(self.id, self.tipo_doc)

class modalidad(models.Model):
    cod_modalidad = models.CharField(max_length=2)
    modalidad_contratacion = models.CharField(max_length=60)
    obs_modalidad = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.modalidad_contratacion)



class jefeUsuario(models.Model):
    cod_jefusuario = models.CharField(max_length=8)
    numero_doc_jefusuario = models.CharField(max_length=8)
    nom_jefusuario = models.CharField(max_length=60)
    ap_pat_usuario = models.CharField(max_length=60)
    ap_mat_usuario = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60) #¿nombre de nuevo?
    obs_jefusuario   = models.CharField(max_length=60, blank=True) 
    moda_jefusuario = models.ForeignKey(modalidad, on_delete=models.CASCADE) #""" FK (modalidad) """
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_jefusuario)

class direccionGerencia(models.Model): #O es Direccion o es Gerencia dependiendo de la Estructura organizacional
    cod_dirger = models.CharField(max_length=2)
    nom_dirger = models.CharField(max_length=60)
    obs_dirger = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_dirger)

class oficina(models.Model):
    cod_oficina = models.CharField(max_length=2)
    nom_oficina = models.CharField(max_length=60)
    obs_oficina = models.CharField(max_length=60, blank=True)
    gere_oficina = models.ForeignKey(direccionGerencia, on_delete=models.CASCADE)  #""" FK (gerencia) """
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_oficina)

class suboficina(models.Model):
    cod_suboficina = models.CharField(max_length=2)
    nom_suboficina = models.CharField(max_length=60)
    obs_suboficina = models.CharField(max_length=60, blank=True)
    #""" 
    #FK (gerencia)
    gere_suboficina = models.ForeignKey(direccionGerencia, on_delete=models.CASCADE) 
    #FK (oficina)
    ofi_suboficina = models.ForeignKey(oficina, on_delete=models.CASCADE)
    #"""
    def __str__(self):
        return '{}, {}'.format(self.id, self.nom_suboficina)


"""class usuario(models.Model):
    cod_usuario = models.CharField(max_length=8)
    numero_doc_usuario = models.CharField(max_length=8)
    nom_final_usuario = models.CharField(max_length=60)
    ap_pat_usuario = models.CharField(max_length=60)
    ap_mat_usuario = models.CharField(max_length=60)
    nom_usuario = models.CharField(max_length=60)
    obs_usuario   = models.CharField(max_length=60, blank=True) 
    # 
    #FK (tipo documentos)
    t_doc_usuario = models.ForeignKey(tipoDoc, on_delete=models.CASCADE)
    #FK (modalidad)
    moda_usuario = models.ForeignKey(modalidad, on_delete=models.CASCADE)


    def __str__(self):
        return '{}, {}'.format(self.id, self.cod_usuario)
        """

class Usuario(models.Model):
    cod_usuario = models.CharField(max_length=8)
    numero_doc_usuario = models.CharField(max_length=8)
    nom_final_usuario = models.CharField(max_length=60,blank=True)
    ap_pat_usuario = models.CharField(max_length=60, blank=True)
    ap_mat_usuario = models.CharField(max_length=60, blank=True)
    nom_usuario = models.CharField(max_length=60, blank=True)
    obs_usuario   = models.CharField(max_length=60, blank=True) 
    #""" 
    #FK (tipo documentos)
    t_doc_usuario = models.ForeignKey(tipoDoc, on_delete=models.CASCADE)
    #FK (modalidad)
    moda_usuario = models.ForeignKey(modalidad, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.cod_usuario)

class ficha(models.Model):    
    num_ficha = models.CharField(max_length=7, blank=False, null= False)
    fecha_ficha = models.DateField(auto_now_add=True)
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #datos libres
    ambiente = models.CharField(max_length=60, default="")
    piso = models.CharField(max_length=5, default="") #deberia ser 2
    dependencia = models.CharField(max_length=60, default="")
    sede = models.CharField(max_length=60, default="")

    def __str__(self):
        return '{}, {} {}'.format(self.id, self.num_ficha, self.fecha_ficha)

    class Meta:
        unique_together = ['idusuario']

class ambiente(models.Model):
    # FK (usuario)
    #usuario_ambiente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #""" FK (nombre de Sede) """
    sede_ambiente = models.ForeignKey(sede, on_delete=models.CASCADE)
    #""" FK (piso) """
    piso_ambiente = models.ForeignKey(piso, on_delete=models.CASCADE)
    #""" FK (sector) """
    #sector_ambiente = models.ForeignKey(sector, on_delete=models.CASCADE)
    #depart = models.ForeignKey(departamento, on_delete=models.CASCADE)
    num_ambiente = models.CharField(max_length=4)
    nom_ambiente = models.CharField(max_length=60)
    cod_ambiente = models.CharField(max_length=9)
    obs_ambiente = models.CharField(max_length=60, blank=True)
    #cod_correlativo = models.CharField(max_length=4, default='')
    def __str__(self):
        return 'Codigo: {}, Nombre : {}, Sede: {}, Departamento: {}, Piso: {}'.format(self.cod_ambiente, self.nom_ambiente, self.sede_ambiente.nom_sede, self.sede_ambiente.depa_sede.nom_departamento, self.piso_ambiente.cod_piso)

"""class cabecera(models.Model):
    usu = models.ForeignKey(usuario, on_delete=models.CASCADE)
    moda = models.ForeignKey(modalidad, on_delete=models.CASCADE)
    sed = models.ForeignKey(sede, on_delete=models.CASCADE)
    pis = models.ForeignKey(piso, on_delete=models.CASCADE)
    ambi = models.ForeignKey(ambiente, on_delete=models.CASCADE)
    depa = models.ForeignKey(departamento, on_delete=models.CASCADE)
    provi = models.ForeignKey(provincia, on_delete=models.CASCADE)
    distri = models.ForeignKey(distrito, on_delete=models.CASCADE)
    dire_gere = models.ForeignKey(direccionGerencia, on_delete=models.CASCADE)
    ofi = models.ForeignKey(oficina, on_delete=models.CASCADE)
    subofi = models.ForeignKey(suboficina, on_delete=models.CASCADE)
"""
#Fin de cabecera"

#inicio de detalles"
class operatividad(models.Model):
    cod_ope = models.CharField(max_length=1)
    nom_ope = models.CharField(max_length=1)
    deta_ope = models.CharField(max_length=2)
    obs_ope = models.CharField(max_length=60, blank=True)
    
    def __str__(self):
        return '{}'.format( self.deta_ope)
    

class etiquetado(models.Model):
    cod_eti = models.CharField(max_length=1)
    nom_eti = models.CharField(max_length=60) #SI o NO -> ¿deberia ser 2?

class marca(models.Model):
    cod_marca = models.CharField(max_length=3)
    marca = models.CharField(max_length=60)

    def __str__(self):
        return ' {}'.format( self.marca)

class recurso(models.Model):
    cod_re = models.CharField(max_length=2)
    nom_re = models.CharField(max_length=60)
    deta_re = models.CharField(max_length=60, blank=True)
    obs_re = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return '{} {}'.format(self.cod_re, self.nom_re)

class color(models.Model):
    cod_color = models.CharField(max_length=3)
    nom_color = models.CharField(max_length=60)

    def __str__(self):
        return ' {}'.format( self.nom_color)
    
    def colors(self):
        col = self.nom_color        
        return '{}'.format(col)

class estado(models.Model):
    cod_es = models.CharField(max_length=1)
    nom_es = models.CharField(max_length=1)
    deta_es = models.CharField(max_length=60, blank=True)
    obs_es = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return ' {} '.format(  self.deta_es)


class base0(models.Model):
    #situ = models.ForeignKey(situacion, on_delete=models.CASCADE)
    mar = models.ForeignKey(marca, on_delete=models.CASCADE) #obligatorio
    col = models.ForeignKey(color, on_delete=models.CASCADE) #obligatorio
    est = models.ForeignKey(estado, on_delete=models.CASCADE) #obligatorio
    op = models.ForeignKey(operatividad, on_delete=models.CASCADE) #obligatorio

    codigo_sbn =models.CharField(max_length=12, blank=True)
    codigo_interno = models.CharField(max_length=5, blank=True)    
    descripcion = models.CharField(max_length=60, default='') #obligatorio
    detalle = models.CharField(max_length=60,default='')  #obligatorio
    modelo = models.CharField(max_length=60,default='')  #obligatorio
    serie =  models.CharField(max_length=60,default='') #obligatorio
    medida = models.CharField(max_length=60,default='') #obligatorio
    placa = models.CharField(max_length=60, blank=True, null=True) 
    motor = models.CharField(max_length=60, blank=True, null=True) 
    chasis =  models.CharField(max_length=60, blank=True, null=True)
    a_fabri = models.DateField(blank=True, null=True)
    puertas = models.IntegerField(blank=True, null=True)
    tar_propiedad = models.CharField(max_length=50, blank=True, null=True)
    observacion1 = models.CharField(max_length=60, blank=True, null=True)
    observacion2 = models.CharField(max_length=60, blank=True, null=True)
    observacion3 = models.CharField(max_length=60, blank=True, null=True)


    #usuario_base0 = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return 'SBN: {} | Interno: {}'.format(self.codigo_sbn, self.codigo_interno)

    

class base12019(models.Model):
    id = models.AutoField(primary_key=True, max_length=12)    
    base0_fk = models.ForeignKey(base0, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    idficha = models.ForeignKey(ficha, on_delete=models.CASCADE)  
    codigo_conformidad = models.CharField(max_length=5, blank=False, null=False)

    class Meta:
        unique_together = ['base0_fk']

    def __str__(self):
        return 'Base0: {} {} {}'.format(self.base0_fk,self.id, self.user)
    
