from django.shortcuts import render

from PollApp.models import Exam


# Create your views here.

def home(request):
    exam = Exam.objects.all()
    
    return render(request, 'PollApp/index.html', {'exam': exam})
