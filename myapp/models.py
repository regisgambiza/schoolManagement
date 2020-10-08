from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Learner(models.Model):
    first_name = models.CharField(max_length=30,default='')
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    grade = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Learner, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
