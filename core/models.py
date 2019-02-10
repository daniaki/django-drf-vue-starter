import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TimeStampedModel(models.Model):
    """
    Base model representing a time stamped model updating the modification
    date everytime a change is saved.
    """
    creation_date = models.DateField(
        default=datetime.date.today,
        verbose_name='Creation date',
    )
    modification_date = models.DateField(
        default=datetime.date.today,
        verbose_name='Modification date',
    )

    class Meta:
        abstract = True
        ordering = ('-creation_date',)

    def save(self, *args, **kwargs):
        self.modification_date = datetime.date.today()
        return super().save(*args, **kwargs)


class SiteInformation(TimeStampedModel):
    """
    Contains site information such as the privacy policy, about, etc

    Markdown rendering is handled by the client.

    Attributes
    ----------
    name : `models.CharField`
        Namespace of the instance, usually the name of the owning app.
    about : `models.TextField`
        About information
    privacy : `models.TextField`
        The privacy policy
    terms : `models.TextField`
        The terms and conditions
    documentation : `models.TextField`
        Documentation regarding API, registration etc.
    """
    name = models.CharField(
        null=False, unique=True, blank=False, max_length=64)
    about = models.TextField(null=True, blank=True)
    privacy = models.TextField(null=True, blank=True)
    terms = models.TextField(null=True, blank=True)
    documentation = models.TextField(null=True, blank=True)
    version = models.CharField(
        max_length=64, null=True, default='0.1.0-alpha')
