from django import template
from events.models import SpecialEvent
import datetime

register = template.Library()


@register.assignment_tag
def get_upcoming_events(limit=None):
    event_list = SpecialEvent.objects.filter(end_date__gte=datetime.date.today(),
                                                           published=True)

    if limit is None:
        return event_list
    else:
        return event_list[:limit]