from django import forms

class MutexSearchForm(forms.Form):
    mutexs = models.CharField(label='search', max_length=500) 