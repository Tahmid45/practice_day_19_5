from django.shortcuts import render
from music.models import Album

def home(request):
    data = Album.objects.all()
    # print(data)
    # for i in data:
    #     print(i.name)
    #     print(i.release_date)
    #     print(i.musician)
    #     print(i.rating)
    #     print()
    return render(request, 'home.html', {'data':data})