from django.shortcuts import render

def welcome(request):
    return render(request, 'trips/welcome.html')
