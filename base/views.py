from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm






# rooms = [
#     { 'id': 1, 'name': 'Room1' },
#     { 'id': 2, 'name': 'Room2' },
#     { 'id': 3, 'name': 'Room3' },

# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(pk=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form': form}
    return render(request,'base/room_form.html',context)



