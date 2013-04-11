from django.db import models

class Highlight(models.Model):
  entry = models.ForeignKey(Entry) 
  text = models.TextField()
  score = models.IntergerField()
  

class Entry(models.Model):
  user = models.CharField()
  day = models.DateField(auto_now_add=True)
      



  
  
 
