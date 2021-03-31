from django.shortcuts import render
from django.http import HttpResponse
from.forms import StudentForm

def index(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'index.html',{'form':form})
    return render(request,'index.html',{'form':form})