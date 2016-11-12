from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def acc_login(request):
    if request.method=="POST":
        print request.POST
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request,user)
            return redirect('/')
        else:
            error="error"
            return render(request, "login.html",{"login_error":error})
    return render(request,"login.html")


@login_required
def index(request):
    return render(request,"index.html")

def acc_logout(requrst):
    logout(requrst)
    return redirect("/")