from django import forms
from django.forms import ModelForm
from models import Mutexs, Feedback	

class MutexSearchForm(ModelForm):
    class Meta:
    	model = Mutexs
    	fields = '__all__'

    mutexs = forms.CharField(max_length=500, label='') 
    # This sentence is just to put the 'label' widget there, so that it doesn't show any name in the template

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    name = forms.CharField(label='Your Name', required=True)
    company = forms.CharField(label='The company you work for', required=False)
    website = forms.URLField(label='Your Website', required=False)
    email = forms.EmailField(label='Your email address',required=True)
    message = forms.CharField(widget=forms.Textarea, label='Your feedback message', required=True)
    
    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words< 5:
            raise forms.ValidationError("Not enough words!")
        return message

# from captcha.fields import CaptchaField
# class CaptchaFeedbackForm(ModelForm):
#     message = forms.CharField(widget=forms.Textarea)
#     captcha = CaptchaField()

#     class Meta:
#         model = Feedback
#         fields = '__all__'        