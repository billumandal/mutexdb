from django import forms
from models import Mutexs, Feedback	

class MutexSearchForm(forms.Form):
    mutexs = forms.CharField(label='', max_length=500) 

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='')
    company = forms.CharField(max_length=100, label='')
    website = forms.CharField(max_length=70,label='')
    email_address = forms.EmailField(max_length=100, label='')
    message = forms.CharField(max_length=500, label='')
    