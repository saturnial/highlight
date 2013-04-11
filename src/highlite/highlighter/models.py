from django.db import models

class Entry(models.Model):
  user = models.CharField(max_length=50)
  day = models.DateField(auto_now_add=True)
 
class Highlight(models.Model):
  entry = models.ForeignKey(Entry) 
  text = models.TextField()
  score = models.IntegerField()
