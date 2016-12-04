from django.forms import ModelForm
from models import Mutexs, Feedback	

class MutexSearchForm(ModelForm):
    class Meta:
    	model = Mutexs
    	fields = '__all__'

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'