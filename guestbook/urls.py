from django.urls import include, path
from rest_framework import routers

from guestbook.views.entry import EntryViewSet
from guestbook.views.user import UserViewSet

app_name = "guestbook"

router = routers.DefaultRouter()
router.register(
    "entry",
    EntryViewSet,
    basename="entry"
)
router.register(
    "user",
    UserViewSet,
    basename="user"
)

urlpatterns = [
    path("", include(router.urls)),
]
