from django.db import models

# Create your models here.

class Todomodel(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    date=models.DateField()
                            # here directly create a new file and save the image
    image=models.ImageField(upload_to="todoimages")
    