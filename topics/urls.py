from django.urls import path
from . import views

app_name = "topics"

urlpatterns = [
    path("topics/",views.TopicListApiView.as_view(),name="topics"),
]