from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=50000)
    date = models.DateField()
    
    def __str__(self):
        return self.title