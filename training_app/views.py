from django.shortcuts import render, redirect
from training_app.models import Upcomingclass, Course
# Create your views here.
def home(request):
    classes = Upcomingclass.objects.all()
    return render(request,'training_app/home.html',{'classes':classes})

def search(request):
    if request.method == "POST":
        python = request.POST['searched']
        courses= Course.objects.filter(title__contains =python)
        return render(request,'training_app/search.html',{'searched':python, 'courses':courses})
    else:
        return redirect('training-courses')
        # return render(request,'training_app/search.html',{}) 
    

def courses(request):
    courses = Course.objects.all()              
    return render(request,'training_app/courses.html',{'courses':courses})

def add_course(request):
    if request.method == "GET":
        return render(request, 'training_app/add_course.html')
    elif request.method == "POST":
        title = (request.POST['title'])
        price = (request.POST['price'])
        description = (request.POST['description'])
        level = (request.POST['level'])
        c = Course.objects.create(title=title, description=description, price=price, level=level)
        c.save()
        return redirect('training-courses')

    # c = Course.objects.create(title=title, description='description', price=price, level=level)
    # c.save()
    # return redirect('training-courses')

def delete(request, id):
   courses = Course.objects.get(id=id)
   courses.delete() 

   return redirect('training-courses')

def edit(request, id):
    if request.method == "GET":
        courses = Course.objects.get(id=id) 
        return render(request, 'training_app/edit.html',{'courses':courses})
    else:
        courses = Course.objects.get(id=id)
        courses.title = request.POST['title']
        courses.price = request.POST['price']
        courses.description = request.POST['description']
        courses.level = request.POST['level']

        courses.save()

    return redirect('training-courses')

