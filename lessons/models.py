from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class TimeStampedModel(models.Model):
    class Meta:
        abstract = True
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Lesson(TimeStampedModel):
    title = models.CharField(max_length=256, unique=True)
    content = RichTextUploadingField()

    def __str__(self) -> str:
        return self.title

# class Question(models.Model):
#     content