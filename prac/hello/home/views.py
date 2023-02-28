from django.shortcuts import render
from home.models import Register
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def registration(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        username=request.POST.get('uname')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        existing_users=Register.objects.all()
        x=True
        for i in existing_users:
            if i.username==username:
                x=False
        if x==True:
            if password1==password2:
                registration=Register(name=first_name,username=username,password=password1)
                registration.save()
            else:
                messages.info(request,'Password Not Matched')
        else:
            messages.info(request,'user exists')
    return render(request,'registration.html')
def login(request):
    username=request.POST.get('uname')
    password=request.POST.get('password')
    users=Register.objects.all()
    for i in users:
        if i.username==username and i.password==password:
            return render(request,'student.html',{'name':i.name,'uname':i.username})
            
    return render(request,'login.html')