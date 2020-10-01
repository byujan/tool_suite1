from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            return render(request, 'trollresults.html', {})
    else:
        form = UploadFileForm()
    return render(request, 'main/base.html', {'form': form})

def trollresults(response):
    return render(response, 'main/trollresults.html', {})

def login(response):
    return redirect("/login")

def v1(response):
    return HttpResponse("<h1>Hellov1</h1>")