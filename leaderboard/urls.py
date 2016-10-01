from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leaderboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^login/$', 'accounts.views.login_user'),
    url(r'^auth/$', 'accounts.views.auth_login'),
)
