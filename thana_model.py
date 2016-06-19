from django.db import models
from django.core.urlresolvers import reverse
from dashboard.division_model import Division
from .district_model import District

class Thana(models.Model):
    name=models.CharField(max_length=200,unique=True)
    thana_code=models.CharField(max_length=200,unique=True)
    division_id=models.ForeignKey(Division)
    district_id=models.ForeignKey(District)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('thana_edit', kwargs={'pk': self.pk})


