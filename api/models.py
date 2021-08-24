from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Car(models.Model):
	make = models.CharField(max_length=255)
	model = models.CharField(max_length=255)
	avg_rating = models.FloatField(null=True, blank=True, default=0)
	rates_number = models.IntegerField(null=True, blank=True, default=0)
	ratings = ArrayField(models.FloatField(null=True, blank=True), default=list)

	def __str__(self):
		return self.make + ' ' + self.model
