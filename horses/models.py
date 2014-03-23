from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text
from django.db import models

colors = [
    'bay','gray','white','chestnut','black','dun','buckskin','palomino',
    'perlino','cremello','roan','champagne'
]

class Horse(models.Model):
    name     = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age      = models.IntegerField()
    weight   = models.DecimalField(max_digits=6,decimal_places=2)
    feet     = models.IntegerField()
    inches   = models.IntegerField()
    color    = models.CharField(max_length=100)
    breed    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def height(self):
        return smart_text('%s ft, %s in') % (self.feet,self.inches)

    def get_abosulte_url(self):
        return reverse('horses.views.horse_detail', args=[str(self.id)])