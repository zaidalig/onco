from django.shortcuts import render

def home(request):
    return render(request, 'mri_classifier/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MRIImage
from .forms import MRIImageForm
from ml_model.predict import predict

from ml_model.predict import predict

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = MRIImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            label, confidence = predict(img.image.path)
            img.prediction = label
            img.confidence = confidence
            img.save()
            return redirect('report', pk=img.pk)
    else:
        form = MRIImageForm()
    return render(request, 'mri_classifier/upload.html', {'form': form})


@login_required
def report(request, pk):
    image = MRIImage.objects.get(pk=pk, user=request.user)
    return render(request, 'mri_classifier/report.html', {'image': image})
