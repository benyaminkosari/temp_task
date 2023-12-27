from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Announcement
from .serializers import AnnouncementSerializer

class AnnouncementsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnnouncementDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AnnouncementAcceptAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, announcement_id):
        announcement = get_object_or_404(Announcement, pk=announcement_id)
        announcement.is_accepted = True
        announcement.save()
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MyAnnouncementsAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        return Announcement.objects.filter(author=self.request.user)

class SearchAnnouncementsAPIView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Announcement.objects.filter(title__icontains=query) \
                | Announcement.objects.filter(content__icontains=query)

class NumberViewsAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({'views': instance.views}, status=status.HTTP_200_OK)
