from django.shortcuts import render, HttpResponse
from Apps.Inventario.models import ficha, base12019

import io  
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle , Image 
from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle 
from reportlab.lib import colors  
from reportlab.lib.pagesizes import letter , landscape 
from reportlab.platypus import Table 
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT
# Create your views here.

def exportHojaPDF(self, pk=None):   
   
   response = HttpResponse(content_type='application/pdf')  
   buff = io.BytesIO()  
   doc = SimpleDocTemplate(buff,
               fileName='Hoja.pdf',#+str(pk),
               pagesize= landscape(letter),  
               #pagesize=letter,  
               rightMargin=40,  
               leftMargin=20,  
               topMargin=30,  
               bottomMargin=18,  
               )  
   categorias = []  
   styles = getSampleStyleSheet()  
   styleN = styles["Normal"] 
   
   pa = ParagraphStyle('parrafos', 
                           alignment=TA_CENTER,
                           fontSize = 5,
                           )
   pa2 = ParagraphStyle('parrafos2', 
                           spaceAfter=6,
                           alignment=TA_CENTER,
                           fontSize = 15,
                           )

   pa3 = ParagraphStyle('parrafos3', 
                           spaceAfter=6,
                           alignment=TA_RIGHT,
                           fontSize = 15,
                           )
   
   #ca  = Paragraph("Listado de 222 ", styles['Heading2']) 
   #categorias.append(header) 
   c = 0
   headings = ('ITEM', 'CODIGO 2019', 'CODIGO SBN', 'CODIGO 2018', 'NOMBRE DEL BIEN', 'MARCA', 'MODELO', 'SERIE', 'MEDIDAS','COLOR', 'EST', 'USO', 'OBSERVACION')  
   if not pk:  
     ficha_unique = [(p.id, p.num_ficha, p.fecha_ficha, p.ambiente)  
               for p in ficha_unique.objects.all().order_by('pk')]  
   else:  
     ficha_unique = [(p.idusuario, p.num_ficha, p.fecha_ficha, p.ambiente, p.sede, p.fecha_ficha, p.idusuario.numero_doc_usuario, p.idusuario.moda_usuario.modalidad_contratacion, p.piso, p.cod_ambiente, p.ambiente)  
               for p in ficha.objects.filter(id=pk)] 
     bienes = [( c, b.codigo_conformidad, b.base0_fk.codigo_sbn, b.base0_fk.codigo_interno, Paragraph(b.base0_fk.descripcion, pa),b.base0_fk.mar, b.base0_fk.modelo ,Paragraph(str(b.base0_fk.serie), pa),b.base0_fk.medida,b.base0_fk.col, b.base0_fk.est.nom_es, b.base0_fk.op, b.base0_fk.observacion1)
               for  b in base12019.objects.filter(idficha_id=pk)]


   ca0 = Image('https://upload.wikimedia.org/wikipedia/commons/c/ca/PCM-MIMP.png')
   ca0.drawHeight =  0.6*inch
   ca0.drawWidth = 3.3*inch
   ca0.hAlign = 'LEFT'


   header  = Paragraph("HOJA DE TOMA DE INVENTARIO DE BIENES MUEBLES DEL MIMP", pa2)
   header2 = Paragraph("AL 31 DE DICIEMBRE 2019 ", pa2) 




   ca1  = Paragraph("                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          Folio "+str(ficha_unique[0][1]), styles['Heading5'])
   ca2 = Paragraph("                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         Fecha "+str(ficha_unique[0][5]), styles['Heading5'])

   #Cabecera
   ca3 = Paragraph("USUARIO RESPONSABLE: "+str(ficha_unique[0][0])+" ___________________________________________________________  SEDE: "+str(ficha_unique[0][4])+"_______________________________", styles['Heading6'])
   ca4 = Paragraph("DNI: "+str(ficha_unique[0][6])+" ____________________________________________________  MODALIDAD: "+str(ficha_unique[0][7])+"  ________________________________PISO: "+str(ficha_unique[0][8])+" _________________________________", styles['Heading6'])
   ca5 = Paragraph("DIRECCIÓN: ______________________________________________________________________  CODIGO AMB: "+str(ficha_unique[0][9])+"  __________ AMBIENTE: "+str(ficha_unique[0][10]), styles['Heading6'])

   #Detalle
   ca6 = Paragraph("", styles['Heading6'])
   ca7 = Paragraph("", styles['Heading6'])
   ca8 = Paragraph("", styles['Heading6'])
   ca9 = Paragraph("", styles['Heading6'])

   t = Table([headings] + bienes, colWidths=[1.0 * cm, 1.4 * cm, 2.5 * cm, 1.5 * cm, 5.0 * cm, 1.5 * cm, 2.8 * cm, 1.5 * cm, 1.7 * cm, 1.5 * cm, 1.0 * cm, 1.5 * cm, 2.0 * cm]) 
   
    #, colWidths = [50, 50, 50, 50, 50,50, 50, 50, 50, 5050, 50, 50]

   count = base12019.objects.filter(idficha_id=pk).count()

   """for i in range(0, count+1):
       t.setStyle(TableStyle(
           ('FONTSIZE', (0, 0), (-1, 1), 5),
           ('GRID', (0, 0), (0, 0), 0, colors.white),
        ))"""


   t.setStyle(TableStyle(  
       [           
          
           ('FONTSIZE', (0, 0), (-1, -1), 6),           
            ('GRID', (0, 0), (-1, -1), 0, colors.black),
            ('LINEBELOW', (0, 0), (-1, -1), 0, colors.black),
            #('BACKGROUND', (0, 0), (0, 0), colors.dodgerblue),
           ('ALIGN', (0,0),(-1,-1), 'CENTER'),
           ('BOTTOMPADDING', (-1,-1), (-1,-1), 1),
        ]  
    )) 

   ca10 = Paragraph("Leyenda:_______________ USO (S)SI (N)NO ", styles['Heading6']) 
   ca11 = Paragraph("_______________________ ESTADO (B) BUENO (R) REGULAR (M) MALO (X) RAEE (Y) CHATARRA", styles['Heading6'])

   ca12 = Paragraph("", styles['Heading6'])
   ca13 = Paragraph("", styles['Heading6'])
   ca14= Paragraph("", styles['Heading6'])
   ca15 = Paragraph("", styles['Heading6'])

   ca16 = Paragraph("           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                  ___________________________________________________________________________", styles['Heading6'])

   ca17 = Paragraph("          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; INVENTARIADOR USUAIRO &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RESPONSABLE", styles['Heading6'])
   
   ca18 = Paragraph("", styles['Heading6'])
   ca19 = Paragraph("", styles['Heading6'])

   categorias.append(ca0)
   categorias.append(ca19)
   categorias.append(header) 
   categorias.append(header2)

   categorias.append(ca18)
   #categorias.append(ca19)
   #print(t)
   categorias.append(ca1)  
   categorias.append(ca2)

   categorias.append(ca3)
   categorias.append(ca4)
   categorias.append(ca5)
   categorias.append(ca6)
   categorias.append(ca7)
   categorias.append(ca8)
   categorias.append(ca9)

   categorias.append(t)   
   categorias.append(ca10)
   categorias.append(ca11)

   categorias.append(ca12)
   categorias.append(ca13)
   categorias.append(ca14)
   categorias.append(ca15)

   categorias.append(ca16)

   categorias.append(ca17)

   doc.build(categorias)  
   response.write(buff.getvalue())  
   buff.close()  
   return response  