from django.contrib import admin
from lessons import models

from django import forms
from ckeditor.widgets import CKEditorWidget


class LessonAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = models.Lesson
        fields = '__all__'


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm