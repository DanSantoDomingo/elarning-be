import django_filters

from lessons import models


class QuestionFilterSet(django_filters.FilterSet):
    lessonId = django_filters.CharFilter(field_name="lesson_id", lookup_expr="exact")
    class Meta:
        fields = ["lessonId"]
        model = models.Question