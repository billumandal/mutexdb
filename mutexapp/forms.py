from django import forms
from models import Mutexs, Feedback	

class MutexSearchForm(forms.Form):
    mutexs = forms.CharField(label='search', max_length=500) 