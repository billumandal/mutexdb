from django import forms
from django.forms import ModelForm
from models import Mutexs, Feedback	

class MutexSearchForm(ModelForm):
    class Meta:
    	model = Mutexs
    	fields = '__all__'

    mutexs = forms.CharField(max_length=500, label='') 
    # This sentence is just to put the 'label' widget there, 
    # so that it doesn't show any name in the template

class FeedbackForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
		model = Feedback
		fields = '__all__'