from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

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
        create = 
        messages.success(request, "Student Added Successfully")
        return redirect("student_list")

    return render(request,"student/add-student.html")


def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'student_list' : student_list

    }
    
    return render(request,"student/students.html",context)



# def edit_student(request, slug):
#     student = get_object_or_404(Student, slug = slug )
#     parent = student.parent if hasattr (student, "parent" ) else None
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         student_id = request.POST.get('student_id')
#         gender = request.POST.get('gender')
#         date_of_birth = request.POST.get('date_of_birth')
#         student_class = request.POST.get('student_class')
#         religion = request.POST.get('religion')
#         joining_date = request.POST.get('joining_date')
#         mobile_number = request.POST.get('mobile_number')
#         admission_number = request.POST.get('admission_number')
#         section = request.POST.get('section')
#         student_images = request.FILES.get('student_images')
#         # student save

#         student.father_name = request.POST.get('father_name')
#         student.father_occupation = request.POST.get('father_occupation')
#         student.father_mobile = request.POST.get('father_mobile')
#         student.father_email = request.POST.get('father_email')
#         student.mother_name = request.POST.get('mother_name')
#         student.mother_occupation = request.POST.get('mother_occupation')
#         student.mother_mobile = request.POST.get('mother_mobile')
#         student.mother_email = request.POST.get('mother_email')
#         student.present_address = request.POST.get('present_address')
#         student.parmanent_address = request.POST.get('parmanent_address')

#         student = Student.objects.create(
#             first_name = first_name,
#             last_name = last_name,
#             student_id = student_id,
#             gender = gender,
#             date_of_birth = date_of_birth ,
#             student_class = student_class,
#             religion = religion,
#             joining_date = joining_date,
#             mobile_number = mobile_number,
#             admission_number = admission_number,
#             section = section,
#             student_images = student_images
            
#          )
        



#     return render(request, "student/edit-student.html")

# def edit_student(request, slug):
 
#     student = get_object_or_404(Student, slug=slug)
    
#     if request.method == 'POST':
        
#         student.first_name = request.POST.get('first_name')
#         student.last_name = request.POST.get('last_name')
#         student.student_id = request.POST.get('student_id')
#         student.gender = request.POST.get('gender')
#         student.date_of_birth = request.POST.get('date_of_birth')
#         student.student_class = request.POST.get('student_class')
#         student.religion = request.POST.get('religion')
#         student.joining_date = request.POST.get('joining_date')
#         student.mobile_number = request.POST.get('mobile_number')
#         student.admission_number = request.POST.get('admission_number')
#         student.section = request.POST.get('section')
        
     
#         if request.FILES.get('student_images'):
#             student.student_images = request.FILES.get('student_images')

       
#         student.father_name = request.POST.get('father_name')
#         student.father_occupation = request.POST.get('father_occupation')
#         student.father_mobile = request.POST.get('father_mobile')
#         student.father_email = request.POST.get('father_email')
#         student.mother_name = request.POST.get('mother_name')
#         student.mother_occupation = request.POST.get('mother_occupation')
#         student.mother_mobile = request.POST.get('mother_mobile')
#         student.mother_email = request.POST.get('mother_email')
#         student.present_address = request.POST.get('present_address')
#         student.parmanent_address = request.POST.get('parmanent_address')



#         student.father_name = request.POST.get('father_name')

     
#         student.save()
        
      
#         from django.shortcuts import redirect
#         return redirect('student_list') 

#     context = {
#         'student': student
#     }
#     return render(request, "student/edit-student.html", context)




def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    
    if request.method == 'POST':
        # Student Basic Info Update
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.student_id = request.POST.get('student_id')
        student.gender = request.POST.get('gender')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.student_class = request.POST.get('student_class')
        student.religion = request.POST.get('religion')
        student.joining_date = request.POST.get('joining_date')
        student.mobile_number = request.POST.get('mobile_number')
        student.admission_number = request.POST.get('admission_number')
        student.section = request.POST.get('section')

        if request.FILES.get('student_images'):
            student.student_images = request.FILES.get('student_images')
        
        student.save() # Student data save holo

        # Parent Information Update (Crucial Part)
        # Jodi Student model-er sathe 'parent' namer kono relation thake
        if hasattr(student, 'parent') and student.parent:
            parent = student.parent
            parent.father_name = request.POST.get('father_name')
            parent.father_occupation = request.POST.get('father_occupation')
            parent.father_mobile = request.POST.get('father_mobile')
            parent.father_email = request.POST.get('father_email')
            parent.mother_name = request.POST.get('mother_name')
            parent.mother_occupation = request.POST.get('mother_occupation')
            parent.mother_mobile = request.POST.get('mother_mobile')
            parent.mother_email = request.POST.get('mother_email')
            parent.present_address = request.POST.get('present_address')
            # Admin panel onujayi spelling: 'parmanent_address'
            parent.parmanent_address = request.POST.get('parmanent_address')
            parent.save() # Parent model-er data save holo

        return redirect('student_list') 

    context = {
        'student': student
    }
    return render(request, "student/edit-student.html", context)





def view_student(request, slug):
    student = get_object_or_404(Student, student_id = slug)
    context = {
        'student' : student
    }
    return render(request, "student/student-details.html", context)




def delete(request, slug):
    # নির্দিষ্ট স্টুডেন্টকে খুঁজে বের করা
    student = get_object_or_404(Student, slug=slug)
    
    if request.method == "POST":
        student.delete() # ডাটাবেজ থেকে মুছে ফেলা
        return redirect("student_list")
    return redirect("student_list")