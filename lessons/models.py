from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Lesson(models.Model):
    content = RichTextUploadingField()