from django.shortcuts import render

def home(request):
    return render(request, 'mri_classifier/home.html')
