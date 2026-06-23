"""my_new_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
import datetime
from django.conf.urls.static import static
from django.shortcuts import render
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('resume/', views.pdf, name='resume'),
    path('static/', views.static, name='static'),
]

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'test_temp.html', {'current_date': now})

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, docuemnt_root=settings.STATIC_ROOT)

# # from django.http import Http404, HttpResponse, HttpResponseRedirect
# import datetime
# from django.shortcuts import render #, render_to_response
# # from mysite.books.models import Book
# # from django.contrib import auth
# # from django.core.context_processors import csrf
# # from django.core.mail import send_mail

# def current_datetime(request):
#     now = datetime.datetime.now()
#     return render(request, 'test_temp.html', {'current_date': now})

# """
# def login(request):
#     c={}
#     c.update(csrf(request))
#     return render_to_response('login.html', c)

# def auth_view(request):
#     username = request.POST.get("username", '')
#     password = request.POST.get("password", '')
#     user = auth.authenticate(username=username, password=password)

#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')

# def loggedin(request):
#     return render_to_response('loggedin.html', {'full_name':request.user.username})

# def invalid_login(request):
#     return render_to_response("invalid_login.html")

# def logout(request):
#     auth.logout(request)
#     return render_to_response("logout.html")


# def book_list(request):
#     books = Book.objects.order_by('name')
#     return render(request, 'book_list.html', {'books': books})

# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)


# def hello(request):
#     return HttpResponse("Hello world, this is a simple response. There is no code." +
#     	"Other than what is from outside public libraries.")

# def display_meta(request):
#     values = request.META.items()
#     values.sort()
#     html = []
#     for k, v in values:
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))


# """