from django.db import models


# Create your models here.
class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='items_images',  unique=True, null=False)

    def __str__(self):
        return str(self.id) + " : " + self.name + " : " + str(self.price)
