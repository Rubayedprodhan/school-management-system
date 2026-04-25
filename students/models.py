from django.db import models
from django.utils.text import slugify
# Create your models here.


class Parent(models.Model):
    father_name = models.CharField(max_length=80)
    father_occupation = models.CharField(max_length=30)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=30)
    mother_name = models.CharField(max_length=30)
    mother_occupation = models.CharField(max_length=30)
    mother_mobile = models.CharField(max_length=30)
    mother_email = models.CharField(max_length=30)
    present_address = models.TextField()
    parmanent_address = models.TextField()


    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"



class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    CLASS_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),

        

    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True) 
    gender = models.CharField(choices=GENDER_CHOICES,default='N')
    student_class = models.CharField(choices=CLASS_CHOICES)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=40)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=15)
    section = models.CharField(max_length=15)
    student_images=models.ImageField(upload_to='Student/', blank=True)
    parent = models.OneToOneField(Parent,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255,unique=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
           self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")

   
        super(Student, self).save(*args, **kwargs)