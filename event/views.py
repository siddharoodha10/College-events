from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from event.models import Event,student

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('details')
        else:
            messages.info(request, 'INVALID USERNAME /PASSWORD')
            return redirect('index')
    else:
        return render(request,'index')

def logout(request):
    auth.logout(request)
    return redirect('/')

def details(request):
    listevent = Event.objects.all()
    return render(request,'details.html', {'lists':listevent})
            
    
def details1(request):
    listevent = Event.objects.all()
    return render(request,'details1.html', {'lists':listevent})

def register(request):
    if request.method == 'POST':
        USN = request.POST['USN']
        name = request.POST['name']
        branch = request.POST['branch']
        sem = request.POST['sem']
        college = request.POST['college']
        email = request.POST['email']
        contact = request.POST['contact']
        Even_fees=request.POST['Even_fees']
        payment_mode = request.POST.get('payment_mode')
        account_no = request.POST['account_no'] 
        cvv = request.POST['cvv'] 
        exp_date = request.POST['exp_date'] 
        E_id_id = request.POST['E_id_id']
        E_name=request.POST["E_name"]
        
        user1 =  student.objects.create(USN=USN, name=name,  branch=branch, sem= sem, college=college, email=email, E_id_id=E_id_id ,E_name=E_name,contact=contact,Even_fees=Even_fees, payment_mode=payment_mode , account_no =account_no,cvv = cvv,exp_date = exp_date)
        user1.save();
        return redirect('registered')

    else:
        return render(request, 'register.html')
def registered(request):
    return render(request, 'registered.html')


def register1(request):
    if request.method == 'POST':
        USN = request.POST['USN']
        name = request.POST['name']
        branch = request.POST['branch']
        sem = request.POST['sem']
        college = request.POST['college']
        email = request.POST['email']
        contact = request.POST['contact']
        Even_fees=request.POST['Even_fees']
        payment_mode = request.POST.get('payment_mode')
        account_no = request.POST['account_no'] 
        cvv = request.POST['cvv'] 
        exp_date = request.POST['exp_date'] 
        E_id_id = request.POST['E_id_id']
        E_name=request.POST["E_name"]
        
        user1 =  student.objects.create(USN=USN, name=name,  branch=branch, sem= sem, college=college, email=email, E_id_id=E_id_id ,E_name=E_name,contact=contact,Even_fees=Even_fees, payment_mode=payment_mode , account_no =account_no,cvv = cvv,exp_date = exp_date)
        user1.save();
        return redirect('registered1')

    else:
        return render(request, 'register1.html')
def registered1(request):
    return render(request, 'registered1.html')

def download(request):
    stud = student.objects.all()
    return render(request,'display.html',{'Stud':stud})

def new_event(request):
    if request.method == 'POST':
        E_id = request.POST['E_id']
        E_name = request.POST['E_name']
        E_type = request.POST['E_type']
        E_location = request.POST['E_location']
        E_date = request.POST['E_date']
        E_time = request.POST['E_time']
        E_fees = request.POST['E_fees']
        E_coordinator_no = request.POST['E_coordinator_no'] 
        
        user1 =  Event.objects.create(E_id=E_id,E_name=E_name,E_type=E_type,E_location=E_location,E_date=E_date,E_time=E_time,E_fees=E_fees,E_coordinator_no=E_coordinator_no)
        user1.save();
        return redirect('new_event')

    else:
        return render(request, 'new_event.html')
