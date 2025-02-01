from . import BaseModel, models


class User(BaseModel):
    name = models.CharField(null=False, blank=False, unique=True)
