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

2. Get TOKEN_SECRET from env vars

   import os
   os.environ.get("TOKEN_SECRET")

3. Include the members URLconf in your project urls.py like this::

    url(r'^members/', include('members.urls')),

4. Set TOKEN_SECRET in env vars

   export TOKEN_SECRET=long-secret-token

5. Visit http://127.0.0.1:8000/members/ to validate signed tokens.
