from django.db import models
from django.contrib.auth.models import User

class MRIImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mri_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction or 'Pending'}"
