from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class items(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    offer = models.BooleanField(default=False)
    qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.CharField(max_length=20)
    item = models.CharField(max_length=200)