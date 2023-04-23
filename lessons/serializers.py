

from rest_framework import serializers

from lessons import models



class LessonSerializer(serializers.ModelSerializer):
    def get_has_quiz(self, obj):
        return bool(models.Lesson.objects.get(id=obj.id).question_set.count())

    has_quiz = serializers.SerializerMethodField()

    class Meta:
        model = models.Lesson
        lookup_field = 'slug'
        fields = [
            "id",
            "title",
            "slug",
            "image_url",
            "content",
            "stripped_content",
            "has_quiz",
        ]


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionChoice
        fields = [
            "id",
            "content",
            "is_correct",
        ]

class QuestionSerializer(serializers.ModelSerializer):
    # def get_lesson_slug(self, obj):
    #     return obj.lesson.slug
    
    # lesson_slug = serializers.SerializerMethodField()
    choices = QuestionChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        fields = [
            "id",
            "lesson_id",
            "content",
            "solution",
            "choices",
            # "f",
        ]

