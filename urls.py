import sys
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from cms.sitemaps import CMSSitemap

from basic.blog.feeds import BlogPostsFeed
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    # popit
    url(r'^popit/', include('popit.urls')),
    # mapit
    #url(r'^mapit/', include('mapit.urls')),

    # FileBrowser
    url(r'^admin/filebrowser/', include(site.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/rosetta/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # django comments
    #(r'^annotation/posted/$', 'views.comment_posted' ),
    (r'^annotation/', include('django.contrib.comments.urls')),

    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL + 'img/favicon.ico'}),

    # RSS feed
    url(r'^feeds/blog/$', BlogPostsFeed(), name='feed_blogposts'),

    # API
    url(r'^api/', include('api.urls'), name='api'),

    # SMS Alert
    url(r'^smsalert/', include('smsalert.urls'), name='smsalert'),

    # TinyMCE
    url(r'^tinymce/', include('tinymce.urls')),

    # Podcasting
    url(r"^podcasts/", include("podcasting.urls")),
    url(r"^feeds/podcasts/", include("podcasting.urls_feeds")),

    # CMS THIS MUST BE LAST -- IT INTERCEPTS EVERYTHING
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),


)


if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

if 'test' in sys.argv:
    urlpatterns = patterns('',
        url(r'test/representative/', include('representative.urls')),
        url(r'test/incomedeclaration/', include('incomedeclaration.urls')),
        url(r'test/votingrecord/', include('votingrecord.urls')),
        url(r'test/draftlaw/', include('draftlaw.urls')),
        url(r'test/question/', include('question.urls')),
        url(r'test/contact/', include('contact.urls')),
    ) + urlpatterns
