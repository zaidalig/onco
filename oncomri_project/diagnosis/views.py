import pdfplumber
from django.shortcuts import render, redirect
from .forms import MedicalReportForm
from .models import MedicalReport

from django.contrib import messages
from django.core.exceptions import ValidationError

def upload_medical_report(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # 🛑 Check MIME type (extra safety)
            if uploaded_file.content_type != 'application/pdf':
                messages.error(request, "Invalid file type. Please upload a PDF.")
                return render(request, 'diagnosis/upload_report.html', {'form': form})

            report = form.save(commit=False)

            try:
                with pdfplumber.open(uploaded_file) as pdf:
                    text = ''
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + '\n'
                report.report_text = text
                report.save()
                return render(request, 'diagnosis/report_success.html', {'report': report})
            except Exception as e:
                messages.error(request, "Error parsing PDF: " + str(e))
                return render(request, 'diagnosis/upload_report.html', {'form': form})
    else:
        form = MedicalReportForm()

    return render(request, 'diagnosis/upload_report.html', {'form': form})
