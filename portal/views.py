from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import TeacherLoginForm
from django.contrib.auth.decorators import login_required
from .models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404, redirect


def login_view(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = TeacherLoginForm()
    return render(request, 'portal/login.html', {'form': form})
    

@login_required
def index(request):
    mem=Student.objects.all()
    return render(request,'portal/home.html',{'mem':mem})


@login_required
def add(request):
    return render(request,'portal/add.html')


@login_required
def addrec(request):
    x=request.POST['name']
    y=request.POST['subject']
    z=request.POST['marks']
    mem=Student(name=x,subject=y,marks=z)
    mem.save()
    return redirect("/")


@login_required
def update(request,id):
    mem=Student.objects.get(id=id)
    return render(request,'portal/update.html',{'mem':mem})


@login_required
def uprec(request,id):
    x=request.POST['name']
    y=request.POST['subject']
    z=request.POST['marks']
    mem=Student.objects.get(id=id)
    mem.name=x
    mem.subject=y
    mem.marks=z
    mem.save()
    return redirect("/")


@login_required
def delete(request,id):
    mem=Student.objects.get(id=id)
    mem.delete()
    return redirect("/")

