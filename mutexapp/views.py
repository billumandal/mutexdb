from django.shortcuts import render, render_to_response
from models import Mutexs

def search(request):
    if request.GET:
        form = MutexsSearchForm(request.GET)
        if form.is_valid():
            result = Mutexs.objects.filter(name__icontains=searchterm)
        else:
            results=[]

    else:
        form = MutexsSearchForm()
        results=[]

    return render_to_response('search.html', RequestContext(request, {
        # Should I put index.html here rather than search.html
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

    mutexes = Mutexs.objects.filter(mutexs__contains=search_text)

    return render_to_response('index.html', {'mutexes' : mutexes})
    return render_to_response('search_results.html', {'mutexes' : mutexes})

def mutexs(request):
    args = {}
    args.update(csrf(request))

    args['mutexs'] = Mutexs.objects.all()

def show_header(request):
    return render(request, 'header.html')