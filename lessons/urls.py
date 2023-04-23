from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from lessons.views import LessonViewSet, QuestionViewSet

router = SimpleRouter()

router.register("lessons", LessonViewSet, "lessons")
router.register("questions", QuestionViewSet, "questions")


urlpatterns = [
    path("api/v1/", include(router.urls))
]
