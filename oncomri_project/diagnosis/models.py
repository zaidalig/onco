from django.db import models

# Create your models here.
from django.db import models

class MedicalReport(models.Model):
    patient_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='medical_reports/')
    report_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report of {self.patient_name} ({self.uploaded_at.date()})"
