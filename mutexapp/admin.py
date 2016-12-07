from django.contrib import admin
from models import Mutexs, Userlog, Feedback
from forms import FeedbackForm

# Register your models here.
class MutexsAdmin(admin.ModelAdmin):
    search_fields = ('mutexs',)

class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ['name', 'company', 'website', 'email_address',]
    # form = FeedbackForm()

class UserlogAdmin(admin.ModelAdmin):
    list_display = ('id','visiting_time', 'client_ip')
    search_fields = ['client_ip',]
    list_per_page = 15

admin.site.register(Mutexs, MutexsAdmin)
admin.site.register(Userlog, UserlogAdmin)
admin.site.register(Feedback, FeedbackAdmin)