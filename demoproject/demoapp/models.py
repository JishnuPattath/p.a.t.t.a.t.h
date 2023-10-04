from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.name

class make(models.Model):
    Name1 = models.CharField(max_length=250)
    Image1 = models.ImageField(upload_to='pics')
    details = models.TextField()

    def __str__(self):
        return self.Name1