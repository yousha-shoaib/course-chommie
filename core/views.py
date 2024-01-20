from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {
        "id": 1,
        "name": "Lets learn python!"
    },
    {
        "id": 2,
        "name": "Diving into Delphi!"
    },
    {
        "id": 3,
        "name": "Physics!"
    }
]

def home(request):
    return render(request, 'core/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {"room": room}
    return render(request, 'core/room.html', context)