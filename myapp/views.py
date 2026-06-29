import datetime

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render


def home(request):
    user_ip = request.META.get("HTTP_X_REAL_IP", "unknown")
    return render(
        request,
        "home.html",
        {
            "right_now_utc": datetime.datetime.now(datetime.timezone.utc),
            "right_now": datetime.datetime.now(),
            "user_ip": user_ip,
        },
    )


def pdf(request):
    filepath = settings.BASE_DIR / "myapp" / "Joe_Buty_Resume.pdf"
    return FileResponse(open(filepath, "rb"), content_type="application/pdf")

def drone(request):
    return render(request, "drone.html")
