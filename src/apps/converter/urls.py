from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/file/', views.SampleViewSet.as_view()),
]