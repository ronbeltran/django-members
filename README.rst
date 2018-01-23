=======
Members
=======

This provides a simple membership feature that relies on a third-party signed tokens.
Github Note: This is for private usage and will not fit your requirement.

Quick start
-----------

1. Add "members" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'members',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^members/', include('members.urls')),

3. Visit http://127.0.0.1:8000/members/ to validate signed tokens.
