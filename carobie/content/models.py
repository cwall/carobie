from django.db import models
from datetime import datetime

class Dossier(models.Model):
  title = models.CharField(max_lenth=250)
  subtitle = models.CharField(max_length=250)
  slug = models.SlugField(unique=True)
  date = models.DateField(auto_now=True)
  detail = models.TextField()
  publish = models.BooleanField()
  
  class Meta:
    ordering = ['-date']
    verbose_name_plural = 'Dossiers'
    get_latest_by = 'date'

  def __unicode__(self):
    return self.title

class Post(models.Model):
  content = models.CharField(max_length="140")
  creation = models.DateTimeField(auto_now=True, blank=True)