from django.http import HttpResponse
from django.shortcuts import render
from .models import employee
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def details(request):
    emps=employee.objects.all()
    con={
        'emps':emps
    }
    return render(request,'details.html',con)

def add(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        phone=request.POST.get('phone')
        dept=request.POST.get('dept')
        Address=request.POST.get('Address')
        emp=employee(fname=fname,lname=lname,phone=phone,dept=dept,address=Address)
        emp.save()
        return HttpResponse(f"<h1>Employee Added Successfully : {fname} {lname}</h1>")
    return render(request,'add.html')

def search(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        dept=request.POST.get('dept')
        Address=request.POST.get('Address')
        emps=employee.objects.all()
        if fname:
            emps=emps.filter(Q(fname__icontains=fname) | Q(lname__icontains=fname))
        if dept:
            emps=emps.filter(dept__icontains=dept)
        if Address:
            emps=emps.filter(address__icontains=Address)
        con={
        'emps':emps
        }
        return render(request,'details.html',con)
    return render(request,'search.html')

def remove(request,emp_id=0):
    if emp_id:
        try:
            emp=employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse(f"<h1>Empolyee Removed Succefully : {emp.fname} {emp.lname}</h1>")
        except:
            return HttpResponse("Return a valid id")
    emps=employee.objects.all()
    con={
        'emps':emps
    }
    return render(request,'remove.html',con)
