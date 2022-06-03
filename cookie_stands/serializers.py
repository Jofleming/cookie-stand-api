from rest_framework import serializers
from .models import Cookiestand


class CookiestandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookiestand
        fields = "__all__"
