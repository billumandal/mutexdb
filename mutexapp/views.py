from django.shortcuts import render, render_to_response
from models import Mutexs, Feedback
from django.http import HttpResponseRedirect
from forms import MutexSearchForm

def noformsearch(request):
    if request.POST:
        search_term = request.POST['search']
        if search_term == '':
            print "This is search_term:", search_term
            
            Mutexs.objects.create(
                mutexs = request.POST['search_term']
            )
    else:
        search_term = ''

    mutexes = Mutexs.objects.filter(mutexs__icontains=search_term)

    return render(request, 'index3.html', {'mutexes' : mutexes})

def search(request):
    if request.GET:
        form = MutexSearchForm(request.GET)
        if form.is_valid():
            results = Mutexs.objects.filter(mutexs__icontains=search)
        else:
            results=[]

    else:
        form = MutexSearchForm()
        results=[]

    return render(request, 'index2.html',{
            'form':form,
            'results':results,
        })

def ajax_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        if search_text == '':
            Mutexs.objects.create(
                mutexs = request.POST['search_text']
            )
    else:
        search_text = ''

    mutexes = Mutexs.objects.filter(mutexs__icontains=search_text)

    return render_to_response('index2.html', {'mutexes' : mutexes})
    # return render_to_response('search_results.html', {'mutexes' : mutexes})

def mutexs(request):
    args = {}
    args.update(csrf(request))

    args['mutexs'] = Mutexs.objects.all()

def searchproject(request):
    some_variable = "This is a SearchProject View"
    if request.method == 'POST':
        form = MutexSearchForm(request.POST)
        if form.is_valid():
            mutexes = Mutexs.objects.filter(mutexs__icontains=form.cleaned_data.get('mutexs'))
            if mutexes == '':
                form.save()
                return HttpResponseRedirect('.')
            return render(request, 'index3.html', 
                {'form': form, 'mutexes':mutexes, 'some_variable': some_variable})
        
    else:
        nothing = [' ',]
        form = MutexSearchForm()
        return render(request, 'index3.html', 
                {'form': form, 'nothing':nothing, 'some_variable':some_variable})


    # if request.POST:
    #     search_term = request.POST['search']
    #     if search_term == '':
    #         Mutexs.objects.create(
    #             mutexs = request.POST['search_term']
    #         )
    # else:
    #     search_term = ''

    # mutexes = Mutexs.objects.filter(mutexs__icontains=search_term)

    # return render(request, 'search_results.html', {'mutexes' : mutexes})