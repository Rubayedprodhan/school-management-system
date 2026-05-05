from django.shortcuts import render
from django.http import HttpResponse
from . models import Notification
from django.http import JsonResponse
from django.http import HttpResponseForbidden
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def dashborad(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    unread_notifications_count = unread_notifications.count()
    return render(request, 'student/student-dashboard.html')



def mark_notification(request):
    if request.method == 'POST':

        notification = Notification.objects.fillter(user=request.user,is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})

    return HttpResponseForbidden()


def all_clear_notification(request):
    if request.method == 'POST':
        Notification.objects.filter(user=request.user).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

