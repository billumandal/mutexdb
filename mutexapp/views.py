from django.shortcuts import render, render_to_response, redirect
from models import Mutexs
from django.http import HttpResponseRedirect, HttpResponse
from forms import MutexSearchForm, FeedbackForm
from django.core.mail import send_mail, BadHeaderError

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
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            company=form.cleaned_data['company']
            website=form.cleaned_data['website']
            from_email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            
            addfeedback = form.save() # saved data in database

            subject = "{n} has sent a feedback at your mutexdb website.".format(n=name,)
            email_body = """ 
                Name: {n},
                Company: {c}
                Website: {w}
                His email: {e}
                Message as below.
                ***********************
                {m}
                ***********************
                PS: You can also check the feedback in the admin interface.
            """.format(n=name, c=company, w=website, e=from_email, m=message,)
            try:
                send_mail(name,email_body, from_email, ['jonpeetarson@gmail.com'])
                thanks = "Thanks for you feedback."
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('../thanks')
    return render(request, "feedback.html", {'form':form})

def thanks(request):
    return HttpResponse("""
        <html>Thanks for you feedback. \n Click <a href='..'>here</a> to get back to homepage\n</html>

<script type='text/javascript'>   
function Redirect() 
{  
window.location='..'; 
} 
document.write('\n You will be redirected to a new page in 5 seconds'); 
setTimeout('Redirect()', 5000);   
</script>
""")