from django.urls import path
from . import views
urlpatterns = [
    path('',views.student_list,name='student_list' ),
    path('add_student/',views.add_student,name='add_student' ),
    path('edit/',views.edit_student,name='edit_student' ),
    path('',views.view_student,name='view_student' ),
]