from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _


def notice_count(user):
    """Get count of logged in user's notifications"""
    notice_count = notification.Notice.objects\
        .filter(recipient=user, unseen=1)\
        .count()
    return notice_count


