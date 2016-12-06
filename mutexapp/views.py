from django.shortcuts import render, render_to_response
from models import Mutexs, Feedback
from django.http import HttpResponseRedirect
from forms import MutexSearchForm

def searchproject(request):
    client_ip = get_client_ip(request)

    if request.method == 'POST':
        form = MutexSearchForm(request.POST)
        if form.is_valid():
            mutexes = Mutexs.objects.filter(mutexs__icontains=form.cleaned_data.get('mutexs'))
            if mutexes == '':
                form.save()
                return HttpResponseRedirect('.')
            return render(request, 'index3.html', 
                {'form': form, 'client_ip':client_ip, 'mutexes':mutexes,})
        
    else:
        nothing = [' ',]
        form = MutexSearchForm()
        return render(request, 'index3.html', 
                {'form': form, 'client_ip':client_ip, 'nothing':nothing, })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip

def feedback(request):
    pass