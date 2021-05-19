from django.http import HttpResponse
from django import forms
from django.shortcuts import render
import random
import time
# Create your views here.
class NewTaskForm(forms.Form):
    """docstring ss NewTaskForm."""
    user_submitted_answer = forms.CharField(label = "Your Answer ")

def index(request):
    return render(request, "DoYourMath/index.html")

def multiplication(request):
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    return render(request, "DoYourMath/Multiplication.html",{
    "number1" : num1,
    "number2" : num2,
    "answer" : num1 * num2,
    "form" : NewTaskForm()
    })

def substraction(request):
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    answer= num1-num2
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data["user_submitted_answer"]
            if(user_answer == str(answer)):
                return HttpResponse("<h1>Yes</h1>")
    return render(request, "DoYourMath/Substraction.html",{
    "number1" : num1,
    "number2" : num2,
    "answer" : answer,
    "form" : NewTaskForm()
    })




def addition(request):
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    return render(request, "DoYourMath/Addition.html",{
    "number1" : num1,
    "number2" : num2,
    "answer" : num1 + num2,
    "form" : NewTaskForm()
    })

def division(request):
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    answer= num1/num2
    return render(request, "DoYourMath/Division.html",{
    "number1" : num1,
    "number2" : num2,
    "answer" : answer,
    })


def answer(request,user_answer):
    return render(request, "DoYourMath/answer.html",{
    "user_answer":user_answer
    })
