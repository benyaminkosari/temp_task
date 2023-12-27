from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        extra_kwargs = {'author': {'read_only': True},
                        'is_accepted': {'read_only': True}}
        exclude = ("views",)

    def get_author(self, obj):
        return obj.author.username