from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bib9website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', 'app.views.contact'),
    url(r'^$', 'app.views.home'),
    url(r'^index.html*', 'app.views.home'),
    url(r'^board*', 'app.views.board'),
    url(r'^tickets*', 'app.views.tickets'),
    url(r'^teams*', 'app.views.teams'),
    url(r'^posttest*', 'app.views.posttest'),

)
