from django.shortcuts import render
from django.http import HttpResponse
from . import machine_learning_model


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    user_input = request.GET['test_input']
    user_input = machine_learning_model.multiplier(user_input)
    return render(request, 'result.html', {'home_input':user_input})