"""
Definition of models.
"""

from django.db import models
<<<<<<< HEAD

# Create your models here.
class Commands(models.Model):
    ip = models.CharField('Adres IP', max_length=50)
    system = models.CharField('System operacyjny', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
=======
from django.forms import widgets
from django.contrib.auth.models import User

# Create your models here.
class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=25)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
    user = models.ForeignKey(User, verbose_name="Użytkownik")

>>>>>>> refs/remotes/origin/pr/1
    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'
    def __str__(self):
        return self.ip
