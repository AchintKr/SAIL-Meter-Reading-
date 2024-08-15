from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User 
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from home.form import ContactForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Contact1
from django.contrib import messages

#@login_required(login_url='home')
def index(request):
    # if request.user.is_anonymous:
    #     return render(request,'index.html')
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,'base.html',{'var':username})
        else:
            messages.error(request, "Enter Correct Credentials .")
            return render(request,'index.html')
    return render(request,'index.html')
   # return HttpResponse("This is homepage")
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        File_image = request.FILES.get('File_image')  # Use request.FILES to get the uploaded file
        while len(zip)<5:
            messages.warning(request,"Meter Reading should be greater than 100000")
            zip = request.POST.get('zip')
        contact = Contact1(
            name=name,
            email=email,
            desc=desc,
            phone=phone,
            city=city,
            state=state,
            zip=zip,
            date=datetime.today(),
            File_image=File_image
        )
        contact.save()
        bill = (int(zip)-9999) *5
        messages.success(request, f'Your Billing is :- {bill} | PLease Pay It or be brave to loose your electricity')
        messages.success(request, "Successfully Submitted Form.")
        
        return render(request, 'contact.html', {
            'file_url': contact.File_image.url if File_image else None
        })
    
    return render(request, 'contact.html')
#     if request.method=="POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         desc = request.POST.get('desc')
#         phone = request.POST.get('phone')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         zip = request.POST.get('zip')
#         File_image = request.POST.get('File_image')
#         print(name,File_image,email, desc,phone,city,state,zip,datetime.now())
#         if File_image!="":
#             render(request, 'contact.html', {
#                 'file_url': File_image
#             })
#         contact = Contact1(name=name,File_image=File_image,email=email,desc=desc,phone=phone,city=city,state=state,zip=zip,date=datetime.today())
#         contact.save()
#         messages.success(request, "Successfully Submitted Form.")
        
#     return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def signup(request):
    if request.method=='POST':
        staffno = request.POST.get('staff')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        dob = request.POST.get('DOB')
        print(staffno,pass1,pass2,dob)
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password is not same .")
        my_user = User.objects.create_user(username=staffno, password=pass2)
        my_user.save()
        messages.success(request, "Successfully Created Account .")
        return redirect('home')
    return render(request,'signup.html')
def Logout(request):
    logout(request)
    messages.success(request, "LOGGED OUT SUCCESSFULLY .")
    return redirect('login')