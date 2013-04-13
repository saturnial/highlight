from django import forms

import models

class CreateHighlight(forms.ModelForm):
  class Meta:
    model = models.Highlight
    fields = ('highlight_text',)
