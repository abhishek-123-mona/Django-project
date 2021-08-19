# I have created this file -------------abhishek>>>>>>>>>>>>>>>>>
 
# from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    content={
        "variable1":"Abhishek",
        "variable2":"sharma"
    }
    return render(request,'index.html')


def about(request):
    # return HttpResponse("this is a aboutt")
    return render(request,'About.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        decs=request.POST.get('decs')
        contact=Contact(name=name,email=email,phone=phone,decs=decs,date=datetime.today())
        contact.save() 
    # return HttpResponse("this is contact")
    return render(request,'Contact.html') 


def service(request):
    # return HttpResponse("this is MyINfo")
    return render(request,'Service.html')
