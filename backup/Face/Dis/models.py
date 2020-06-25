from django.db import models

# Create your models here.
class Face(models.Model):
    id=models.CharField(max_length=10,default='aa',primary_key=True)
    a1=models.IntegerField(default=0)
    a2=models.IntegerField(default=0)
    a3=models.IntegerField(default=0)
    a4=models.IntegerField(default=0)
    a5=models.IntegerField(default=0)
    a6=models.IntegerField(default=0)
    a7=models.IntegerField(default=0)
    a8=models.IntegerField(default=0)
    a9=models.IntegerField(default=0)
    a10=models.IntegerField(default=0)