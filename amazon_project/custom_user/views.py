from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('products:index')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:index')
    else:
        form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('products:index')
    
def simple_mail(request):
    send_mail(
        subject='That is  the subject',
        message='That is my message',
        from_email='jonesmichaelfordjour2@gmail.com',
        recipient_list=['franciskwadwofordjour@gmail.com']
    )
    return HttpResponse('Message sent')