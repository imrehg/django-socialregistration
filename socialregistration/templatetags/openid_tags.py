from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('socialregistration/openid_form.html', takes_context=True)
def openid_form(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.TEMPLATE_CONTEXT_PROCESSORS set'
    logged_in = context['request'].user.is_authenticated()
    if 'next' in context:
        next = context['next']
    else:
        next = None
    return dict(next=next, logged_in=logged_in, MEDIA_URL=getattr(settings, 'MEDIA_URL', ''), STATIC_MEDIA_URL=getattr(settings, 'STATIC_MEDIA_URL', ''))
