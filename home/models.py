from django.db import models
# makemigration means creatchange and store in file\
# migrate use for apply the panding changes created by migratioan


# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=112)
    email =models.CharField(max_length=112)
    phone =models.CharField(max_length=12)
    decs=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name