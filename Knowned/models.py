from django.db import models
from datetime import datetime



class investors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="",max_length=50)
    desc = models.CharField(default="",max_length=50)
    link = models.CharField(default="",max_length=100)
    image_link =models.CharField(default="",max_length=500)
   
    payment_choices = models.TextChoices("payment_choices", "Payment_done Payment_not_done")
    payment = models.CharField(choices=payment_choices.choices,max_length=20,default="Payment_not_done")

    def __str__(self):
        return self.name 






class About(models.Model):
    title = models.CharField(max_length=25)
    about_desc = models.TextField(default="")

    def __str__(self):
        return self.title+ " ----- "+self.about_desc[0:]
    