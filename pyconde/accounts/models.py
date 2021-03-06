# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from . import validators


class Profile(models.Model):
    """
    A userprofile model that provides a short_info, twitter handle, website URL, avatar
    field and details about number/age of accompanying children

    This is also used as AUTH_PROFILE_MODULE.
    """
    user = models.OneToOneField(User)
    short_info = models.TextField(_('short info'), blank=True)
    avatar = ThumbnailerImageField(_('avatar'), upload_to='avatars', null=True,
                                   blank=True,
                                   help_text=_('Please upload an image with a side length of at least 300 pixels.'))
    num_accompanying_children = models.PositiveIntegerField(_('Number of accompanying children'),
                                                            null=True,
                                                            blank=True,
                                                            default=0)
    age_accompanying_children = models.CharField(_("Age of accompanying children"), blank=True, max_length=20)
    twitter = models.CharField(_("Twitter"), blank=True, max_length=20,
        validators=[validators.twitter_username])
    website = models.URLField(_("Website"), blank=True)
    organisation = models.TextField(_('organisation'), blank=True)


@receiver(user_logged_in)
def show_logged_in_message(request, user, **kwargs):
    messages.success(request, _("You've logged in successfully."),
                     fail_silently=True)
