from django.db import models
from django.core.urlresolvers import reverse
from dashboard.division_model import Division

class District(models.Model):
    name=models.CharField(max_length=200,unique=True)
    district_code=models.CharField(max_length=200,unique=True)
    division_id=models.ForeignKey(Division)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
     return reverse('district_edit', kwargs={'pk': self.pk})