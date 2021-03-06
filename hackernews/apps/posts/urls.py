from django.conf.urls import patterns, include, url
from .views import TopScorePostListView

from voting.views import vote_on_object
from .views import PostCreate, PostUpdate, PostDelete, PostDetail
from .models import Post
post_dict = {
    'model': Post,
    'template_object_name': 'post',
    'slug_field': 'slug',
    'allow_xmlhttprequest': 'true',
} 

urlpatterns = patterns(
    '',
    url(r'add/$', PostCreate.as_view(), name="post_create"),
    #url(r'(P?<pk>[0-9]+)/$', PostDetail.as_view(), name="post_detail"),
    #url(r'(?P<slug>[\w-]+)/?$', PostDetail.as_view(), name="post_detail"),
    url(r'^(?P<slug>[0-9]+-[0-9]+-[0-9]+/[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'(?P<pk>[0-9]+)/update/$', PostUpdate.as_view(), name="post_update"),    
    url(r'(?P<pk>[0-9]+)/delete/$', PostDelete.as_view(), name="post_delete"),
)

### VOTING ###
urlpatterns += (
    url(r'^(?P<object_id>\d+)/(?P<direction>up|down)vote/?$', vote_on_object, post_dict, name="post-voting-id"),
    url(r'^(?P<slug>[-\w]+)/(?P<direction>up|down)vote/?$', vote_on_object, post_dict, name="post-voting-slug"),
)

### COMMENTS ##
urlpatterns += (
    #url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^comments/', include('fluent_comments.urls')),


)
