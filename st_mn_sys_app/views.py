from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from st_mn_sys_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDemo(request):
    return render(request, 'demo.html')
def showLogin(request):
    return render(request, 'login.html')
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == "1" : return HttpResponseRedirect('admin_page')
            elif user.user_type == "2": return HttpResponseRedirect('staff_page')
            else: return HttpResponseRedirect('teacher_page')
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")