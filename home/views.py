from django.shortcuts import render, HttpResponse, redirect, reverse
from trips.models import Trip


def display_home(request):
    trips = Trip.objects.all()
    return render(request, 'home/home.template.html',{
        'trips':trips
    })

# handle alll 404
def handler404(request, exception):
       return render(request, 'home/404.html')