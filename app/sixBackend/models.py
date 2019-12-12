from django.db import models

# Create your models here.
class Bank(models.Model):
    location_name = models.CharField(max_length=100)

    def _str_(self):
        return(f" Bank {self.location_name}")