from django.db import models

# Create your models here.
class Contact1(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    phone = models.TextField()
    state = models.TextField()
    zip = models.CharField(max_length=6)
    city = models.TextField()
    date = models.DateField()
    File_image = models.FileField(upload_to="document/",max_length=250,null=True,default=None)
    
    def __str__(self):
        return self.name