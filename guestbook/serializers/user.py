from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    message_count = serializers.IntegerField()
    last_entry = serializers.CharField()
