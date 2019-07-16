from django.db import models

# Create y models here.
class Search_result(models.Model):
    title=models.CharField(max_length=100)
    poster=models.ImageField(blank=True)
    like=models.IntegerField(blank=True)
    actor=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    OST=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now = True)

class calendar(models.Model):

class joahyo(models.Model):