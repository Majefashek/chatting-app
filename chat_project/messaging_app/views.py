from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def send_message(request):
    pass


def index(request):
    sender_id=request.user
    users=User.objects.all()
    return render(request, "chat/index.html", {'users': users,
                                               'sender_id':sender_id})


@csrf_exempt
def room_name(request, user2_id):
    user1_id = request.user.id
    room_name = f'chat_{min(user1_id, user2_id)}_{max(user1_id, user2_id)}'
    return JsonResponse({'room_name': room_name})
