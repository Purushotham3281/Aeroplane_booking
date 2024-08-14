from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=20)
    source=models.CharField(max_length=20)
    destiny=models.CharField(max_length=20)
    date=models.DateField()
    Price=models.IntegerField()

    def __str__(self):
        return self.name