from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.members, name="members_index"),
]
