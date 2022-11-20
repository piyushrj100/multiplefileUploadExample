from django.db import models
class UploadPdf(models.Model):
    resumes = models.FileField(upload_to='resumes/', blank=True, null=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title