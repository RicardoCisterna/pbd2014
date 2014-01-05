# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    id = models.AutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.nombre)

class Comentario(models.Model):
    id = models.AutoField('ID', primary_key=True)
    creado = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    # Llaves foráneas
    user = models.ForeignKey(User)
    producto = models.ForeignKey(Producto)
    
    def __unicode__(self):
        return u'%s' % (self.nombre)
