from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator
# Create your models here.
LEVEL = [
    ("B", "Beginner"),
    ("I", "Intermediate"),
    ("A", "Advance"),
]
class Course(models.Model):
    title = models.CharField(max_length=30)
    price =models.DecimalField(max_digits =8 ,decimal_places=0)
    description = models.CharField(max_length =120)
    level =models.CharField(max_length=1, choices= LEVEL, default='Beginner')

    class Meta:
        db_table ='Course'

    def __str__(self):
        return f'{self.title}'
    
class Instructor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length = 25)
    address = models.CharField (max_length = 20)
    phone = models.CharField(max_length =10, validators=[MinLengthValidator(limit_value=10)])
    qualifications = models.CharField(max_length=30)
    experience = models.PositiveSmallIntegerField()
    email = models.EmailField(unique = True)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    
    class Meta:
        db_table = 'Instructor'
        verbose_name_plural = 'Instructors'
    


class Upcomingclass(models.Model):
    title = models.CharField(max_length=25)
    duration = models.CharField(max_length  =25)
    price = models.PositiveIntegerField()
    start_date = models.DateField()
    time = models.CharField(max_length= 10)
    Instructor = models.ForeignKey(Instructor, on_delete= models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        db_table = 'Upcomingclass'
        verbose_name_plural = 'Upcomingclasses'
    

