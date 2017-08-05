from django.db import models

# Create your models here.


class Flight(models.Model):
    price = models.IntegerField(default=0.00)

    def __unicode__(self):
        return self.price