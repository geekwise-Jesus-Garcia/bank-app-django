from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)

    def _str_(self):
        return(f" Bank {self.bank_name}")



class Account(models.Model):
    account_options = (
        ('account', 'ACCOUNT'),
        ('checking', 'CHECKING'),
        ('balance', 'BALANCE'),
     )
     
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    options = models.CharField(max_length=8)

    def _str_(self):
        return(f"Account Name {self.username} Account Email {self.email}")

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

    def _str_(self):
        return(f"Customer Name {self.customer_name}")


class Product(models.Model):
    product_option = (
        ('loan', 'LOAN'),
        ('credit', 'CREDIT'),
        ('cd', 'CD'),
    )

    option = models.CharField(max_length=100)


    def _str_(self):
        return(f"Type {self.product_option}")