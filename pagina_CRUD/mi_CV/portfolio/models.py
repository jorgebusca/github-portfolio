from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
# Create your models here.
class projects(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/imagen/")
    url = URLField(blank=True)
    