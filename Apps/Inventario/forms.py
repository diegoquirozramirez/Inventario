from django import forms
from Apps.Inventario.models import usuario, ambiente

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario

        fields = [
            'cod_usuario',
            'numero_doc_usuario',
            'nom_final_usuario' ,
            'ap_pat_usuario' ,
            'ap_mat_usuario' ,
            'nom_usuario', 
            'obs_usuario', 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' ,
            #FK (modalidad)
            'moda_usuario',
            #"""    
            'sed',
            'pis',
            #'ambi',
            'depa' ,
            'provi',
            'distri',
            'dire_gere',
            'ofi',
            'subofi',           
            'edifi',
            'sect',
            'jef',
        ]

        labels = {
            'cod_usuario': '',
            'numero_doc_usuario': '',
            'nom_final_usuario': '' ,
            'ap_pat_usuario': '' ,
            'ap_mat_usuario': '' ,
            'nom_usuario': '', 
            'obs_usuario': '', 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' : '',
            #FK (modalidad)
            'moda_usuario': '',
            #"""    
            'sed': '',
            'pis': '',
            #'ambi': '',
            'depa' : '',
            'provi': '',
            'distri': '',
            'dire_gere': '',
            'ofi': '',
            'subofi': '',
            'edifi': '',
            'sect': '',
            'jef': '',
        }

        widgets = {
            'cod_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'numero_doc_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'nom_final_usuario': forms.TextInput(attrs={'class':'form-control'}) ,
            'ap_pat_usuario':forms.TextInput(attrs={'class':'form-control'}) ,
            'ap_mat_usuario': forms.TextInput(attrs={'class':'form-control'}) ,
            'nom_usuario': forms.TextInput(attrs={'class':'form-control'}), 
            'obs_usuario': forms.TextInput(attrs={'class':'form-control'}), 
            #""" 
            #FK (tipo documentos)
            't_doc_usuario' : forms.Select(attrs={'class':'form-control'}),
            #FK (modalidad)
            'moda_usuario': forms.Select(attrs={'class':'form-control'}),
            #"""    
            'sed': forms.Select(attrs={'class':'form-control'}),
            'pis': forms.Select(attrs={'class':'form-control'}),
            #'ambi': forms.Select(attrs={'class':'form-control'}),
            'depa' : forms.Select(attrs={'class':'form-control'}),
            'provi': forms.Select(attrs={'class':'form-control'}),
            'distri': forms.Select(attrs={'class':'form-control'}),
            'dire_gere': forms.Select(attrs={'class':'form-control'}),
            'ofi': forms.Select(attrs={'class':'form-control'}),
            'subofi': forms.Select(attrs={'class':'form-control'}),
            'edifi': forms.Select(attrs={'class':'form-control'}),
            'sect': forms.Select(attrs={'class':'form-control'}),
            'jef': forms.Select(attrs={'class':'form-control'}),
        }

class ambienteForm(forms.ModelForm):
    class Meta:
        model = ambiente

        fields = [
            #'cod_ambiente',            
            'sector_ambiente',
            'num_ambiente',
            'nom_ambiente',
            'obs_ambiente',
            'sede_ambiente',
            'piso_ambiente',
            #'usuario_ambiente'
            'cod_correlativo',
        ]

        labels = {
            #'cod_ambiente':'',
            'sede_ambiente':'',
            'piso_ambiente':'',
            'sector_ambiente':'',
            'num_ambiente':'',
            'nom_ambiente':'',
            'obs_ambiente':'',
            'cod_correlativo':'',
        }

        widgets = {
            #'cod_ambiente': forms.TextInput(),
            'sector_ambiente':forms.Select(attrs={'class':'form-control'}),
            'num_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'nom_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'obs_ambiente':forms.TextInput(attrs={'class':'form-control'}),
            'sede_ambiente': forms.Select(attrs={'class':'form-control'}),
            'piso_ambiente': forms.Select(attrs={'class':'form-control'}),
            'cod_correlativo': forms.TextInput(attrs={'class':'form-control'}),
            
        }