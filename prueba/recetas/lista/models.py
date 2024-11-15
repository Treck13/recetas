from django.db import models

class Lista(models.Model):
    receta = models.CharField(max_length=100)
    chef = models.CharField(max_length=100)
    comida = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    
