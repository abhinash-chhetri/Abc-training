from django.urls import path
from training_app import views
urlpatterns = [
    path('', views.home),

]
