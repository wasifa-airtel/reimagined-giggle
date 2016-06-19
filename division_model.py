from django.db import models
from django.core.urlresolvers import reverse

class Division(models.Model):
    name=models.CharField(max_length=200,unique=True)
    division_code=models.CharField(max_length=200,unique=True)
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('division_edit', kwargs={'pk': self.pk})
