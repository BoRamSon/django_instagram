from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
import os
from config.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt  # 403 Forbidden Error Sol
from django.utils.decorators import method_decorator  # 403 Forbidden Error Sol


class Index(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id")  # select * from content_feed;
        return render(request, "instagram/index.html", context=dict(feeds=feed_list))


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES["file"]
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get("content")
        image = uuid_name
        profile_image = request.data.get("profile_image")
        user_id = request.data.get("user_id")

        Feed.objects.create(
            content=content,
            image=image,
            profile_image=profile_image,
            user_id=user_id,
            like_count=0,
        )

        return Response(status=200)
