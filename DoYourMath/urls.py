from django.urls import path
from . import views

app_name = "DoYourMath"
urlpatterns=[
    path("",views.index, name="index"),
    path("multiplication",views.multiplication, name="multiplication"),
    path("substraction",views.substraction, name="substraction"),
    path("addition",views.addition, name="addition"),
    path("division",views.division, name="division"),
    path("answer",views.answer, name="answer")
]
