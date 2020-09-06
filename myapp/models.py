from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=30,unique=True,blank=False)

    def __str__(self):
        return self.topic_name


class webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.name


    
class AccessaDetails(models.Model):
    webpage=models.ForeignKey(webpage,on_delete=models.CASCADE)
    datatime=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.datatime)
    
    