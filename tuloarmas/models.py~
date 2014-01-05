# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

#class Producto(models.Model):
#    id = models.AutoField('ID', primary_key=True)
#    nombre = models.CharField(max_length=255)
#    descripcion = models.TextField()
#    precio = models.IntegerField()

#    def __unicode__(self):
#        return u'%s' % (self.nombre)

#class Comentario(models.Model):
#    id = models.AutoField('ID', primary_key=True)
#    creado = models.DateTimeField(auto_now_add=True)
#    texto = models.TextField()

    # Llaves foráneas
#    Usuario = models.ForeignKey(Usuario)
#    producto = models.ForeignKey(Producto)
    
#    def __unicode__(self):
#        return u'%s' % (self.nombre)
class Auditoria(models.Model):
    id = models.AutoField('ID', primary_key=True) 
    time_stamp = models.DateTimeField(auto_now_add=True)
    tabla = models.CharField(max_length=255)
    filas = models.CharField(max_length=255)
    usuario_accion= models.CharField(max_length=255)
    valor_anterior = models.TextField()
    nuevo_valor = models.TextField()
    operacion = models.CharField(max_length=255)

class Usuario (models.Model):
    id = models.AutoField('ID', primary_key=True) 
    tipo_usuario = models.CharField(max_length=1)
    nombre_usuario= models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    correo_usuario =  models.EmailField()
    direccion_usuario = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular_usuario = models.CharField(max_length=20)
    rut_usuario = models.CharField(max_length=20)
    estado_usuario= models.CharField(max_length=20)
    fecha_ingreso = models.DateField()

class Categoria(models.Model): 
    id = models.AutoField('ID', primary_key=True)
    nombre_categoria=models.CharField(max_length=255)
    #llaves foraneas
    raiz = models.ForeignKey('self')

class Material(models.Model):
    id = models.AutoField('ID', primary_key=True) 
    nombre_material= models.CharField(max_length=255)
    descripcion_material = models.TextField()
    tipo_material = models.CharField(max_length=1)
    marca=  models.CharField(max_length=255)
    modelo= models.CharField(max_length=255)
    imagen_material =  models.ImageField(upload_to='/tmp')
    #llaves foreaneas
    categoria = models.ForeignKey(Categoria)

class Cotizacion(models.Model):
    id = models.AutoField('ID', primary_key=True) 
    fecha_cotizacion=models.DateField(auto_now_add=True)    
    #llaves foraneas    
    usuario = models.ForeignKey(Usuario)
    
    
class Proveedor_material (models.Model):
    id  = models.AutoField('ID', primary_key=True) 
    precio_material = models.IntegerField()
    visibilidad = models.CharField(max_length=255)
    codigo_proveedor_material = models.CharField(max_length=255)
    #llaves foraneas
    Usuario = models.ForeignKey(Usuario)
    material = models.ForeignKey(Material)

class Envio (models.Model):
    id = models.AutoField('ID', primary_key=True) 
    #llaves foraneas
    Usuario = models.ForeignKey(Usuario)
    cotizacion = models.ForeignKey(Cotizacion)
    material= models.ForeignKey(Material)

class Detalle_cotizacion (models.Model):
    cantidad_material =  models.IntegerField()
    #llaves foraneas
    cotizacion = models.ForeignKey(Cotizacion, unique=True)
    material = models.ForeignKey(Material, unique=True)
    
class Caracteristicas(models.Model):
    id = models.AutoField('ID', primary_key=True)
    nombre_caracterisitica= models.CharField(max_length=255)
    descripcion_caracterisiticas = models.TextField() 
     
class Caracteristicas_material(models.Model):
    id = models.AutoField('ID', primary_key=True)
    #llave foraneas
    caracterisiticas = models.ForeignKey(Caracteristicas, unique=True)
    material = models.ForeignKey(Material, unique=True)
      
class Tutorial(models.Model):
    id =models.AutoField('ID', primary_key=True)
    video = models.URLField()
    nombre_tutorial = models.CharField(max_length=255)
    descripcion_tutorial =  models.TextField()
    imagen_tutorial = models.ImageField(upload_to='/tmp')
    #llaves foraneas
    Usuario = models.ForeignKey(Usuario)
    categoria = models.ForeignKey(Categoria)

class Comentario (models.Model):
    cuerpo= models.TextField()
    #llaves foraneas
    Usuario = models.ForeignKey(Usuario, unique=True)
    tutorial = models.ForeignKey(Tutorial, unique=True)


class Notificacion (models.Model):
    id =models.AutoField('ID', primary_key=True)
    tipo_notificacion = models.CharField(max_length=255)
    usaurio_cambio=models.CharField(max_length=255)
    fecha_accion = models.DateField()
    #llaves foraneas
    Usuario = models.ForeignKey(Usuario)

class Proceso(models.Model):
    id =models.AutoField('ID', primary_key=True)
    nombre_proceso= models.CharField(max_length=255)
    descripcion_proceso = models.TextField()
    hh = models.IntegerField()
    #llaves foraneas
    tutorial = models.ForeignKey(Tutorial,on_delete=models.PROTECT)
    material = models.ForeignKey(Material)

class Consumo (models.Model):
    id =models.AutoField('ID', primary_key=True)
    cantidad_consumo = models.IntegerField()
    #llaves foraneas
    proceso = models.ForeignKey(Proceso)
    material = models.ForeignKey(Material) 


class Flujo (models.Model):
    tiempo_espera = models.IntegerField()
    descripcion_flujo = models.IntegerField()
    #llaves foraneas
 
class proceso_flujo(models.Model):
    id= models.AutoField('ID', primary_key=True)  
    #llaves foraneas
    flujo = models.ForeignKey(Flujo)
    proceso = models.ForeignKey(Proceso)  

class Herramienta (models.Model):
    id= models.AutoField('ID', primary_key=True)
    nombre_herramienta = models.CharField(max_length=255)
    descripcion_herrmienta =  models.IntegerField()
    imagen_herrmienta =   models.ImageField(upload_to='/tmp')  

class Uso_herramienta (models.Model):
    id= models.AutoField('ID', primary_key=True)
    #llaves foraneas
    material = models.ForeignKey(Material)
    proceso = models.ForeignKey(Proceso)  





class Compone_A(models.Model):
    #id = models.AutoField('ID', primary_key=True) 
    material = models.ForeignKey(Material,primary_key=True)
    otro=descripcion_herrmienta =  models.IntegerField()
    nombre_material1= models.CharField(max_length=255)
    descripcion_material = models.TextField()
    tipo_material = models.CharField(max_length=1)
    marca=  models.CharField(max_length=255)
    modelo= models.CharField(max_length=255)
    imagen_material =  models.ImageField(upload_to='/tmp')
    #llaves foreaneas

class Compuesto_de(models.Model):
    #id = models.AutoField('ID', primary_key=True) 
    material = models.OneToOneField(Material,primary_key=True)
    nombre_material2= models.CharField(max_length=255)
    descripcion_material = models.TextField()
    tipo_material = models.CharField(max_length=1)
    marca=  models.CharField(max_length=255)
    modelo= models.CharField(max_length=255)
    imagen_material =  models.ImageField(upload_to='/tmp')
    #llaves foreaneas


class Composicion (models.Model):
    #llaves foranea
    compuesto_de = models.ForeignKey(Compuesto_de, primary_key=True)
    compone_a = models.ForeignKey(Compone_A, primary_key=True)
