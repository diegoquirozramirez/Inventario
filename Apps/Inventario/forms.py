from django import forms
from Apps.Inventario.models import Usuario, ambiente, base0

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            #'cod_usuario',
            'numero_doc_usuario',
            #'nom_final_usuario' ,
            'ap_pat_usuario' ,
            'ap_mat_usuario' ,
            'nom_usuario', 
            #'obs_usuario', 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' ,
            #FK (modalidad)
            'moda_usuario',
            #"""    
        
        ]

        labels = {
            #'cod_usuario': '',
            'numero_doc_usuario': '',
            #'nom_final_usuario': '' ,
            'ap_pat_usuario': '' ,
            'ap_mat_usuario': '' ,
            'nom_usuario': '', 
            #'obs_usuario': '', 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' : '',
            #FK (modalidad)
            'moda_usuario': '',
            
        }

        widgets = {
            #'cod_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'numero_doc_usuario': forms.TextInput(attrs={'class':'form-control'}),
            #'nom_final_usuario': forms.TextInput(attrs={'class':'form-control'}) ,
            'ap_pat_usuario':forms.TextInput(attrs={'class':'form-control'}) ,
            'ap_mat_usuario': forms.TextInput(attrs={'class':'form-control'}) ,
            'nom_usuario': forms.TextInput(attrs={'class':'form-control'}), 
            #'obs_usuario': forms.TextInput(attrs={'class':'form-control'}), 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' : forms.Select(attrs={'class':'form-control'}),
            #FK (modalidad)
            'moda_usuario': forms.Select(attrs={'class':'form-control'}),
          
        }

class ambienteForm(forms.ModelForm):
    class Meta:
        model = ambiente

        fields = [
            #'cod_ambiente',            
            #'sector_ambiente',
            'num_ambiente',
            'nom_ambiente',
            'obs_ambiente',
            'sede_ambiente',
            'piso_ambiente',
            #'usuario_ambiente'
            #'cod_correlativo',
        ]

        labels = {
            #'cod_ambiente':'',
            'sede_ambiente':'',
            'piso_ambiente':'',
            #'sector_ambiente':'',
            'num_ambiente':'',
            'nom_ambiente':'',
            'obs_ambiente':'',
           # 'cod_correlativo':'',
        }

        widgets = {
            #'cod_ambiente': forms.TextInput(),
            #'sector_ambiente':forms.Select(attrs={'class':'form-control'}),
            'num_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'nom_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'obs_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'sede_ambiente': forms.Select(attrs={'class':'form-control'}),
            'piso_ambiente': forms.Select(attrs={'class':'form-control'}),
            #'cod_correlativo': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class base0Form(forms.ModelForm):
    class Meta:
        model = base0

        fields =[
            'id',
            'mar' ,
            'col' ,
            'est',
            'op' ,

            'codigo_sbn' ,
            'codigo_interno' ,
            'descripcion',
            'detalle' ,
            'modelo',
            'serie',
            'medida' ,
            'placa' ,
            'motor' ,
            'chasis' ,
            'a_fabri' ,
            'puertas' ,
            'tar_propiedad',
            'observacion1',
            'observacion2',
            'observacion3',
        ]

        labels = {
            'id':'',
            'mar':'' ,
            'col':'' ,
            'est':'',
            'op' :'',

            'codigo_sbn':'' ,
            'codigo_interno':'' ,
            'descripcion':'',
            'detalle' :'',
            'modelo':'',
            'serie':'',
            'medida' :'',
            'placa' :'',
            'motor' :'',
            'chasis' :'',
            'a_fabri' :'',
            'puertas' :'',
            'tar_propiedad':'',
            'observacion1':'',
            'observacion2':'',
            'observacion3':'',
        }

        widgets = {
            'id':forms.TextInput(),
            'mar' : forms.Select(attrs={'class':'form-control'}),
            'col' : forms.Select(attrs={'class':'form-control'}),
            'est': forms.Select(attrs={'class':'form-control'}),
            'op' : forms.Select(attrs={'class':'form-control'}),

            'codigo_sbn' :forms.TextInput(attrs={'class':'form-control'}),
            'codigo_interno' :forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'detalle' :forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'medida' :forms.TextInput(attrs={'class':'form-control'}),
            'placa' :forms.TextInput(attrs={'class':'form-control'}),
            'motor' :forms.TextInput(attrs={'class':'form-control'}),
            'chasis' :forms.TextInput(attrs={'class':'form-control'}),
            'a_fabri' :forms.TextInput(attrs={'class':'form-control'}),
            'puertas' :forms.TextInput(attrs={'class':'form-control'}),
            'tar_propiedad':forms.TextInput(attrs={'class':'form-control'}),
            'observacion1':forms.TextInput(attrs={'class':'form-control'}),
            'observacion2':forms.TextInput(attrs={'class':'form-control'}),
            'observacion3':forms.TextInput(attrs={'class':'form-control'}),
        }