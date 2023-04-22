from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class TimeStampedModel(models.Model):
    class Meta:
        abstract = True
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Lesson(TimeStampedModel):
    title = models.CharField(max_length=256, unique=True)
    slug = models.CharField(max_length=512, unique=True, blank=True)
    image_url = models.URLField(blank=True, max_length=1024)
    content = RichTextUploadingField()

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    class QuestionType(models.IntegerChoices):
        MULTIPLE_CHOICE = 1
        ESSAY = 2

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True)
    question_type = models.IntegerField(choices=QuestionType.choices, default=QuestionType.MULTIPLE_CHOICE)
    solution = RichTextUploadingField(blank=True)

    def __str__(self) -> str:
        return f"{self.lesson} - Question {self.id or ''}"

class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    content = models.CharField(max_length=256)
