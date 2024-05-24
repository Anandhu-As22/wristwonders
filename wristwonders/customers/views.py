from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from .forms import Loginform,RegisterForm


# Create your views here.


def Home_page(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    return redirect('user-login.html')


# user login
def user_login(request):
    print('hai')
    if request.method == "POST":
        print('method')
        form = Loginform(request.POST)
        if form.is_valid():
            email =form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email = email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid email or password')
    else:
        form =Loginform()
    return render(request,'user-login.html',{'form':form})
            

        
 


    
# user signup

def user_signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('user-login')
    else:
        form = RegisterForm()


    return render(request,'user-signup.html',{'form':form})