# content/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class Index(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()  # select * from content_feed;
        return render(
            request,
            "instagram/index.html",
            context=dict(
                feeds=feed_list,
            ),
        )
