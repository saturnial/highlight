from django.db import models
from django.contrib.auth.models import User

class Highlight(models.Model):
  user = models.ForeignKey(User)
  highlight_text = models.CharField(max_length=30)
  timestamp = models.DateTimeField(auto_now_add=True, editable=False)

  class Meta:
    get_latest_by = 'timestamp'
    ordering = ["-timestamp"]

  def __unicode__(self):
    return self.highlight_text
