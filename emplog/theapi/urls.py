from django.conf.urls import url
from .views import UsersView, PostUsersView, EditUsersView, DeleteUsersView

urlpatterns = [
    url(r'', UsersView.as_view()),
    url(r'post', PostUsersView.as_view()),
    url(r'edit/(?P<pk>[0-9]+)', EditUsersView.as_view()),
    url(r'delete/(?P<pk>[0-9]+)', DeleteUsersView.as_view()),
]