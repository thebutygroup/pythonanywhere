from django.shortcuts import render
import datetime

def resume(request):
    return render(request, 'resume/templates/Joseph Buty Resume HTML.html', {'right_now_utc':datetime.datetime.utcnow(), 'right_now':datetime.datetime.now()})

    # Create your views here