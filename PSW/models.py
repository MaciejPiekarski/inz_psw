"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Commands(models.Model):
    ip = models.CharField('Adres IP', max_length=50)
    system = models.CharField('System operacyjny', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __str__(self):
        return self.ip