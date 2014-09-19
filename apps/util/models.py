from django.db import models


class Announcement(models.Model):
    """
    Notification for myparliament.ge announcements
    """
    text = models.CharField(max_length=255, blank=False, null=False,
                            help_text='Announcement link text')

    url = models.CharField(max_length=255, blank=False, null=False,
                           help_text='Announcement url')

