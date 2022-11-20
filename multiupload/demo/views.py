from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Post
from .forms import ResumeUpload
from .models import UploadPdf

def upload_pdf(request) : 
    if request.method == "POST" :
        form = ResumeUpload(request.POST, request.FILES)
        files=request.FILES.getlist('resumes')
        if form.is_valid() : 
            for f in files: 
                file_instance = UploadPdf(resumes=f)
                file_instance.save()
    else : 
        form = ResumeUpload()
    return render(request,'demo/upload_pdf.html', {'form' : form})

