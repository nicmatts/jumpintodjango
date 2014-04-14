from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'jumpintodjango.views.homepage', name="homepage"),
    url(r'^questions/$', 'questionsandanswers.views.index', name='questions'),
    url(r'^login/$', 'jumpintodjango.views.login_page', name='login'),
    url(r'^logout/$', 'jumpintodjango.views.logout_view', name='logout'),
    url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail', name='question_detail'),
    url(r'^questions/create/$', 'questionsandanswers.views.question_create', name='question_create'),
    url(r'^questions/edit/(?P<question_id>\d+)$', 'questionsandanswers.views.question_edit', name='question_edit'),

    #url(r'^$', 'questionsandanswers.views.home', name='home'),
    #url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail'),

    # Examples:
    # url(r'^$', 'jumpintodjango.views.home', name='home'),
    # url(r'^jumpintodjango/', include('jumpintodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
