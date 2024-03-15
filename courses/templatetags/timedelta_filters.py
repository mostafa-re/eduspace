from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def td_total(queryset):
    return queryset.aggregate(Sum('duration')).get('duration__sum')

@register.filter
def td_exact(timedelta):
    secs = timedelta.total_seconds()

    hrs = int(secs // 3600)
    secs %= 3600
    mins = int(secs // 60)
    secs %= 60

    return f"{hrs:02d}:{mins:02d}:{secs:02d}"


@register.filter
def td_hours_minutes(timedelta):
    secs = timedelta.total_seconds()

    hrs = int(secs // 3600)
    secs %= 3600
    mins = int(secs // 60)

    return f"{hrs:02d}:{mins:02d}"


@register.filter
def td_hours(timedelta):
    secs = timedelta.total_seconds()

    hrs = int(secs // 3600)

    return f"{hrs:02d}"


@register.filter
def td_minutes(timedelta):
    secs = timedelta.total_seconds()

    mins = int(secs // 60)

    return f"{mins:02d}"
