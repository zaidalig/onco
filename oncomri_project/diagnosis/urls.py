from django.urls import path
from .views import upload_medical_report

urlpatterns = [
    path('upload-report/', upload_medical_report, name='upload_medical_report'),
]
