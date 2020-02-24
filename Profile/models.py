from django.db import models
from django.utils import timezone

class ModelCiudad(models.Model):
    ciudad = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Ciudad'

class ModelGenero(models.Model):
    genero = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Genero'

class ModelOcupacion(models.Model):
    ocupacion = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Ocupacion'
    
class ModelEstado(models.Model):
    estado = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Estado'
    
class ModelEstadoCivil(models.Model):
    estado_civil = models.CharField(max_length=254,null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'EstadoCivil'


class Profile(models.Model):
    nombre = models.CharField(max_length=254,null=False)
    apellido_paterno = models.CharField(max_length=254,null=False)
    apellido_materno = models.CharField(max_length=254,null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(ModelCiudad,on_delete=models.CASCADE)
    genero = models.ForeignKey(ModelGenero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(ModelOcupacion,on_delete=models.CASCADE)
    estado= models.ForeignKey(ModelEstado,on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(ModelEstadoCivil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Profile'
        
    
    

# Create your models here.
