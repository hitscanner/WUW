from django.db import models
from django.contrib.auth.models import User 
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

    like_user_set = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='like_user_set',
                                        through='Like')
    def __str__(self):
        return '%d - %s' % (self.id,self.name)   
    
    @property
    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    moive = models.ForeignKey(Movie,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return '%s' % (self.moive.name)
# class calendar(models.Model):
