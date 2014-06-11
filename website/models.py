from django.db import models

# Create your models here.
class SubService(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=128)
    subservices = models.ManyToManyField(SubService)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.title
