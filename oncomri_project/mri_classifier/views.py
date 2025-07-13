from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MRIImage
from .forms import MRIImageForm
from ml_model.predict import predict
from utils.decorators import role_required

# =====================
# General Home View
# =====================
def home(request):
    return render(request, 'mri_classifier/home.html')

# =====================
# Upload View (Doctor Only)
# =====================
@role_required('doctor')
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

# =====================
# Report View (Logged-in user only)
# =====================
@login_required
def report(request, pk):
    image = get_object_or_404(MRIImage, pk=pk)

    # Allow if user is owner or radiologist
    if image.user == request.user or request.user.groups.filter(name='radiologist').exists():
        return render(request, 'mri_classifier/report.html', {'image': image})
    
    return render(request, '403.html', status=403)

# =====================
# All Reports for Logged-in User
# =====================
@login_required
def my_reports(request):
    if request.user.groups.filter(name='radiologist').exists():
        # Radiologists can see all
        reports = MRIImage.objects.all().order_by('-uploaded_at')
    else:
        # Others see only their own
        reports = MRIImage.objects.filter(user=request.user).order_by('-uploaded_at')

    return render(request, 'mri_classifier/my_reports.html', {'reports': reports})
