from django.db.models import F, Count, Subquery, OuterRef, Value, CharField
from django.db.models.functions import Concat
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from guestbook.models import Entry, User
from guestbook.serializers import UserSerializer


class UserViewSet(GenericViewSet):
    parser_classes = [JSONParser,]
    permission_classes = []
    pagination_class = None

    def get_queryset(self):
        return User.objects.all().order_by('-created_at')

    def list(self, request, **kwargs):
        """
        Scope: Lists users with entry details.
        URI: /guestbook/user/
        HTTP verbs: GET.
        """
        users = self.get_queryset()
        users = users.annotate(
            username=F('name'),
            message_count=Count('entries'),
            last_entry=Subquery(
                Entry.objects.filter(user_id=OuterRef('pk')).annotate(
                    sub_msg=Concat(F('subject'), Value(' | '), F('message'), output_field=CharField())
                ).values(
                    'sub_msg'
                )[:1]
            )
        ).values(
            'username',
            'message_count',
            'last_entry',
        )

        serializer = UserSerializer(
            users,
            many=True
        )
        return Response({"users": serializer.data}, status=HTTP_200_OK)
