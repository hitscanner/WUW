from django.db import models

# Create y models here.
class Search_result(models.Model):
    title=models.CharField(max_length=100)
    poster=models.ImageField(blank=True)
    # like=models.ManyToManyField(User)
    youtube = models.BooleanField(default=False) 
    netflix = models.BooleanField(default=False)
    watcha = models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now = True)

# class calendar(models.Model):
