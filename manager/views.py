from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import Post,Profile


def index(request):
    if request.user.is_authenticated:

        post=reversed(list(Post.objects.select_related('profile')))
        #print(request.user)
        if request.method=="POST":
            
            st=request.POST['status']
            
            pr=Profile.objects.filter(user=request.user)
            pro=''
            for p in pr:
                pro=p
            if 'img' in request.FILES:
                img=request.FILES['img']
                pos=Post.objects.create(written_text=st,profile=pro,img=img)
            else:
                pos=Post.objects.create(written_text=st,profile=pro)
            return render(request,'index.html',{'post':post})
    else:
        return redirect('login')    
    return render(request,'index.html',{'post':post})
def find_friends(request):
    # return HttpResponse("Hello world")
    user=User.objects.all()
    #user=user[1:]
    #print(user)
    return render(request,'find_friends.html',{"user":user})

def home(request):
    
    return redirect('login')

def login(request):
    
    if request.method=="POST":
        if 'password1' in request.POST.keys():
            print("yes this is signup")
            email=request.POST['email']
            un=email.split('@')
            un=un[0]
        
            p1=request.POST['password1']
            p2=request.POST['password2']
            if not p1==p2:
                messages.info(request,"password not matched")
                return render(request,'login2.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
            else:
                user=User.objects.create_user(username=un,password=p1,email=email)
                user.save()
                messages.info(request,"user created")
                return render(request,'update_profile.html')
            return render(request,'login2.html')
        
   
   
    
        if 'password' in request.POST.keys():
            
            username=request.POST['email']
            username=username.split("@")
            username=username[0]
            #print(username)
            password=request.POST['password']
            U=User.objects.filter(username=username)
            

            user=auth.authenticate(username=username,password=password)
            #print(user)
            if user is not None:
                auth.login(request,user)
               
                return redirect('index')
            else:
                messages.info(request,"incorrect Password or account not found")
                return render(request,'login2.html')
            
            
        
    return render(request,'login2.html')

def forget_password(request):
    return render(request,'forget_password.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    pr=Profile.objects.filter(user=request.user)
    for p in pr:
        pro=p
    return render(request,'profile.html',{'pro':pro})

def update_profile(request):
    return render(request,'update_profile.html')

def post(request):
    post=Post.objects.all()
    return render(request,'home.html',{'post':post})