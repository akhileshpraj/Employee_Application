from django.shortcuts import render
from django.http import HttpResponse
import datetime
def homepages(request):
    if request.method=='POST':
        isActive=True
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=True
        else: isActive =True
    
    
    
    date=datetime.datetime.now()
    name="learn code with"
    list_of_program=[
        'WAP to check even or odd'
        'WAP to check prime number'
        'WAP TO print all prime number from 1 to 100'
        'WAP to print pascel number'
    ]
    Student={
        "student_name": 'Akhilesh',
        'student_college':'dce',
        'student_addres':'delhi'
    }
    data={
        'date':date,
        'name':name,
        'list_of_program':list_of_program,
        'Student':Student
        
    }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")