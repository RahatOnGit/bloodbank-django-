from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .decorators import *

@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
          login(request,user) 
          return redirect('home')
          

        else:
          messages.info(request, "Username or password invalid")


    context={}
    return render(request,'login.html',context)





@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')




# Create your views here.

@login_required(login_url='login')
def home(request):
    query = Donor.objects.all()

    if request.GET.get('address'):
       
        address = request.GET.get('address')
        query = Donor.objects.filter( address__icontains =  address)

    if request.GET.get('blood_group'):
       
        group = request.GET.get('blood_group')
        query = query.filter( blood_group =  group)


    context={'all_donors': query}

    
    return render(request,'home.html', context)




@login_required(login_url='login')
@admin_only
def manage_donors(request):
    query = Donor.objects.all()
    phone = ""
    name= ""
    count = 0

    if request.GET.get('phone_num'):
       
        phone_num = request.GET.get('phone_num')
        phone = phone_num
        query = Donor.objects.filter(phone = phone_num)
        count = 1

    if request.GET.get('name'):
       
        name = request.GET.get('name')
        name = name
        query = query.filter( name = name)
        count = 1

    context={'donors': query, 'count': count}
    return render(request,'manage_donors.html', context)



@login_required(login_url='login')
@admin_only
def add_donor(request):

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        phone = data.get('phone')
        blood_group = data.get('blood_group')
        house = data.get('house')
        upazila = data.get('upazila')
        district = data.get('district')
        
        Donor.objects.create(
            name = name,
            phone = phone,
            blood_group= blood_group,
            house_details = house,
            upazila = upazila,
            district  =district,
            address = house + " "+ upazila + " "+district
        )

        return redirect('manage_donors')


    context={}
    return render(request,'add_donor_form.html', context)



@login_required(login_url='login')
@admin_only
def delete_donor(request,pk):
    donor1 = Donor.objects.get(id=pk)
    context = {'donor1': donor1}
    return render(request,'delete_donor.html', context)


@login_required(login_url='login')
@admin_only
def delete_ok(request,pk):
    donor1 = Donor.objects.get(id=pk)
    donor1.delete()
    return redirect('manage_donors')


@login_required(login_url='login')
@admin_only
def update_donor(request,pk):
    donor1 = Donor.objects.get(id=pk)
    
    if request.method == "POST":
        donor1.name = request.POST.get('name')
        donor1.phone = request.POST.get('phone')
        donor1.blood_group = request.POST.get('blood_group')
        donor1.house_details = request.POST.get('house') 
        donor1.upazila = request.POST.get('upazila')
        donor1.district = request.POST.get('district')
        donor1.address = request.POST.get('house') +" "+ request.POST.get('upazila')+ " " + request.POST.get('district')
        

        donor1.save()
        return redirect("manage_donors")


    context={'donor1': donor1}

    return render(request,'update_donor.html',context)


