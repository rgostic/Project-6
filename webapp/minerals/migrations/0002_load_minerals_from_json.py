# Generated by Django A.B on YYYY-MM-DD HH:MM
from django.db import migrations
import os.path
import json
def load_data(apps, schema_editor):
	# this is how you want to load your Model class in a migration.
	
	# yours might look more like this.
	# Assuming your app_name is minerals in your project.
    Mineral = apps.get_model('minerals', 'Mineral')
    filePath = os.path.join(os.path.dirname(__file__), os.pardir,os.pardir, os.pardir, 'data\\minerals.json')
    file = open(filePath, encoding="utf8")
    fileJson = file.read()
    mineralObjects = json.loads(fileJson)
    for mineral in mineralObjects:
        Mineral.objects.create(
            name = mineral["name"],
            image_filename = mineral["image filename"],
            image_caption = mineral["image caption"],
            category = mineral.get("category", ""),
            formula = mineral.get("formula", ""),
            strunz_classification = mineral.get("strunz classification", ""),
            color = mineral.get("color", ""),
            crystal_system = mineral.get("crystal system", ""),
            unit_cell = mineral.get("unit cell", ""),
            crystal_symmetry = mineral.get("crystal symmerty", ""),
            cleavage = mineral.get("cleavage", ""),
            mohs_scale_hardness = mineral.get("mohs scale hardness", ""),
            luster = mineral.get("luster", ""),
            streak = mineral.get("streak", ""),
            diaphaneity = mineral.get("diaphaneity", ""),
            optical_properties = mineral.get("optical properties", ""),
            refractive_index = mineral.get("refractive index", ""),
            crystal_habit = mineral.get("crystal habit", ""),
            specific_gravity = mineral.get("specific gravity", ""),
            group = mineral.get("group", "")
        )

class Migration(migrations.Migration):
    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(load_data, reverse_code=migrations.RunPython.noop),
    ]



