from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Topic
from serializers import TopicSerializer
class TopicListApiView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
# Create your views here.
