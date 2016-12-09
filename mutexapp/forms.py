from django import forms
from django.forms import ModelForm
from models import Mutexs, Feedback	

class MutexSearchForm(ModelForm):
    class Meta:
    	model = Mutexs
    	fields = '__all__'

    mutexs = forms.CharField(max_length=500, label='', required=False, widget=forms.TextInput(attrs={'class':'form-control',})) 
    # This sentence is just to put the 'label' widget there, so that it doesn't show any name in the template

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    name = forms.CharField(label='Your Name', required=True, widget=forms.TextInput(attrs={'class':'form-control',}))
    company = forms.CharField(label='The company you work for', required=False, widget=forms.TextInput(attrs={'class':'form-control',}))
    website = forms.URLField(label='Your Website', required=False, widget=forms.TextInput(attrs={'class':'form-control',}))
    email = forms.EmailField(label='Your email address',required=True, widget=forms.TextInput(attrs={'class':'form-control',}))
    message = forms.CharField(label='Your feedback message', required=True, widget=forms.Textarea(attrs={'class':'form-control',}))
    
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