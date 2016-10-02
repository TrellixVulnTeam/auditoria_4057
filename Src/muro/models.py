from django.db import models
from evaluacion.models import *
from django.contrib.auth.models import User

class Trabajo(models.Model):
	empresa = models.ForeignKey(User, related_name='usuario_empresa', on_delete=models.CASCADE)
	auditor = models.ForeignKey(User, related_name='usuario_auditor', on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(Evaluacion)
	creacion = models.DateTimeField(auto_now_add=True)
	inicio = models.DateTimeField(null=True, blank=True)
	estado = models.ForeignKey('Estado')

	def __str__(self):
		return self.empresa.first_name + ' - ' + self.evaluacion.getNombre() + ' - ' + self.evaluacion.getFecha()

class Estado(models.Model):
	titulo = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.titulo