from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
from nvd3.views import notice_count


@register.assignment_tag(name='get_notice_count')
def get_notice_count(user):
    """tag to display notice count"""
    return notice_count(user)
