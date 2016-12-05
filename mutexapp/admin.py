from django.contrib import admin
from models import Feedback, Mutexs, Userlog

# Register your models here.
class MutexsAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
    pass

class UserlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mutexs, MutexsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Userlog, UserlogAdmin)