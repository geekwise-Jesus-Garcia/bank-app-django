from django.db import models

# Create your models here.
class Bank(models.Model):
    location_name = models.CharField(max_length=100)

    def _str_(self):
        return(f" Bank {self.location_name}")

 class Account(models.Model):
     account_options = (
         ('account', 'ACCOUNT')
         ('checking', 'CHECKING')
         ('balance', 'BALANCE')
     )

     product_username = models.CharField(max_length=100)
     product_email = models.EmailField(max_length=100)
     product_options = models.CharField(max_length=8)

     def _str_(self):
         return(f"Account Name {self.product_username} Account Email {self.product_email}")