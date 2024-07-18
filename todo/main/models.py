from django.utils import timezone
from uuid import uuid4
from django.db import models


# Create your models here.
class Item(models.Model):
    uuid = models.UUIDField(
        unique=True,
        auto_created=True,
        blank=False,
        null=False,
        default=uuid4(),
        editable=False,
    )
    title = models.CharField(max_length=256, blank=False, null=False)
    done = models.BooleanField(default=False, blank=False, null=False)
    due = models.DateTimeField(null=True)
    created = models.DateTimeField(
        blank=False, null=False, auto_created=True, default=timezone.now, editable=False
    )

    def __str__(self) -> str:
        return self.title + " " + str(self.uuid)
