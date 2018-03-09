from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login
from django.urls import reverse
from django.shortcuts import redirect

from .utils import verify_link

User = get_user_model()


def members(request):
    u = request.GET.get("u", "")  # email
    e = request.GET.get("e", 0)  # timestamp
    t = request.GET.get("t", "")  # token
    secret = settings.TOKEN_SECRET
    has_access = verify_link(u, secret, e, t)

    if has_access:
        username = u.lower().strip().replace("@", "_at_").replace(".", "_dot_")
        user, created = User.objects.get_or_create(email=u, defaults={
            "username": username
        })
    else:
        # TEMP FIX, third party sometimes provide invalid user ids
        user, created = User.objects.get_or_create(username='Demo')

    if created:
        user.set_unusable_password()
        user.save()

    # login user without password
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    django_login(request, user)
    return redirect("/pages/instructions/")
