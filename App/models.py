from django.db import models

# Create your models here.


class Test(models.Model):
    col = models.CharField(max_length=100)

    def __str__(self):
        return self.col