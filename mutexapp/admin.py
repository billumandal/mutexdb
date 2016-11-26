from django.contrib import admin
from models import Feedback, Mutexs

# Register your models here.
class MutexsAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mutexs, MutexsAdmin)
admin.site.register(Feedback, FeedbackAdmin)