from django.shortcuts import render
from django.contrib import messages
from .models import *

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_images = request.FILES.get('student_images')
        # student save
        student = Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            student_id = student_id,
            gender = gender,
            date_of_birth = date_of_birth ,
            student_class = student_class,
            religion = religion,
            joining_date = joining_date,
            mobile_number = mobile_number,
            admission_number = admission_number,
            section = section,
            student_images = student_images
             

        )
        #Parent Information
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        parmanent_address = request.POST.get('parmanent_address')

        #save parent
        parent = Parent.objects.create(
            father_name = father_name,
            father_occupation = father_occupation,
            father_mobile = father_mobile,
            father_email = father_email,
            mother_name = mother_name,
            mother_occupation = mother_occupation,
            mother_mobile= mother_mobile,
            mother_email = mother_email,
            present_address = present_address,
            parmanent_address = parmanent_address
        )
        messages.success(request, "Student Added Successfully")
        return render(request,"student_list")

    return render(request,"student/add-student.html")


def student_list(request):
    return render(request,"student/students.html")

def edit_student(request):
    return render(request, "student/edit-student.html")

def view_student(request):
    return render(request, "student/student-details.html")