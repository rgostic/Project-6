from django.db import models

# Create your models here.
class Mineral(models.Model):
	name = models.CharField(max_length=100)
	image_filename = models.CharField(max_length=200)
	image_caption = models.TextField()
	category = models.TextField()
	formula = models.TextField()
	strunz_classification = models.TextField()
	color = models.TextField()
	crystal_system = models.TextField()
	unit_cell = models.TextField()
	crystal_symmetry = models.TextField()
	cleavage = models.TextField()
	mohs_scale_hardness = models.TextField()
	luster = models.TextField()
	streak = models.TextField()
	diaphaneity = models.TextField()
	optical_properties = models.TextField()
	refractive_index = models.TextField()
	crystal_habit = models.TextField()
	specific_gravity = models.TextField()
	group = models.TextField()