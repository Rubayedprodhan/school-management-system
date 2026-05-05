from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset_password/<str:token>/', reset_view, name='reset_password'),
    
    

    
] 
