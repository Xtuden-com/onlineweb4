from django.contrib import admin
from django.utils.translation import gettext as _
from reversion.admin import VersionAdmin

from .models import Poster


@admin.register(Poster)
class PosterAdmin(VersionAdmin):
    model = Poster
    list_display = (
        "event",
        "title",
        "assigned_to",
        "display_from",
        "ordered_date",
        "ordered_by",
        "ordered_committee",
    )
    fieldsets = (
        (
            _("Event info"),
            {"fields": ("event", "title", "price", "description", "comments")},
        ),
        (_("Order info"), {"fields": ("amount",)}),
        (
            _("proKom"),
            {
                "fields": (
                    "display_from",
                    "assigned_to",
                    "ordered_by",
                    "ordered_committee",
                    "finished",
                )
            },
        ),
    )
    search_fields = (
        "title",
        "event__title",
        "assigned_to__first_name",
        "assigned_to__last_name",
        "ordered_by__first_name",
        "ordered_by__last_name",
    )
