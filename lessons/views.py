from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from lessons import models, filtersets
from lessons.serializers import LessonSerializer, QuestionSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = models.Lesson.objects.select_related("questions_set").all()
    queryset = models.Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'slug'

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = models.Question.objects.prefetch_related("questionchoice_set").all()
    queryset = models.Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filtersets.QuestionFilterSet
