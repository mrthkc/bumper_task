from rest_framework import serializers

from guestbook.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, write_only=True)
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    user = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Entry
        fields = ('name', 'subject', 'message', 'user', )
