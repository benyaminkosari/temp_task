from django.urls import path
from .views import (AnnouncementsAPIView,
                    AnnouncementDetailsAPIView,
                    AnnouncementAcceptAPIView,
                    MyAnnouncementsAPIView,
                    SearchAnnouncementsAPIView,
                    NumberViewsAPIView)


urlpatterns = [
    path('announcements/', AnnouncementsAPIView.as_view(), name='announcements-list-create'),
    path('announcements/<int:pk>/', AnnouncementDetailsAPIView.as_view(), name='announcement-detail'),
    path('announcements/<int:announcement_id>/accept/', AnnouncementAcceptAPIView.as_view(), name='announcement-accept'),
    path('my-announcements/', MyAnnouncementsAPIView.as_view(), name='my-announcements'),
    path('announcements/search/', SearchAnnouncementsAPIView.as_view(), name='search-announcements'),
    path('announcements/<int:pk>/views/', NumberViewsAPIView.as_view(), name='number-of-views'),

]