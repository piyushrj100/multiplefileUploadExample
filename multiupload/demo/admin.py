from django.contrib import admin
from .models import Post, UploadPdf

# Register your models here.
admin.site.register(UploadPdf)
admin.site.register(Post)