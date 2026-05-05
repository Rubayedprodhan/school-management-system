from django.urls import path
from . import views
urlpatterns = [
    path('',views.index , name='index'),
    path('dashborad/',views.dashborad , name='dashborad'),
    path('all_clear_notification/', views.all_clear_notification, name='all_clear_notification'),
    path('mark_notification/', views.mark_notification, name='mark_notification'),
    
]