from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Topic
from .serializers import TopicSerializer
from django.db.models import Q

class TopicListApiView(ListAPIView):
    queryset = Topic.objects.all()
    # queryset = Topic.objects.all().annotate(likes=Count("votes",filter=Q(votes__vote=Vote.VoteChoice.like))
    #                                         ,dislike=Count("votes",filter=Q(votes__vote=Vote.VoteChoice.dislike)))
    serializer_class = TopicSerializer

# Create your views here.
