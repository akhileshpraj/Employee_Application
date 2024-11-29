from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
from .form import feedbackform
# Create your views hf

def emp_home(request):
    
    # data ke fetch kremge aur template me bhengeb
    emps=Emp.objects.all()
    
    return render(request,'emp/Home.html',{
        'emps':emps
    })
    


def add_emp(request):
    if request.method=='POST':
        # data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_work=request.POST.get("emp_work")
        emp_department=request.POST.get("emp_department")
        
        # create models object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_work is None:
            e.working=False
        else:
            e.working=True
        # save the object
        e.save()
        
        return redirect('/emp/home/')
    
    return render(request, 'emp/add_emp.html',{})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })
    
def do_emp_update(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_work=request.POST.get("emp_work")
        emp_department=request.POST.get("emp_department")
        
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_work is None:
            e.working=False
        else:
            e.working=True
        # save the object
        e.save()
      
    return redirect('/emp/home/')
    

def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,"emp/testimonials.html",{
        'testi':testi
    })
    
def feedback(request):
    if request.method=='POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
        else:
             return render(request,"emp/feedback.html",{'form':form})
        
    else:
        form=feedbackform()
        return render(request,"emp/feedback.html",{'form':form})

