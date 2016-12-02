from django.shortcuts import render, render_to_response
from models import Mutexs, Feedback
from django.http import HttpResponseRedirect
from forms import MutexSearchForm

def searchproject(request):
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
            results = Mutexs.objects.filter(name__icontains=search)
        else:
            results=[]

    else:
        form = MutexSearchForm()
        results=[]

    return render_to_response('search.html', RequestContext(request, {
            'form':form,
            'results':results,
        })
    )

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

# def mutexs(request):
#     args = {}
#     args.update(csrf(request))

#     args['mutexs'] = Mutexs.objects.all()

def show_header(request):
    return render(request, 'header.html')
<<<<<<< HEAD
=======

def searchproject(request):

    if request.method == 'POST':
        form = MutexSearchForm(request.POST)
        if form.is_valid():
            mutexes = Mutexs.objects.filter(name__icontains=search)
            if mutexes == '':
                form.save()
                return HttpResponseRedirect('.')
        else:
            form = MutexSearchForm()
            mutexes=[]
            return render(request, 'index3.html', 
                {'form': form})

        return render(request, 'index3.html', 
            {'form': form, 'mutexes':mutexes,})
    else:
        form1 = MutexSearchForm(request.GET)
        # mutexes=[]
        mutexes=''
        return render(request, 'index3.html', {'form':form1})


    # if request.POST:
    #     search_term = request.POST['search']
    #     if search_term == '':
    #         Mutexs.objects.create(
    #             mutexs = request.POST['search_term']
    #         )
    # else:
    #     search_term = ''

    # mutexes = Mutexs.objects.filter(mutexs__icontains=search_term)

    # return render(request, 'index3.html', {'mutexes' : mutexes})