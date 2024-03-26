# Required Modules

from django.shortcuts import render
from django.contrib import messages
from ChatApp.models import SupportForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , UserChangeForm
from .forms import RegisterForm , EditProfile 

# Create your views here.

def home(req):
    user = req.user
    return render(req,'ChatApp/index.html')

def discover(req):
    return render(req,"ChatApp/discover.html")


def safety(req):
    return render(req,"ChatApp/safety.html")

def support(req):
    return render(req,"ChatApp/support.html")

def submittedSupport(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        phone = req.POST.get("phone")
        query = req.POST.get("query")
        # Saving to Database
        supportForm = SupportForm.objects.create(name=name,email=email,phoneNumber=phone,queryTitle=query)
        supportForm.save()
        print("Created")
        # Sending Email
        subject="Hey from LiveChat"
        message = f"Hey {name} , we have got your query and are working on it . As soon we are finished with your query , we will get in touch with you with this email !"
        fromEmail = "handasahil300@gmail.com"
        send_mail(subject=subject,message=message,from_email=fromEmail,recipient_list=[email],fail_silently=False)

    return render(req,"ChatApp/support.html")
def register(req):
    if req.method=="POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save() 
            messages.success(req,"You have Registered Successfully")
    else:
        form = RegisterForm()
    return render(req,"ChatApp/registrationForm.html",{"form":form})




def loginPage(req):
    if req.method=="POST":
        form = AuthenticationForm(request=req,data=req.POST)

        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_password = form.cleaned_data["password"]
            
            auth = authenticate(username=user_name,password=user_password)

            if auth is not None:
                login(req,auth)

                return render(req,"ChatApp/loggedIndex.html")
    else:
        form = AuthenticationForm()
    return render(req,"ChatApp/login.html",{"form":form})

def forgotPassword(req):
    if req.method=="POST":
        changePassword = PasswordChangeForm(user=req.user,data=req.POST)
        if changePassword.is_valid():
            changePassword.save()
    else:

        changePassword = PasswordChangeForm(user=req.user)
    return render(req,"ChatApp/changePassword.html",{"form":changePassword})

def submittedUser(req):
    return render(req,"ChatApp/userProfile.html")





def loggedInPage(req):
    return render(req,"ChatApp/loggedIndex.html")

def userProfile(req):
    if req.method == "POST":
        user = EditProfile(req.POST, instance=req.user)
        if user.is_valid():
            user.save()
            messages.success(req,"Your Profile has been changed Successfully")
    else:
        user = EditProfile(instance=req.user)

    return render(req, "ChatApp/userProfile.html", {"form": user,'user':req.user})
def logoutWebsite(req):
    logout(req)
    return render(req,"ChatApp/index.html")

def loggedIndex(req):
    return render(req,"ChatApp/loggedIndex.html")


def jobChat(req):
    return render(req,"ChatApp/jobChat.html")

def vehicalChat(req):
    return render(req,"ChatApp/vehicalChat.html")

def writers(req):
    return render(req,"ChatApp/writers.html")

def friends(req):
    return render(req,"ChatApp/friends.html")

def bodyBuilding(req):
    return render(req,"ChatApp/bodyBuilding.html")

def multiMedia(req):
    return render(req,"ChatApp/multimedia.html")

def medico(req):
    return render(req,"ChatApp/medico.html")

def techno(req):
    return render(req,"ChatApp/techno.html")