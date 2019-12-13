from django.db import models

# Create your models here.


class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    Slug = models.CharField(max_length=200,unique=True)
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    Content = models.TextField()
    Time = models.DateField()

    def __str__(self):
        return  self.Title + ' By ' + self.Author 

    