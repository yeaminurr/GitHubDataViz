from django.db import models
class fname(models.Model):
    name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.name

class userss(models.Model):
    #firstname = models.ForeignKey(fname,on_delete=models.CASCADE)
    firstname= models.CharField(max_length=264)
    lastname = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)
    def __str__(self):
        return self.firstname



# Create your models here.
