from django.db import models

# Create y models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    poster=models.TextField(blank=True)
    # like=models.ManyToManyField(User)
    netflix = models.BooleanField(default=False)
    watcha = models.BooleanField(default=False)

    action=models.BooleanField(default=False)
    fantasy=models.BooleanField(default=False)
    thriller=models.BooleanField(default=False)
    comedy=models.BooleanField(default=False)
    romance=models.BooleanField(default=False)
    drama=models.BooleanField(default=False)
    sf=models.BooleanField(default=False)
    horror=models.BooleanField(default=False)
    animation=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

# class calendar(models.Model):
