from django.db import models


# Create your models here.
class Learner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    # grade=models.IntegerField(max_length=2)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
