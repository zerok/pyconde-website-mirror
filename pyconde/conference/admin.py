from django.contrib import admin

from . import models


admin.site.register(models.Conference, list_display=("title", "start_date", "end_date"))
admin.site.register(models.Section, list_display=("name", "conference", "start_date", "end_date"))
admin.site.register(models.AudienceLevel,
    list_display=("name", "slug", "level", "conference"),
    list_filter=("conference",))
admin.site.register(models.SessionKind,
    list_display=("name", "closed", "start_date", "end_date", "conference"),
    list_filter=("conference",))
admin.site.register(models.SessionDuration,
    list_display=("label", "minutes", "conference"),
    list_filter=("conference",))
admin.site.register(models.Track,
    list_display=("name", "slug", "conference", "order", "visible"),
    list_filter=("conference", "visible"))
admin.site.register(models.Location,
    list_display=("name", "slug", "conference", "order", "used_for_sessions"),
    list_filter=("conference", "used_for_sessions"))
