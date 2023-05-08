from django.urls import path
from training_app import views
urlpatterns = [
    path('', views.home, name='training-home'),
    path('courses/', views.courses, name = 'training-courses'), 
    path('home/', views.home),
    path('addcourse/', views.add_course, name='training-addcourse'),
    path('delete/<int:id>', views.delete, name ='training-delete'),
    path('edit/<int:id>', views.edit, name= 'training-edit'),
    path('search/>', views.search, name= 'training-search'),

]
