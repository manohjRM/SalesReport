from django.db import models
from django.db.models.fields import EmailField

class customer(models.Model):
    Company_name = models.CharField(max_length=150)
    Contact_Person = models.CharField(max_length=150)
    Designation = models.CharField(max_length=50)
    Mobile_num = models.CharField(max_length=10)
    Login_person = models.CharField(max_length=50)
    Existing_Customer = models.BooleanField(default="True")
    
    def __str__(self):
        return self.Company_name