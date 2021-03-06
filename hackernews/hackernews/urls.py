from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from posts.views  import TopScorePostListView
urlpatterns = patterns( 
    '',
    # Examples:
    # url(r'^$', 'hackernews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TopScorePostListView.as_view(), name='index'),
    (r'^accounts/', include('allauth.urls')),
    (r'^accounts/', include('profiles.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('posts.urls')),


)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
