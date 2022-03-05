from django.db import models
from django.utils import timezone


class SoftDeletableManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeletableModel(models.Model):
    """
    An abstract base class model with a ``deleted_at`` field that
    marks entries that are not going to be used anymore, but are
    kept in db for any reason.
    Default manager returns only not-removed entries.
    """

    deleted_at = models.DateTimeField()
    available_objects = SoftDeletableManager()

    class Meta:
        abstract = True

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        Soft delete object (set its ``deleted_at`` field to current time).
        Actually delete object if setting ``soft`` to False.
        """
        if soft:
            self.deleted_at = timezone.now()
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)


class CreatedTimeModel(models.Model):
    """
    An abstract base class model with a ``created_at`` field that
    fills time when create an object.
    """

    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)

    class Meta:
        abstract = True
