# content/views.py

from django.shortcuts import render
from rest_framework.response import Response  # 추가
from rest_framework.views import APIView
from .models import Feed


class Index(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()  # select * from content_feed;
        return render(request, "instagram/index.html", context=dict(feeds=feed_list))


# 추가
class UploadFeed(APIView):
    def post(self, request):

        file = request.data.get("file")
        image = request.data.get("image")
        content = request.data.get("content")
        user_id = request.data.get("user_id")
        profile_image = request.data.get("profile_image")

        return Response(status=200)
