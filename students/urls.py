from django.urls import path
from . import views
urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('add_student/',views.add_student,name='add_student' ),
    path('edit_student/<str:slug>/',views.edit_student,name='edit_student' ),
   # path('view_student/',views.view_student,name='view_student' ),
    path('students/<str:slug>/', views.view_student, name='view_student'),
    path('delete/<str:slug>/', views.delete, name='delete')

]