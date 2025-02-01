from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=now, db_index=True)

    class Meta:
        abstract = True

from .user import User
from .entry import Entry
