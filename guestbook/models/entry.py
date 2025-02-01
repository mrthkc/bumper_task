from . import BaseModel, User, models


class Entry(BaseModel):
    subject = models.CharField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='entries',
    )