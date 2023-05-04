from django.shortcuts import render
from training_app.models import Upcomingclass
# Create your views here.
def home(request):
    classes = Upcomingclass.objects.all()
    return render(request,'training_app/home.html',{'classes':classes})