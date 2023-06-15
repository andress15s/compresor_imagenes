from PIL import Image #importamos la libreria PIL
import os #importamos la libreria os

rutaActual = os.path.dirname(os.path.abspath(__file__)) #obtenemos la ruta actual

cont = 1

for nombre in os.listdir(rutaActual): #recorremos la ruta actual
    name, extencion = os.path.splitext(rutaActual +nombre)  
    if extencion in ['.jpg', '.png', '.jpeg']:   #si la extencion es una de las que queremos
        foto=Image.open(rutaActual + "\\" + nombre)   #abrimos la imagen
        foto = foto.convert('RGB')                    #convertimos la imagen a RGB
        foto.save(f'{cont}_compessed_' + ".jpg", optimize=True, quality=20) #guardamos la imagen con la calidad deseada
        cont += 1                        #aumentamos el contador
        print(f'Imagen {nombre} comprimida') #imprimimos el nombre de la imagen comprimida
         
    
    

