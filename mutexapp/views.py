from django.shortcuts import render, render_to_response
from models import Mutexs, Feedback
from django.http import HttpResponseRedirect
from forms import MutexSearchForm

def searchproject(request):
    some_variable = "This is a SearchProject View"
    ip = get_client_ip(request)

    if request.method == 'POST':
        form = MutexSearchForm(request.POST)
        if form.is_valid():
            mutexes = Mutexs.objects.filter(mutexs__icontains=form.cleaned_data.get('mutexs'))
            if mutexes == '':
                form.save()
                return HttpResponseRedirect('.')
            return render(request, 'index3.html', 
                {'form': form, 'ip':ip, 'mutexes':mutexes, 'some_variable': some_variable})
        
    else:
        nothing = [' ',]
        form = MutexSearchForm()
        return render(request, 'index3.html', 
                {'form': form, 'ip':ip, 'nothing':nothing, 'some_variable':some_variable})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip