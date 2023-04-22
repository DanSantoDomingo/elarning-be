from django.contrib import admin
from lessons import models

from django import forms
from ckeditor.widgets import CKEditorWidget

admin.site.site_url = None


class QuestionInline(admin.TabularInline):
    class QuestionInlineForm(forms.ModelForm):
        content = forms.CharField()
        class Meta:
            model = models.Question
            fields = ["content", "question_type"]

    form = QuestionInlineForm
    model = models.Question
    extra = 1
    show_change_link = True


class QuestionChoiceInline(admin.TabularInline):
    class QuestionChoiceInlineForm(forms.ModelForm):
        content = forms.CharField()
        class Meta:
            model = models.QuestionChoice
            fields = ["content", "is_correct"]

    form = QuestionChoiceInlineForm
    model = models.QuestionChoice
    extra = 1
    show_change_link = True
    

@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    class LessonAdminForm(forms.ModelForm):
        content = forms.CharField(widget=CKEditorWidget())
        class Meta:
            model = models.Lesson
            fields = '__all__'

    form = LessonAdminForm
    list_display = ["title", "created", "modified"]
    inlines = [QuestionInline]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["lesson",]
    fields = ["lesson", "question_type", "content", "solution",]
    inlines = [QuestionChoiceInline]


@admin.register(models.QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ["question",]

