from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    offer = models.BooleanField(default=False)