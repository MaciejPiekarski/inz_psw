"""
Definition of models.
"""

from django import forms
from django.db import models
from django.forms import widgets

# Create your models here.
class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=50)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')

    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __str__(self):
        return self.ip