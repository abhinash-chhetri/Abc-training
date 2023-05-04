from django.shortcuts import render
from training_app.models import Upcomingclass, Course
# Create your views here.
def home(request):
    classes = Upcomingclass.objects.all()
    return render(request,'training_app/home.html',{'classes':classes})

def courses(request):
    courses = Course.objects.all().order_by('price')                #filter(title__exact= 'python for django')
    return render(request,'training_app/courses.html',{'courses':courses})

def add_course(request):
    return render(request, 'training_app/add_course.html')
# classes = Upcomingclass.objects.all()
    # c = Course(title=title, description=desc, price=price, level=level)
        # c.save()
    