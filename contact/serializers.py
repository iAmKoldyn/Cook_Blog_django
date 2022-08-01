from rest_framework import serializers
from .models import About, ContactLink, ContactModel, Social


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ContactLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLink
        fields = "__all__"


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"