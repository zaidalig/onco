from django.shortcuts import render

def home(request):
    return render(request, 'mri_classifier/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MRIImage
from .forms import MRIImageForm
from ml_model.predict import predict

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = MRIImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            label, confidence = predict(obj.image.path)
            obj.prediction = label
            obj.confidence = confidence
            obj.save()
            return redirect('report', pk=obj.pk)
    else:
        form = MRIImageForm()
    return render(request, 'mri_classifier/upload.html', {'form': form})

@login_required
def report(request, pk):
    image = MRIImage.objects.get(pk=pk, user=request.user)
    return render(request, 'mri_classifier/report.html', {'image': image})
