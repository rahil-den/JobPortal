from django.db import models

# Create your models here.

class Signin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=120,null=False,blank=False)
    file=models.FileField(upload_to="userfile")

    class Meta:
        db_table="SIGNIN"
        verbose_name="Signin"
        verbose_name_plural="signin"
    def __str__(self):
        return self.name