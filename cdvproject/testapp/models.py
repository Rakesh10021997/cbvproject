from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
    Company_Name=models.CharField(max_length=50)
    CEO=models.CharField(max_length=50)
    Location=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('list',kwargs={'pk':self.pk})
