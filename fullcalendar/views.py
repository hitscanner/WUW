from django.shortcuts import render

def fullcalendar(request):

    return render(request, 'fullcalendar.html')