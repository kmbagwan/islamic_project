from django.shortcuts import render

def f1(request):
    return render(request,'my_app/home.html')