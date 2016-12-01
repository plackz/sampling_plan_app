"""
comes built in
from django.db import models

# Create your models here.
"""
from django.db import models

class SampleLotCode(models.Model):
    lot_max = models.IntegerField()
    inspection_level = models.CharField(max_length=3)
    sample_code = models.CharField(max_length=1)
    def __str__(self):
        return self.inspection_level
        return self.sample_code # maybe not needed? tutorial only had one CharField

class SampleSize(models.Model):
    inspection_type = models.CharField(max_length=25)
    sample_code_letter = models.ForeignKey(SampleLotCode, on_delete=models.CASCADE)
    sample_size = models.IntegerField()
    aql = models.DecimalField(max_digits=100, decimal_places=1)
    accept = models.IntegerField()
    reject = models.IntegerField()
    def __str__(self):
        return self.inspection_type
        # not sure if we need one for sample_code
