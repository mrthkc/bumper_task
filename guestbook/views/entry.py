from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from guestbook.models import Entry, User
from guestbook.serializers import EntrySerializer


class EntryViewSet(GenericViewSet):
    parser_classes = [JSONParser,]
    permission_classes = []

    def get_queryset(self):
        return Entry.objects.select_related('user').all().order_by('-created_at')

    def create(self, request, *args, **kwargs):
        """
        Scope: Creates a new entry and user if it does not exist.
        URI: /guestbook/entry/
        HTTP verbs: POST.
        """
        serializer = EntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, _ = User.objects.get_or_create(name=serializer.validated_data['name'])
        entry_data = {
            'subject': serializer.validated_data['subject'],
            'message': serializer.validated_data['message'],
            'user_id': user.pk,
        }
        Entry.objects.create(**entry_data)

        return Response(serializer.validated_data, status=HTTP_201_CREATED)

    def list(self, request, **kwargs):
        """
        Scope: Lists all entries in descending order.
        URI: /guestbook/entry/
        HTTP verbs: GET.
        """
        entries = self.get_queryset()
        entries = self.paginate_queryset(entries)
        serializer = EntrySerializer(
            entries,
            many=True
        )
        paginated_data = {
            'key': 'entries',
            'results': serializer.data,
        }
        return self.get_paginated_response(paginated_data)
