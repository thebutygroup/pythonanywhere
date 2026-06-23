from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
import datetime

def home(request):
    ua = request.META.get('HTTP_X_REAL_IP', 'unknown')
    return render(request, 'home.html', {'right_now_utc':datetime.datetime.utcnow(), 'right_now':datetime.datetime.now(), 'user_ip':ua})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def pdf(request):
    filepath = os.path.join('/home/JoeButy/mysite/myapp/', 'Joe_Buty_Resume.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def my_view(request):
    return render(request, 'index.html')

def static():
    ...

"""


def newpage(request):
    return render(request, 'newpage.html')

def babynames(request):
    return render(request, 'babynames.html')

def babynames2(request):
    return render(request, 'babynames2.txt')


def visitor_email(request):
    if 'vemail' in request.GET:
        message = 'Your email: %r' % request.GET['vemail']
    else:
        message = 'Empty form.'
    return render(request, 'home.html', {'vemailmessage':message})

from django.http import HttpResponse, Http404
from datetime import datetime


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



def register_user(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            #.....
            return HttpResponseRedirect('home.html') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('home.html', {'form': form,})"""