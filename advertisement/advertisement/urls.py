from django.urls import path
from .views import index
from .views import lesson

urlpatterns = [
    path("",index),
    path('lesson_4/',lesson)
]
