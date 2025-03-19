from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'chat/home.html')
    def post(self, request):
        room = request.POST['room']
        user = request.POST['username']
        
        try: 
            existing_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            created_room = Room.objects.create(room_name=room)
        return redirect('room', room_name=room, username=user)

class RoomView(View):
    def get(self, request, room_name, username):
        existing_room = Room.objects.get(room_name__icontains=room_name)
        get_messages = Message.objects.filter(room=existing_room)

        context = {
            "messages" : get_messages,
            "user" : username,
            "room_name" : room_name
        }

        return render(request, 'chat/room.html', context)