from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth import login
from django.contrib import messages
from .forms import RoomForm,NewUserForm
from django.contrib.auth.models import User


# rooms = [
#     { 'id': 1, 'name': 'Room1' },
#     { 'id': 2, 'name': 'Room2' },
#     { 'id': 3, 'name': 'Room3' },

# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def registerUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request,"base/register_user.html", context={"register_form":form})

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



