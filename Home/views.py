from django.shortcuts import render,redirect
from.models import sign_up,sign_up_cater,catering_info
import time
from django.contrib import messages
from django.http import HttpResponse

def home(request): 
    return render(request,'main.html')
def home1(request): 
    return render(request,'main1.html')

def cateringinfo(request):
    if request.method == 'POST':
        print("Received POST request")  # Check if this prints
        # uname = request.POST['name']
        uname=request.POST['name']
        address=request.POST['Address']
        menu=request.POST['Menu']
        cuisine=request.POST['Cuisine']
        availability=request.POST['Availability']
        experience=request.POST['Experience']
        additionalservices=request.POST['Additionalservices']
        about=request.POST['About']
        #   gallery=request.POST['Gallery']

        object=catering_info()
        object.Cname=uname
        object.Address=address
        object.Menu=menu
        object.Cuisine=cuisine
        object.Availability=availability
        object.Experience=experience
        object.Additionalservices=additionalservices
        object.About=about
        #   object.Gallery=gallery
        object.save()  
    return render(request,'cateringinfo.html')
# def login(request):
#     a=0
#     if request.method == "POST":
#         user_login = request.POST['username1']
#         pass_login = request.POST['password1']
#         if sign_up.objects.filter(Pass=pass_login).exists() and sign_up.objects.filter(Uname=user_login).exists():
#             messages.success(request, "Login successful! Redirecting in 4 seconds...")
#             a=1
#             return render(request, 'main.html', {'redirect_url': 'main.html'})
            
#         elif sign_up_cater.objects.filter(Pass=pass_login).exists() and sign_up_cater.objects.filter(Uname=user_login).exists():
#             a=1
#             messages.success(request, "Login successful! Redirecting in 4 seconds...")
            
#             time.sleep(4)
#             return redirect('cateringinfo.html')
        
#         else: 
#            a=1
#            messages.error(request, "Invalid userid or password")
        
#     return render(request,'login.html',{'a':a})

def login(request):
    if request.method == "POST":
        user_login = request.POST.get('username1', '')  # Default empty string
        pass_login = request.POST.get('password1', '')

        if sign_up.objects.filter(Uname=user_login, Pass=pass_login).exists():
            messages.success(request, "Login successful! ")
            return render (request,'main1.html')  # Redirect to your main view

        elif sign_up_cater.objects.filter(Uname=user_login, Pass=pass_login).exists():
            messages.success(request, "Login successful! ")
            time.sleep(4)  # Caution with time.sleep in production
            return redirect('cateringinfo.html')  # Redirect to your catering view

        else:
            messages.error(request, "Invalid username or password")
            return redirect('login.html')
   
    
    return render(request, 'login.html')

def signup(request):
         if request.method=='POST':
              
            uname=request.POST['uname']
            mail=request.POST['mail']
            phone=request.POST['phone']
            password=request.POST['pass']
            cpassword=request.POST['cpass']

            object=sign_up()
            object.Uname=uname
            object.Mailid=mail
            object.Phone=phone
            object.Pass=password
            object.Cpass=cpassword
            object.save()
         return render(request, 'signup.html')
def index(request):
    return render(request,'index.html')
def caterersignup(request):
    if request.method=='POST':
              
            uname=request.POST['uname']
            mail=request.POST['mail']
            phone=request.POST['phone']
            password=request.POST['pass']
            cpassword=request.POST['cpass']

            object=sign_up_cater()
            object.Uname=uname
            object.Mailid=mail
            object.Phone=phone
            object.Pass=password
            object.Cpass=cpassword
            object.save()
    return render(request,'caterersignup.html')
def booking1(request):
    return render(request,'booking1.html')
def booking2(request):
    return render(request,'booking2.html')
def booking3(request):
    return render(request,'booking3.html')
def booking4(request):
    return render(request,'booking4.html')
def booking5(request):
    return render(request,'booking5.html')
def booking6(request):
    return render(request,'booking6.html')
def booking7(request):
    return render(request,'booking7.html')
def booking8(request):
    return render(request,'booking8.html')
def booking9(request):
    return render(request,'booking9.html')
def booking10(request):
    return render(request,'booking10.html')
def booking11(request):
    return render(request,'booking11.html')
def booking12(request):
    return render(request,'booking12.html')
def booking13(request):
    return render(request,'booking13.html')