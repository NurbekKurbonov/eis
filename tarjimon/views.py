from django.shortcuts import render

from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
import json

from django.shortcuts import render, redirect
from kirish.models import sahifa, savolnoma
from datetime import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden

from django.contrib.auth.decorators import user_passes_test
import six
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group

        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url='/login')

@group_required('Tarjimon')
def bosh_sahifa(request):
    return render(request, 'tarjimon/bosh_sahifa/00_bosh_sahifa_tarjimon.html')