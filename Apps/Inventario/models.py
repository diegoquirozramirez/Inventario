from django.db import models

# Create your models here.
class ficha(models.Model):
    cod_ficha = models.CharField(max_length=3)
    num_ficha = models.CharField(max_length=9)

class situacion(models.Model):
    cod_situ = models.CharField(max_length=2)
    nom_situ = models.CharField(max_length=60)
    obs_situ = models.CharField(max_length=60, blank=True)

class piso(models.Model):
    cod_piso = models.CharField(max_length=2)
    nom_psio = models.CharField(max_length=60)
    deta_piso = models.CharField(max_length=60, blank=True, null=True)
    obs_piso = models.CharField(max_length=60, blank=True, null=True)

class sector(models.Model):
    cod_sector = models.CharField(max_length=2)
    nom_sector = models.CharField(max_length=60)
    obs_sector = models.CharField(max_length=60)


class departamento(models.Model):
    cod_departamento = models.CharField(max_length=2)
    mon_departamento = models.CharField(max_length=60)
    obs_departamento = models.CharField(max_length=60, blank=True)

class provincia(models.Model):
    cod_provincia = models.CharField(max_length=3)
    mon_provincia = models.CharField(max_length=60)
    obs_provincia = models.CharField(max_length=60, blank=True)
    depa_provincia = models.ForeigKey(departamento, on_delete=models.CASCADE) #""" FK (departamento) """

class distrito(models.Model):
    cod_distrito = models.CharField(max_length=4)
    mon_distrito = models.CharField(max_length=60)
    obs_distrito = models.CharField(max_length=60, blank=True)
    prov_distrito = models.ForeigKey(provincia, on_delete=models.CASCADE) #FK (provincia)


class sede(models.Model):
    cod_sede = models.CharField(max_length=3)
    nom_sede = models.CharField(max_length=60)
    direc_fis_sede = models.CharField(max_length=60, blank=True, null=True)
    obs_sede = models.CharField(max_length=60, blank=True, null=True)
    depa_sede = models.ForeigKey(departamento, on_delete=models.CASCADE)#Depoartamento se convirtio en Tabla
    provi_sede = models.ForeigKey(provincia, on_delete=models.CASCADE)#Provincia se convirtio en Tabla    
    dis_sede = models.ForeigKey(distrito, on_delete=models.CASCADE)  #Distrito se convirtio en Tabla  
    


class edificio(models.Model):
    cod_edificio = models.CharField(max_length=1)
    nom_edificio = models.CharField(max_length=60)
    deta_edificio = models.CharField(max_length=60)
    sede_edificio = models.ForeigKey(sede, on_delete=models.CASCADE) #""" FK (nombre de sede) """

class ambiente(models.Model):
    #""" FK (nombre de Sede) """
    sede_ambiente = models.ForeigKey(sede, on_delete=models.CASCADE)
    #""" FK (piso) """
    piso_ambiente = models.ForeigKey(piso, on_delete=models.CASCADE)
    #""" FK (sector) """
    sector_ambiente = models.ForeigKey(sector, on_delete=models.CASCADE)
    num_ambiente = models.CharField(max_length=4)
    mon_ambiente = models.CharField(max_length=60)
    cod_ambiente = models.CharField(max_length=9)
    obs_ambiente = models.CharField(max_length=60, blank=True)

class tipoDoc(models.Model):
    cod_documento = models.CharField(max_length=1)
    tipo_doc = models.CharField(max_length=20)

class modalidad(models.Model):
    cod_modalidad = models.CharField(max_length=2)
    modalidad_contratacion = models.CharField(max_length=8)
    obs_modalidad = models.CharField(max_length=60, blank=True)

class usuario(models.Model):
    cod_usuario = models.CharField(max_length=8)
    numero_doc_usuario = models.CharField(max_length=8)
    nom_final_usuario = models.CharField(max_length=60)
    ap_pat_usuario = models.CharField(max_length=60)
    ap_mat_usuario = models.CharField(max_length=60)
    nom_usuario = models.CharField(max_length=60)
    obs_usuario   = models.CharField(max_length=60, blank=True) 
    #""" 
    #FK (tipo documentos)
    t_doc_usuario = models.ForeigKey(tipoDoc, on_delete=models.CASCADE)
    #FK (modalidad)
    moda_usuario = models.ForeigKey(modalidad, on_delete=models.CASCADE)
    #"""

class jefeUsuario(models.Model):
    cod_jefusuario = models.CharField(max_length=8)
    numero_doc_jefusuario = models.CharField(max_length=8)
    nom_jefusuario = models.CharField(max_length=60)
    ap_pat_usuario = models.CharField(max_length=60)
    ap_mat_usuario = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60) #¿nombre de nuevo?
    obs_jefusuario   = models.CharField(max_length=60, blank=True) 
    moda_jefusuario = models.ForeigKey(modalidad, on_delete=models.CASCADE) #""" FK (modalidad) """

class direccionGerencia(models.Model): #O es Direccion o es Gerencia dependiendo de la Estructura organizacional
    cod_dirger = models.CharField(max_length=2)
    nom_dirger = models.CharField(max_length=60)
    obs_dirger = models.CharField(max_length=60, blank=True)

class oficina(models.Model):
    cod_oficina = models.CharField(max_length=2)
    nom_oficina = models.CharField(max_length=60)
    obs_oficina = models.CharField(max_length=60, blank=True)
    gere_oficina = models.ForeigKey(direccionGerencia, on_delete=models.CASCADE)  #""" FK (gerencia) """

class suboficina(models.Model):
    cod_suboficina = models.CharField(max_length=2)
    nom_suboficina = models.CharField(max_length=60)
    obs_suboficina = models.CharField(max_length=60, blank=True)
    #""" 
    #FK (gerencia)
    gere_suboficina = models.ForeigKey(direccionGerencia, on_delete=models.CASCADE) 
    #FK (oficina)
    ofi_suboficina = models.ForeigKey(oficina, on_delete=models.CASCADE)
    #"""

class cabecera(models.Model):
    usu = models.ForeigKey(usuario, on_delete=models.CASCADE)
    moda = models.ForeigKey(modalidad, on_delete=models.CASCADE)
    sed = models.ForeigKey(sede, on_delete=models.CASCADE)
    pis = models.ForeigKey(piso, on_delete=models.CASCADE)
    ambi = models.ForeigKey(ambiente, on_delete=models.CASCADE)
    depa = models.ForeigKey(departamento, on_delete=models.CASCADE)
    provi = models.ForeigKey(provincia, on_delete=models.CASCADE)
    distri = models.ForeigKey(distrito, on_delete=models.CASCADE)
    dire_gere = models.ForeigKey(direccionGerencia, on_delete=models.CASCADE)
    ofi = models.ForeigKey(oficina, on_delete=models.CASCADE)
    subofi = models.ForeigKey(suboficina, on_delete=models.CASCADE)

#Fin de cabecera"

#inicio de detalles"
class operatividad(models.Model):
    cod_ope = models.CharField(max_length=1)
    nom_ope = models.CharField(max_length=1)
    deta_ope = models.CharField(max_length=2)
    obs_ope = models.CharField(max_length=60, blank=True)

class etiquetado(models.Model):
    cod_eti = models.CharField(max_length=1)
    nom_eti = models.CharField(max_length=60) #SI o NO -> ¿deberia ser 2?

class marca(models.Model):
    cod_marca = models.CharField(max_length=3)
    marca = models.CharField(max_length=60)

class recurso(models.Model):
    cod_re = models.CharField(max_length=2)
    nom_re = models.CharField(max_length=60)
    deta_re = models.CharField(max_length=60, blank=True)
    obs_re = models.CharField(max_length=60, blank=True)

class color(models.Model):
    cod_color = models.CharField(max_length=3)
    nom_color = models.CharField(max_length=60)

class estado(models.Model):
    cod_es = models.CharField(max_length=1)
    nom_es = models.CharField(max_length=1)
    deta_es = models.CharField(max_length=60, blank=True)
    obs_es = models.CharField(max_length=60, blank=True)

