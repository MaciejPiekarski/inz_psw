"""
Definition of models.
"""

from django.db import models
from django.forms import widgets
from django.contrib.auth.models import User

# Create your models here.
class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=25)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
    user = models.ForeignKey(User, verbose_name="Użytkownik")
    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __str__(self):
        return self.ip