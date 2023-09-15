from django.urls import path
from .views import register, login, logout


app_name = "accounts"


urlpatterns = [
    path("register/", register, name = "register"),
    path("login/", login, name = "login"),
    path("logout/", logout, name = "logout")
]

urlpatterns = [
    url(r'^register/$', view=register, name='register'),
    url(r'^login/$', view=user_login, name='user-login'),
    url(r'^logout/$', view=user_logout, name='user-logout'),
    url(r'^settings/$', view=user_settings, name='user-settings'),
    url(r'^password-change/$', user_password_change, name='user-password-change'),
    url(r'^(?P<username>[-\w]+)/$', view=user_profile, name='user-profile'),
    url(r'^(?P<username>[-\w]+)/about/$', view=user_about, name='user-about')
]