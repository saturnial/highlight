from django.db import models

class Highlight(models.Model):
  user = models.ForeignKey(User)
  text = models.CharField(max_length=30)
  timestamp = models.DateTimeField(auto_now_add=True)

class User(models.Model):
  username = models.CharField(max_length=25)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()

  def __unicode__(self):
    return u"%s %s" % (self.first_name, self.last_name)
