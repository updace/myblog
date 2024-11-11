from django.shortcuts import render, redirect

def blog(request):
    return render(request,'index.html')