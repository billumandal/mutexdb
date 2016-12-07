from django import forms
from django.forms import ModelForm
from models import Mutexs, Feedback	

class MutexSearchForm(ModelForm):
    class Meta:
    	model = Mutexs
    	fields = '__all__'

    mutexs = forms.CharField(max_length=500, label='') 
    # This sentence is just to put the 'label' widget there, so that it doesn't show any name in the template

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your Name', required=True)
    company = forms.CharField(label='The company you work for', required=False)
    website = forms.URLField(label='Your Website', required=False)
    email = forms.EmailField(label='Your email address',required=True)
    message = forms.CharField(widget=forms.Textarea, label='Your feedback message', required=True)
    

# from captcha.fields import CaptchaField
# class CaptchaFeedbackForm(ModelForm):
#     message = forms.CharField(widget=forms.Textarea)
#     captcha = CaptchaField()

#     class Meta:
#         model = Feedback
#         fields = '__all__'        