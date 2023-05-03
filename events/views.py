from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from events.models import acc_crt
from events.models import create_poc
from events.models import details_comp
from datetime import datetime
from django.contrib import messages

admin = [
    {'username': 'shadab', 'password': 'shadab2005', 'club': 'IEEE'},
    {'username': 'aditya', 'password': 'adilol200', 'club': 'ACM'},
    {'username': 'hritik', 'password': 'flame123', 'club': 'NCC'}
]
people = []
students = acc_crt.objects.all()
for person in students:
    people.append(person.name)


poc = []
i = 0
point_of_contact = create_poc.objects.all()
active_company = details_comp.objects.all()

poc_company = []
for comp in point_of_contact:
    poc_company.append(comp.company)

for pocs in point_of_contact:
    poc.append({'username':pocs.name,'password':pocs.password})

active_comp = []

for active in active_company:
    active_comp.append(active.name)
    
print(poc)


# alam@738
def index(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        
        compi = details_comp.objects.all()
        return render(request, 'index.html',{'compi':compi})

def crt_acc(request):
    return render(request, 'acc_crt.html')

def crt_comp(request):
    return render(request, 'poc.html')

# hritik shadab2005

def details_added(request):

    if request.method == 'POST':
       details = request.POST.get('details')
       package = request.POST.get('package')
       date = request.POST.get('last_date')
       branch = request.POST.get('branch')
       name = request.POST.get('name')
       if details == "" or package == "" or date == "" or branch == "" or name == "":
            messages.success(request, 'PLEASE ENTER ALL THE DETAILS')
            return render(request, 'comp_details.html')
       for comp in active_comp:
            if name == comp:
                messages.success(request, 'company already exist')
                return  render(request, 'comp_details.html')
       else:
        info = details_comp(details = details,package = package,date = date,branch = branch,name=name)
        info.save()
       
        return render(request, 'poc_page.html')


def login(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            compi = details_comp.objects.all()
            return render(request, 'index.html',{'compi':compi})

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')


def adlog(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        # club = request.POST.get("club")

        for users in admin:
            if username == users['username']:
                if password == users['password']:
                    compi = create_poc.objects.all()
                    return render(request, 'club_adm.html',{'compi':compi})
            else:
                return render(request, 'adlog.html')
    else:
        return render(request, 'adlog.html')

def comp_details(request):
    return render(request, 'comp_details.html')
    

def adminlog(request):
    return render(request, 'adlog.html')

def poc_login(request):
    return render(request, 'poc_login.html')

def poc_page(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")

        for p_of_cont in poc:
            if username == p_of_cont['username']:
                if password == p_of_cont['password']:
                    compi = create_poc.objects.all()
                    for points in compi:
                        if username == points.name:
                            if points.status == "Active":
                                return render(request, 'poc_page.html',{'points':points})
                            else:
                                messages.success(request, 'Your Company status is not active please contact admin to make it active')
                            return render(request, 'poc_login.html')
        
        else:
            return render(request, 'poc_login.html')

    

def Acc_crt(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('edu')
        phone = request.POST.get('phone')
        registerd = request.POST.get('registerd')
        password = request.POST.get('password')
        if name == "" or email == "" or phone == "" or registerd == "" or password == "":
            messages.success(request, 'PLEASE ENTER ALL THE DETAILS')
            return render(request, 'acc_crt.html')
        acc = acc_crt(name=name, email=email, phone=phone,
                      registerd=registerd, date=datetime.today())
        if name in people :
             messages.success(request, 'username already exists ')
             return render(request, 'acc_crt.html')
        else:
            user = User.objects.create_user(name, email, password)
            acc.save()  
            user.save()
            messages.success(request, 'your id has been added successfully')
            return render(request, 'login.html')
    else:
        return render(request, 'acc_crt.html')
    # return HttpResponse("this is contact page")


def pocs_crt(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('edu')
        phone = request.POST.get('phone')
        registerd = request.POST.get('registerd')
        company = request.POST.get('company')
        date = request.POST.get('date')
        password = request.POST.get('password')
        status = request.POST.get('status')
        if name == "" or email == "" or phone == "" or registerd == "" or company == "" or date == "" or password == "" :
            messages.success(request, 'PLEASE ENTER ALL THE DETAILS')
            return render(request, 'poc.html')
        for comp in poc_company:
            if company == comp:
                messages.success(request, 'company already exist')
                return  render(request, 'poc.html')

        else:
            poc = create_poc(name=name, email=email,status = status,password=password, phone=phone,company = company,subdate= date, registerd=registerd, date=datetime.today())
            poc.save()
            messages.success(request, 'your id has been added successfully')
            return render(request, 'club_adm.html')
    else:
        return render(request, 'poc.html')
    # return HttpResponse("this is contact page")


def logoutuser(request):
    logout(request)
    return render(request, 'login.html')
