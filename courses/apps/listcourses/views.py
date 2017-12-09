from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages 

from models import *
# Create your views here.
def index(request):
    try:
        course.objects.all()
    except:
        pass

    return render(request, "listcourses/index.html",{"courses": course.objects.all()})

def detailinfo(request,id):
    course.objects.get(id=id)
    return render(request,"listcourses/coursedetail.html", {"courses":course.objects.get(id=id)})
    
def add(request):
        errors = course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            print 'need more information'
            
            return redirect('/listcourses')
        else:
            course.objects.create(name=request.POST['name'],description=request.POST['description'],coursenumber=request.POST['coursenumber'],semester=request.POST['semester'])
        
        return redirect('/listcourses')
def remove(request,id):
     course.objects.get(id=id)
     return render(request,"listcourses/coursealert.html", {"courses":course.objects.get(id=id)})
def delete(request,id):

    c = course.objects.get(id=id)
    c.delete()
    return redirect("/listcourses")

def news(request):

    return render(request,'listcourses/news.html')

def faculty(request):
    
    return render(request,'listcourses/faculty.html')