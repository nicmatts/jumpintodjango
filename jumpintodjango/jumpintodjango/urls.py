from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^questions/$', 'questionsandanswers.views.index'),
    url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail', name='question_detail'),

    #url(r'^$', 'questionsandanswers.views.home', name='home'),
    #url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail'),

    # Examples:
    # url(r'^$', 'jumpintodjango.views.home', name='home'),
    # url(r'^jumpintodjango/', include('jumpintodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
